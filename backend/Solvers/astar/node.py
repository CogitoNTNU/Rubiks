from typing import Any, Optional
from dataclasses import dataclass
from magiccube import Cube


@dataclass
class Node:
    def __init__(
        self,
        state: Cube,
        parent: Optional["Node"] = None,
        action: Optional[Any] = None,
        path_cost: float = 0.0,
        depth: int = 0,
    ):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = depth
        self.f = 0  # f = g + h

    def __repr__(self):
        return f"Node(state={self.state}, f={self.f})"
