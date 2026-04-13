from dataclasses import dataclass


@dataclass
class TraversalResult:
    order: list[int]
    visited_count: int
    peak_frontier: int
