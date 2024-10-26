import magiccube
from backend.Solvers.alg_solver import AlgSolver
from backend.Solvers.astar.helpers import (
    get_children_dr,
    heuristic_DR,
    heuristic_solved,
    is_goal_dr,
    is_goal_solved_cube,
)
from backend.Solvers.domino_solver import Domino_solver
from backend.Solvers.astar.astar import ida_star
from magiccube import Cube
from backend.Solvers.astar.node import Node


# Helper function to create a solved cube node
def create_solved_node():
    # Assuming a solved cube is represented by Cube(size=3, solved_state=True) or similar
    solved_cube = Cube(3)  # Create a solved cube instance
    node = Node(state=solved_cube, parent=None, action=None, path_cost=0, depth=0)
    return node


def test_solve_solved_cube():
    solved_cube = create_solved_node()
    path = ida_star(solved_cube.state, heuristic_solved, get_children_dr, is_goal_dr)
    assert len(path) == 1


def test_one_moves_to_solve():
    node = create_solved_node()
    node.state.rotate("U2")
    print(node.state)
    path = ida_star(node.state, heuristic_solved, get_children_dr, is_goal_solved_cube)
    print(path[0].state)

    assert len(path) == 2


def test_two_u_moves_to_solve():
    node = create_solved_node()
    node.state.rotate("U2")
    path = ida_star(node.state, heuristic_solved, get_children_dr, is_goal_solved_cube)
    print(path[0].state)
    assert len(path) == 2


def test_one_moves_to_solve():
    node = create_solved_node()

    node.state.rotate("R2 F2 ")  # DR state
    path = ida_star(node.state, heuristic_solved, get_children_dr, is_goal_solved_cube)
    print(path[0].state)
    assert len(path) == 3


#  def test_one_moves_to_solve():
#     node = create_solved_node()
#
#     node.state.rotate("D2 R2 B2 F2 D2 B2")  # DR state
#     path = ida_star(node.state, heuristic_solved, get_children_dr, is_goal_solved_cube)
#     print(path[0].state)
#     assert len(path) == 2
