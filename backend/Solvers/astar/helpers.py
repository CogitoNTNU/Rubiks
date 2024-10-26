from backend.Solvers.astar.node import Node
from backend.Solvers.domino_solver import Domino_solver
from backend.Solvers.alg_solver import AlgSolver
from backend.utils import get_cube_str
from magiccube import Cube

LEGAL_MOVES = {
    "SCRAMBLED": [
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
        "F2",
        "B2",
    ],
    "DR": [
        "R2",
        "U2",
        "D2",
        "L2",
        "F2",
        "B2",
    ],
}


def heuristic_EO(cube: Cube) -> float:

    cube = Domino_solver(cube)

    alligned_edges = 0

    alligned_edges += cube.check_all_edges(False)
    alligned_edges += cube.check_all_edges(True)

    return 24 - alligned_edges


def heuristic_DR(cube: Cube) -> float:
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


def heuristic_solved(cube: Cube) -> float:
    # Checks how many faces are the same as the center
    cube = Domino_solver(cube)

    sum = 0

    faces = ["L", "R", "D", "U", "B", "F"]

    for i in range(6):
        face = cube.get_face_by_center(faces[i])
        center_color = face[4]
        face = face[:4] + face[5:]
        sum += face.count(center_color)

    return 48 - sum


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



def is_goal_eo(node: Node) -> bool:
    """
    Args:
        state: The current state.

    Returns:
        True if the state is a goal state, False otherwise.
    """
    return heuristic_EO(node.state) == 0


def is_goal_dr(node: Node) -> bool:
    """
    Args:
        state: The current state.

    Returns:
        True if the state is a goal state, False otherwise.
    """
    return heuristic_DR(node.state) == 0


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
        copy_node = copy(node)
        copy_node.state.rotate(move)
        children.append(copy_node)
        copy_node.depth = node.depth + 1
    return children


def get_children_scrambled(node: Node) -> list[Node]:
    return get_children(node, LEGAL_MOVES["SCRAMBLED"])


def get_children_eo(node: Node) -> list[Node]:
    return get_children(node, LEGAL_MOVES["EO"])


def get_children_dr(node: Node) -> list[Node]:
    return get_children(node, LEGAL_MOVES["DR"])


def copy(node: Node) -> Node:
    cube_copy = Cube(node.state.size, get_cube_str(node.state))
    return Node(cube_copy, node.parent, node.action, node.path_cost, node.depth)
