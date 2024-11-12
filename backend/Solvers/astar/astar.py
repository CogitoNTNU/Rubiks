import heapq
from typing import Any, Callable, List, Tuple, Union

from magiccube import Cube

from backend.Solvers.astar.helpers import reconstruct_path
from backend.Solvers.astar.node import Node
from backend.utils import get_cube_str


def a_star(
    initial_state: Cube,
    heuristic_fn: Callable[[Cube], float],
    create_children_fn: Callable[[Node], List[Node]],
    is_goal_fn: Callable[[Node], bool],
) -> Tuple[List[Node], int]:
    root = Node(state=initial_state, heuristic_fn=heuristic_fn)
    counter = 0
    finished = False
    heap = []
    visited = set()

    heapq.heappush(heap, root)

    while not finished:
        node = heapq.heappop(heap)
        if is_goal_fn(node):
            finished = True
        children = create_children_fn(node)

        for child in children:
            if get_cube_str(child.state) not in visited:
                visited.add(get_cube_str(child.state))
                heapq.heappush(heap, child)
        counter += 1

    return reconstruct_path(node), counter
