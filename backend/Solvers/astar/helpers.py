from backend.Solvers.astar.node import Node
from backend.utils import get_cube_str

LEGAL_MOVES = {
    "EO": [
        "R",
        "R'",
        "R2",
        "U",
        "U'",
        "U2",
        "D",
        "D'",
        "D2",
        "L",
        "L'",
        "L2",
        "F",
        "F'",
        "F2",
        "B",
        "B'",
        "B2",
    ],
    "DR": [
        "R",
        "R'",
        "R2",
        "U",
        "U'",
        "U2",
        "D",
        "D'",
        "D2",
        "L",
        "L'",
        "L2",
        "F2",
        "B2",
    ],
    "SOLVED": [
        "R2",
        "U2",
        "D2",
        "L2",
        "F2",
        "B2",
    ],
}


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


def reconstruct_path(node: Node) -> list[Node]:
    current_node = node
    succesors = []
    i = 0

    while current_node.parent is not None:
        step = (current_node.action, current_node.parent, i)
        current_node = current_node.parent
        succesors.append(step)
        i += 1

    step = (current_node.action, current_node.parent, i)
    succesors.append(step)
    succesors = succesors[::-1]
    return succesors

    """
    TODO: Implement the successor function.
    This function should return a list of successors for a given state.


    Args:
        state: The current state.

    Returns:
        A list of tuples, each containing (action, successor_state, step_cost).
    """
    return node.parrent
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


def is_goal_solved_cube(node: Node) -> bool:
    """
    Args:
        state: The current state.

    Returns:
        True if the state is a goal state, False otherwise.
    """
    cube_str = get_cube_str(node.state)

    for i in range(0, 54, 9):
        if cube_str[i : i + 9] != cube_str[i] * 9:
            return False
    return True


def get_children(node: Node, moves: list[str]) -> list[Node]:
    children = []
    for move in moves:
        child = node.state.rotate(move)
        children.append(child)
    return children
