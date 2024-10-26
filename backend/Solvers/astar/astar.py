from typing import Any, Callable, List, Optional, Tuple

from backend.Solvers.astar.node import Node


def ida_star(
    initial_state: Any,
    heuristic_fn: Callable[[Any], float],
    get_successors_fn: Callable[[Node], list],
    is_goal_fn: Callable[[Any], bool],
) -> Optional[List[Any]]:
    """
    Perform the Iterative Deepening A* search.

    Args:
        initial_state: The initial state from which to start the search.
        heuristic_fn: A function that takes a state and returns its heuristic value.
        get_successors_fn: A function that returns the successors of a given node.
        is_goal_fn: A function that tests whether a state is the goal.

    Returns:
        A list of actions to reach the goal, or None if no solution is found.
    """
    threshold = heuristic_fn(initial_state)
    while True:
        temp_threshold, path = search(
            initial_state, 0, threshold, heuristic_fn, get_successors_fn, is_goal_fn
        )
        if path is not None:
            return path
        if temp_threshold == float("inf"):
            return None
        threshold = temp_threshold


def search(
    node: Node,
    g: float,
    threshold: float,
    heuristic_fn: Callable[[Any], float],
    get_successors_fn: Callable[[Node], list],
    is_goal_fn: Callable[[Any], bool],
) -> Tuple[float, Optional[List[Any]]]:
    """
    Recursive depth-first search function used by IDA*.

    Args:
        node: The current node.
        g: The cost to reach the current node.
        threshold: The current threshold for f = g + h.
        heuristic_fn: The heuristic function.
        get_successors_fn: Function to get successors.
        is_goal_fn: Goal test function.

    Returns:
        A tuple containing:
            - The minimum f-value that exceeded the threshold, or float('inf') if no solution.
            - The path to the goal as a list of actions, or None if not found.
    """
    f = g + heuristic_fn(node)
    if f > threshold:
        return f, None
    if is_goal_fn(node):
        return f, []
    min_threshold = float("inf")
    for successor in get_successors_fn(node):
        successor_node, action, step_cost = successor
        temp_threshold, temp_path = search(
            successor_node,
            g + step_cost,
            threshold,
            heuristic_fn,
            get_successors_fn,
            is_goal_fn,
        )
        if temp_path is not None:
            return temp_threshold, [action] + temp_path
        if temp_threshold < min_threshold:
            min_threshold = temp_threshold
    return min_threshold, None
