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
    maxdepth: int = 6,
) -> Tuple[List[Node], int, int]:
    root = Node(state=initial_state)
    bound = heuristic_fn(root.state)
    path = [root]
    counter = 0
    depth = 0
    while True:
        t, counter, depth = search(
            path=path,
            g=0,
            bound=bound,
            heuristic_fn=heuristic_fn,
            create_children_fn=create_children_fn,
            is_goal_fn=is_goal_fn,
            counter=counter,
            depth=depth,
            maxdepth=maxdepth,
        )
        if t == "FOUND":
            return (
                reconstruct_path(path[-1]),
                counter,
                depth,
            )  # Return the successful path and counter
        if t == float("inf"):
            return [], counter, depth  # No solution exists
        bound = t  # Increase threshold


def search(
    path: List[Node],
    g: float,
    bound: float,
    heuristic_fn: Callable[[Cube], float],
    create_children_fn: Callable[[Node], List[Node]],
    is_goal_fn: Callable[[Node], bool],
    counter: int,
    depth: int,
    maxdepth: int,
) -> Union[Tuple[float, int], Tuple[str, int], int]:
    if depth > maxdepth:
        return float("inf"), counter, depth  # Stop searching this path

    node = path[-1]
    counter += 1  # Increment the counter for each visited state
    f = g + heuristic_fn(node.state)
    if f > bound:
        return f, counter, depth
    if is_goal_fn(node):
        print(f"The goal is {node.state}")
        return "FOUND", counter, depth

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

            t, counter, newdepth = search(
                path=path,
                g=g + 1,  # Assuming uniform cost of 1 per move
                bound=bound,
                heuristic_fn=heuristic_fn,
                create_children_fn=create_children_fn,
                is_goal_fn=is_goal_fn,
                counter=counter,
                depth=depth + 1,
            )

            if t == "FOUND":
                return "FOUND", counter, newdepth
            if t < min_threshold:
                min_threshold = t
            path.pop()
    return min_threshold, counter
