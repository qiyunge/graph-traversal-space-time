from dataclasses import dataclass


@dataclass
class TraversalStatistics:
    order: list[int]
    visited_count: int
    peak_frontier: int
