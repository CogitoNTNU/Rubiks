from dataclasses import dataclass
from typing import Callable, Optional

from magiccube import Cube

from backend.utils import get_cube_str


@dataclass
class Node:

    def __init__(
        self,
        state: Cube,
        parent: Optional["Node"] = None,
        action: Optional[str] = None,
        g: float = 0.0,
        depth: int = 0,
        heuristic_fn: Optional[Callable[[Cube], float]] = None,
    ) -> None:
        self.state = state
        self.parent = parent
        self.action = action
        self.h = heuristic_fn(self.state) if heuristic_fn else 0
        self.g = g
        self.depth = depth

    @property
    def f(self) -> float:
        return self._f

    @property
    def g(self) -> float:
        return self._g

    @g.setter
    def g(self, value: float) -> None:
        self._g = value
        self._f = self.g + self.h

    def __repr__(self) -> str:
        return f"Node(state={self.state}, f={self.f})"

    def __lt__(self, other: "Node") -> bool:
        if isinstance(other, Node):
            if self.f == other.f:
                return self.h < other.h
            return self.f < other.f
        return NotImplemented

    def __eq__(self, other: "Node") -> bool:
        if isinstance(other, Node):
            return get_cube_str(self.state) == get_cube_str(other.state)
        return NotImplemented
