import magiccube
import pytest
from magiccube import Cube

from backend.Solvers.alg_solver import AlgSolver
from backend.Solvers.astar.astar import ida_star
from backend.Solvers.astar.helpers import (
    get_children_dr,
    get_children_eo,
    get_children_scrambled,
    heuristic_DR,
    heuristic_EO,
    heuristic_solved,
    is_goal_dr,
    is_goal_eo,
    is_goal_solved_cube,
)
from backend.Solvers.astar.node import Node
from backend.Solvers.domino_solver import Domino_solver


# Helper function to create a solved cube node
def create_solved_node():
    # Assuming a solved cube is represented by Cube(size=3, solved_state=True) or similar
    solved_cube = Cube(3)  # Create a solved cube instance
    node = Node(state=solved_cube, parent=None, action=None, path_cost=0, depth=0)
    return node


# DO DIS SHIZZLE MY NIZZLE FO SHO YO


@pytest.mark.slow
def test_eo_to_dr():
    node = create_solved_node()
    node.state.rotate("F2 B2 R2 B2 ")  # DR state
    moves = "U L U R"
    for move in moves.split(" "):
        node.state.rotate(move)
        path, counter = ida_star(node.state, heuristic_DR, get_children_eo, is_goal_dr)
        print(counter)
    assert False
