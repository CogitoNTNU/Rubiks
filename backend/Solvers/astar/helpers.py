from backend.Solvers.astar.node import Node
from backend.Solvers.domino_solver import Domino_solver
from backend.Solvers.alg_solver import AlgSolver


def heuristic_EO(node: Node) -> float:
    cube = node.state
    cube = Domino_solver(cube)

    alligned_edges = 0

    alligned_edges += cube.check_all_edges(False)
    alligned_edges += cube.check_all_edges(True)

    return 24 - alligned_edges


def heuristic_DR(node: Node) -> float:
    cube = node.state
    cube = Domino_solver(cube)

    faces = 0

    faces += cube.color_edge_count_on_face("W", "U")
    faces += cube.color_corner_count_on_face("W", "U")

    faces += cube.color_edge_count_on_face("Y", "U")
    faces += cube.color_corner_count_on_face("Y", "U")

    faces += cube.color_edge_count_on_face("W", "D")
    faces += cube.color_corner_count_on_face("W", "D")

    faces += cube.color_edge_count_on_face("Y", "D")
    faces += cube.color_corner_count_on_face("Y", "D")

    return 16 - faces


def heuristic_solved(node: Node) -> float:
    # Checks how many faces are the same as the center

    cube = node.state
    cube = Domino_solver(cube)

    faces = 0

    colors = ["W", "Y", "R", "O", "G", "B"]

    for color in colors:
        faces += cube.get_face_by_center(color).count(color) - 1

    return 48 - faces


def get_successors(node: Node) -> list[Node]:
    current_node = node
    succesors = []
    i = 0

    while current_node.parent is not None:
        step = (current_node.action, current_node.parent, i)
        current_node = current_node.parent
        succesors.append(step)
        i += 1

    step = (current_node.action, current_node.parent, i)

    return succesors

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
