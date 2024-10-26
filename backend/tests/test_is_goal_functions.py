import pytest
from backend.Solvers.astar.node import Node
from backend.utils import get_cube_str
from magiccube import Cube
from backend.Solvers.astar.helpers import (
    is_goal_solved_cube,
    is_goal_domino_reduction,
    is_goal_oriented_edges,
)


# Helper function to create a solved cube node
def create_solved_node():
    # Assuming a solved cube is represented by Cube(size=3, solved_state=True) or similar
    solved_cube = Cube(3)  # Create a solved cube instance
    node = Node(state=solved_cube, parent=None, action=None, path_cost=0, depth=0)
    return node


# Helper function to create a scrambled cube node
def create_scrambled_node():
    scrambled_cube = Cube(3)  # Create a scrambled cube instance
    scrambled_cube.rotate("R U R' U'")  # Apply moves to scramble it
    node = Node(state=scrambled_cube, parent=None, action=None, path_cost=0, depth=0)
    return node


def test_is_goal_oriented_edges_with_solved_cube():
    node = create_solved_node()
    assert (
        is_goal_oriented_edges(node) is True
    ), "is_goal_oriented_edges should return True for a solved cube"


def test_is_goal_oriented_edges_with_scrambled_cube():
    node = create_scrambled_node()
    assert (
        is_goal_oriented_edges(node) is False
    ), "is_goal_oriented_edges should return False for a scrambled cube"


def test_is_goal_DR_with_solved_cube():
    node = create_solved_node()
    assert (
        is_goal_domino_reduction(node) is True
    ), "is_goal_DR should return True for a solved cube"


def test_is_goal_DR_with_scrambled_cube():
    node = create_scrambled_node()
    assert (
        is_goal_domino_reduction(node) is False
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
