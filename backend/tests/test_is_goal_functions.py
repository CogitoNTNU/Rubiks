import pytest
from magiccube import Cube

from backend.Solvers.astar.helpers import (
    heuristic_DR,
    heuristic_EO,
    is_goal_dr,
    is_goal_eo,
    is_goal_solved_cube,
)
from backend.Solvers.astar.node import Node
from backend.utils import get_cube_str


# Helper function to create a solved cube node
def create_solved_node():
    # Assuming a solved cube is represented by Cube(size=3, solved_state=True) or similar
    solved_cube = Cube(3)  # Create a solved cube instance
    node = Node(state=solved_cube, parent=None, action=None, g=0, depth=0)
    return node


# Helper function to create a scrambled cube node
def create_scrambled_node():
    scrambled_cube = Cube(3)  # Create a scrambled cube instance
    scrambled_cube.rotate("R U R' U'")  # Apply moves to scramble it
    node = Node(state=scrambled_cube, parent=None, action=None, g=0, depth=0)
    return node


def test_is_goal_oriented_edges_with_solved_cube():
    node = create_solved_node()
    assert (
        is_goal_eo(node) is True
    ), "is_goal_oriented_edges should return True for a solved cube"


def test_is_goal_oriented_edges_with_scrambled_cube():
    node = create_scrambled_node()
    assert (
        is_goal_eo(node) is False
    ), "is_goal_oriented_edges should return False for a scrambled cube"


def test_is_goal_DR_with_solved_cube():
    node = create_solved_node()
    assert is_goal_dr(node) is True, "is_goal_DR should return True for a solved cube"


def test_is_goal_DR_with_scrambled_cube():
    node = create_scrambled_node()
    assert (
        is_goal_dr(node) is False
    ), "is_goal_DR should return False for a scrambled cube"


def test_is_goal_solved_cube_with_solved_cube():
    node = create_solved_node()
    assert (
        is_goal_solved_cube(node) is True
    ), "is_goal_solved_cube should return True for a solved cube"


def test_is_goal_solved_cube_with_scrambled_cube():
    node = create_scrambled_node()
    assert (
        is_goal_solved_cube(node) is False
    ), "is_goal_solved_cube should return False for a scrambled cube"


def test_is_goal_dr_correct():
    node = create_solved_node()
    print(node.state)
    node.state.rotate("D2 R2 B2 F2 D2 B2")  # DR state
    val = heuristic_DR(node.state)
    print(f"DR heuristic value: {val}")
    print(node.state)
    assert is_goal_dr(node) is True, "The method does not detect when in DR"


def test_is_goal_dr_incorrect():
    node = create_solved_node()
    val = heuristic_DR(node.state)
    print(f"DR heuristic value: {val}")
    print(node.state)
    node.state.rotate("F R U R' U' R U R' U' R U R' U' F'")  # EO state
    print(node.state)
    assert is_goal_dr(node) is False, "The method does not detect when not in DR"


def test_is_goal_dr_incorrect2():
    node = create_solved_node()
    node.state.rotate("U")
    val = heuristic_DR(node.state)
    print(f"DR heuristic value: {val}")
    print(node.state)


def test_is_goal_eo_correct():
    node = create_solved_node()
    val = heuristic_EO(node.state)
    print(f"EO heuristic value: {val}")
    print(node.state)
    node.state.rotate("F R U R' U' R U R' U' R U R' U' F'")  # EO state
    assert is_goal_eo(node) is True, "is_goal_eo should return False for only EO state"
