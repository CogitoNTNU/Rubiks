from typing import Any, Callable, List, Union
from magiccube import Cube
from backend.Solvers.astar.helpers import reconstruct_path
from backend.Solvers.astar.node import Node
from backend.utils import get_cube_str


def ida_star(
    initial_state: Cube,
    heuristic_fn: Callable[[Cube], float],
    create_children_fn: Callable[[Node], List[Node]],
    is_goal_fn: Callable[[Node], bool],
) -> List[Node]:
    root = Node(state=initial_state)
    bound = heuristic_fn(root.state)
    path = [root]

    while True:
        t = search(
            path=path,
            g=0,
            bound=bound,
            heuristic_fn=heuristic_fn,
            create_children_fn=create_children_fn,
            is_goal_fn=is_goal_fn,
        )
        if t == "FOUND":
            # print(t)
            return reconstruct_path(path[-1])  # Return the successful path
        if t == float("inf"):
            return []  # No solution exists
        # print(f"Threshold: {t}")
        bound = t  # Increase threshold


def search(
    path: List[Node],
    g: float,
    bound: float,
    heuristic_fn: Callable[[Cube], float],
    create_children_fn: Callable[[Node], List[Node]],
    is_goal_fn: Callable[[Node], bool],
) -> Union[float, str]:
    node = path[-1]
    f = g + heuristic_fn(node.state)
    if f > bound:
        return f
    if is_goal_fn(node):
        print(f"The goal is {node.state}")
        return "FOUND"

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
 

            t = search(
                path=path,
                g=g + 1,  # Assuming uniform cost of 1 per move
                bound=bound,
                heuristic_fn=heuristic_fn,
                create_children_fn=create_children_fn,
                is_goal_fn=is_goal_fn,
            )

            if t == "FOUND":
                return "FOUND"
            if t < min_threshold:
                min_threshold = t
            path.pop()
    return min_threshold
