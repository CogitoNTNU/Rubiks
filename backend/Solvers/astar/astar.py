from typing import Any, Callable, List, Union, Tuple

from magiccube import Cube

from backend.Solvers.astar.helpers import reconstruct_path
from backend.Solvers.astar.node import Node
from backend.utils import get_cube_str


def ida_star(
    initial_state: Cube,
    heuristic_fn: Callable[[Cube], float],
    create_children_fn: Callable[[Node], List[Node]],
    is_goal_fn: Callable[[Node], bool],
) -> Tuple[List[Node], int]:
    root = Node(state=initial_state)
    bound = heuristic_fn(root.state)
    path = [root]
    counter = 0

    while True:
        t, counter = search(
            path=path,
            g=0,
            bound=bound,
            heuristic_fn=heuristic_fn,
            create_children_fn=create_children_fn,
            is_goal_fn=is_goal_fn,
            counter=counter,
        )
        if t == "FOUND":
            return (
                reconstruct_path(path[-1]),
                counter,
            )  # Return the successful path and counter
        if t == float("inf"):
            return [], counter  # No solution exists
        bound = t  # Increase threshold


def search(
    path: List[Node],
    g: float,
    bound: float,
    heuristic_fn: Callable[[Cube], float],
    create_children_fn: Callable[[Node], List[Node]],
    is_goal_fn: Callable[[Node], bool],
    counter: int,
) -> Union[Tuple[float, int], Tuple[str, int]]:
    node = path[-1]
    counter += 1  # Increment the counter for each visited state
    f = g + heuristic_fn(node.state)
    if f > bound:
        return f, counter
    if is_goal_fn(node):
        print(f"The goal is {node.state}")
        return "FOUND", counter

    min_threshold = float("inf")
    ordering = sorted(
        create_children_fn(node),
        key=lambda child: g + heuristic_fn(child.state),
    )
    for succ in ordering:
        succ_state_str = get_cube_str(succ.state)
        if not any(get_cube_str(ancestor.state) == succ_state_str for ancestor in path):
            succ.parent = node  # Set parent for path reconstruction
            path.append(succ)

            t, counter = search(
                path=path,
                g=g + 1,  # Assuming uniform cost of 1 per move
                bound=bound,
                heuristic_fn=heuristic_fn,
                create_children_fn=create_children_fn,
                is_goal_fn=is_goal_fn,
                counter=counter,
            )

            if t == "FOUND":
                return "FOUND", counter
            if t < min_threshold:
                min_threshold = t
            path.pop()
    return min_threshold, counter
