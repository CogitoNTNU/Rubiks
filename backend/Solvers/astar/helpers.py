from backend.Solvers.astar.node import Node


def heuristic(node: Node) -> float:
    """
    TODO: Implement the heuristic function.
    The heuristic should estimate the cost from the current state to the goal.

    Args:
        state: The current state.

    Returns:
        A numeric estimate of the cost to reach the goal from the current state.
    """
    raise NotImplementedError("Heuristic function is not implemented.")


def get_successors(node: Node) -> list[Node]:
    """
    TODO: Implement the successor function.
    This function should return a list of successors for a given state.

    Args:
        state: The current state.

    Returns:
        A list of tuples, each containing (action, successor_state, step_cost).
    """
    raise NotImplementedError("Successor function is not implemented.")


def is_goal(node: Node) -> bool:
    """
    TODO: Implement the goal test.

    Args:
        state: The current state.

    Returns:
        True if the state is a goal state, False otherwise.
    """
    raise NotImplementedError("Goal test function is not implemented.")
