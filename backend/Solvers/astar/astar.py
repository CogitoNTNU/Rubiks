from typing import Any, Callable, Optional, Tuple, List

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
    raise NotImplementedError("IDA* function is not implemented.")


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
    raise NotImplementedError("Search function is not implemented.")
