from __future__ import annotations

from dataclasses import dataclass,asdict
from pathlib import Path
from typing import Literal


GraphType = Literal["gnp"]
StorageSplit = Literal["cache", "curated"]

@dataclass(slots=True, frozen=True)
class GraphSpec:
    num_vertices: int
    graph_type: GraphType = "gnp"
    directed: bool = False
    seed: int = 42
    edge_prob: float | None = None
    generator_version: str = "v1"

    def validate(self) -> None:
        if self.num_vertices <= 0:
            raise ValueError("num_vertices must be positive")
        if self.graph_type == "gnp":
            if self.edge_prob is None:
                raise ValueError("edge_prob must be provided for gnp graphs")
            if not (0 <= self.edge_prob <= 1):
                raise ValueError("edge_prob must be between 0 and 1")
            
    def to_dict(self) -> dict:
        return asdict(self)

    def __str__(self) -> str:
        return f"{self.graph_type}_n{self.num_vertices}_p{self.edge_prob}_s{self.seed}"
    

@dataclass(slots=True, frozen=True)
class DatasetPaths:
    graph_id:str
    split:StorageSplit
    base_dir: Path
    edge_file: Path
    meta_file: Path


@dataclass(slots=True, frozen=True)
class DatasetMeta:
    graph_id: str
    graph_type:str
    num_vertices: int
    num_edges: int
    directed: bool
    seed: int
    generator_version: str
    edge_file: str
    params: dict

    def to_dict(self) -> dict:
        return asdict(self)
    


