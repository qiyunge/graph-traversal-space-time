from __future__ import annotations

import csv
import json

from dataclasses import replace
from pathlib import Path

from .generator import generate_edges
from .schemas import GraphSpec, DatasetMeta, DatasetPaths, StorageSplit

class DatasetManager:
    def __init__(self,datasets_root:str|Path) -> None:
        self.datasets_root = Path(datasets_root)

    def make_graph_id(self, spec: GraphSpec) -> str:
        spec.validate()

        direction = "dir" if spec.directed else "undir"

        if spec.graph_type == "gnp":
            p_token = self._format_prob_token(spec.edge_prob)
            return (f"gnp_n{spec.num_vertices}_p{p_token}"
                    f"_s{spec.seed}_{direction}_{spec.generator_version}")
        

        raise NotImplementedError(f"Graph type {spec.graph_type} not supported")
    
    def get_paths(self,
                  spec: GraphSpec,
                  split: StorageSplit = "cache") -> DatasetPaths:
                 
        graph_id = self.make_graph_id(spec)
        base_dir = self.datasets_root / split
        edge_file = base_dir / f"{graph_id}_edges.csv"
        meta_file = base_dir / f"{graph_id}_meta.json"  
        return DatasetPaths(graph_id=graph_id, split=split,
                            base_dir=base_dir, edge_file=edge_file,
                            meta_file=meta_file)
    
    def exists(self, 
               spec: GraphSpec,
               split: StorageSplit = "cache") -> bool:
        paths = self.get_paths(spec, split = split)
        return paths.edge_file.exists() and paths.meta_file.exists()
    
    def ensure_dataset(self,
                       spec: GraphSpec,
                       split: StorageSplit = "cache",
                       overwrite: bool = False ) -> DatasetMeta:
        paths = self.get_paths(spec, split = split)
        paths.base_dir.mkdir(parents=True, exist_ok=True)

        if not overwrite and self.exists(spec, split):
           return self.load_meta(spec, split)

        edges = generate_edges(spec)
        self._write_edges(paths.edge_file, edges)
        meta = self._build_meta(spec, paths,num_edges = len(edges))
        self._write_meta(paths.meta_file, meta)
        return meta
    
    def load_meta(self, spec: GraphSpec, split: StorageSplit = "cache") -> DatasetMeta: 
        paths = self.get_paths(spec, split = split)
        if not paths.meta_file.exists():
            raise FileNotFoundError(f"Meta file not found: {paths.meta_file}")
        with paths.meta_file.open( "r", encoding="utf-8") as f:
            data = json.load(f)
        return DatasetMeta(**data)
    
    def load_edges(self, spec: GraphSpec, split: StorageSplit = "cache") -> list[tuple[int, int]]:
        paths = self.get_paths(spec, split = split)
        if not paths.edge_file.exists():
            raise FileNotFoundError(f"Edge file not found: {paths.edge_file}")
        return self.read_edges_by_path(paths.edge_file)
    
    def read_edges_by_path(self, edge_file:str| Path) -> list[tuple[int, int]]:
        edge_path  = Path(edge_file)
        edges :list[tuple[int, int]] = []

        with edge_path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if len(row) != 2:
                    raise ValueError(f"Invalid edge row: {row}")
                edges.append((int(row["src"]), int(row["dst"])))

        return edges    
    
    def freeze_to_curated(self, spec: GraphSpec) -> DatasetMeta:
        cache_paths = self.get_paths(spec, split="cache")
        curated_paths = self.get_paths(spec, split="curated")

        if not cache_paths.edge_file.exists() or not cache_paths.meta_file.exists():
            self.ensure_dataset(spec, split="cache")
        
        curated_paths.base_dir.mkdir(parents=True, exist_ok=True)
        curated_paths.edge_file.write_bytes(cache_paths.edge_file.read_bytes())
        curated_paths.meta_file.write_bytes(cache_paths.meta_file.read_bytes())

        meta = self.load_meta(spec, split="curated")
        return meta
    
    def _build_meta(self, spec: GraphSpec, paths: DatasetPaths, num_edges:int) -> DatasetMeta:
        params = {}
        if spec.graph_type == "gnp":
            params["edge_prob"] = spec.edge_prob
        
        
        return DatasetMeta(
            graph_id=paths.graph_id,
            graph_type=spec.graph_type,
            num_vertices=spec.num_vertices,
            num_edges=num_edges,
            directed=spec.directed,
            seed=spec.seed,
            generator_version=spec.generator_version,
            edge_file= paths.edge_file.name,
            params= params
        )
    
    def _write_edges(self, edge_file: Path, edges: list[tuple[int, int]]) -> None:
        with edge_file.open("w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["src", "dst"])
            writer.writerows(edges) 

    
    def _write_meta(self, meta_file: Path, meta: DatasetMeta) -> None:
        with meta_file.open("w", encoding="utf-8") as f:
            json.dump(meta.to_dict(), f, indent=4, ensure_ascii=False)

    @staticmethod
    def _format_prob_token(p: float | None) -> str:
        if p is None:
            return ValueError("p cannot be None for gnp graphs")
        token = f"{p:.4f}".rstrip("0").rstrip(".")
        return token.replace(".", "d")