import random
from typing import Any, Callable, List, Tuple, Union

import magiccube
import pytest
from magiccube import Cube

from backend.moves.sequence import simplify_sequence
from backend.Solvers.alg_solver import AlgSolver
from backend.Solvers.astar.astar import ida_star
from backend.Solvers.astar.helpers import *

# from backend.Solvers.astar.helpers import (
#     get_children_dr,
#     get_children_eo,
#     get_children_scrambled,
#     heuristic_DR,
#     heuristic_EO,
#     heuristic_solved,
#     is_goal_dr,
#     is_goal_eo,
#     is_goal_solved_cube,
# )
from backend.Solvers.astar.node import Node
from backend.Solvers.domino_solver import Domino_solver
from backend.utils import *


# Helper function to create a solved cube node
def create_solved_node():
    # Assuming a solved cube is represented by Cube(size=3, solved_state=True) or similar
    solved_cube = Cube(3)  # Create a solved cube instance
    node = Node(state=solved_cube, parent=None, action=None, path_cost=0, depth=0)
    return node


def test_solve_solved_cube():
    solved_cube = create_solved_node()
    path, counter, depth = ida_star(
        solved_cube.state, heuristic_solved, get_children_dr, is_goal_dr
    )
    assert len(path) == 1


def test_one_moves_to_solve():
    node = create_solved_node()
    node.state.rotate("U2")
    print(node.state)
    path, counter, depth = ida_star(
        node.state, heuristic_solved, get_children_dr, is_goal_solved_cube
    )
    print(path[0].state)

    assert len(path) == 2


def test_two_u_moves_to_solve():
    node = create_solved_node()
    node.state.rotate("U2")
    path, counter, depth = ida_star(
        node.state, heuristic_solved, get_children_dr, is_goal_solved_cube
    )
    print(path[0].state)
    assert len(path) == 2


def test_two_moves_to_solve():
    node = create_solved_node()

    node.state.rotate("R2 F2 ")  # DR state
    path, counter, depth = ida_star(
        node.state, heuristic_solved, get_children_dr, is_goal_solved_cube
    )
    print(path[0].state)
    assert len(path) == 3


def test_three_moves_to_solve():
    node = create_solved_node()

    node.state.rotate("R2 F2 D2")  # DR state
    path, counter, depth = ida_star(
        node.state, heuristic_solved, get_children_dr, is_goal_solved_cube
    )
    print(path[0].state)
    assert len(path) >= 4


def help_scramble(
    cube: Cube, state_checker: Callable[[Cube], float], n: int, key: str
) -> str:
    moves = ""
    set_cube = Cube(3, get_cube_str(cube))
    while len(moves.split(" ")) < n + 1:
        move = random.choice(LEGAL_MOVES[key])

        new_cube = Cube(3, get_cube_str(set_cube))
        new_cube.rotate(move)

        if state_checker == None:
            moves = moves + " " + move
            length = len(moves)
            moves = simplify_sequence(moves)

            if length == len(moves):
                set_cube = new_cube

        elif state_checker(new_cube) == 0:
            moves = moves + " " + move
            length = len(moves)
            moves = simplify_sequence(moves)

            if length == len(moves):
                set_cube = new_cube
    return moves.lstrip()


@pytest.mark.slow
def test_four_moves_to_solve():
    node = create_solved_node()
    moves = help_scramble(node.state, heuristic_DR, 8, "DR")
    i = 0
    for move in moves.split(" "):
        i += 1
        node.state.rotate(move)
        path, counter, depth = ida_star(
            node.state, heuristic_solved, get_children_dr, is_goal_solved_cube
        )
        print("moves away from solved: ", i)
        print("solution: ", [node.action for node in path])
        print(counter)
    print(moves)
    assert False


# @pytest.mark.slow
# def test_scrambled_to_eo():
#     node = create_solved_node()
#     node.state.rotate("F B R B ")  # scrambled
#     path, counter, depth = ida_star(
#         node.state, heuristic_EO, get_children_scrambled, is_goal_eo
#     )
#     for node in path:
#         print(node.action)

#     assert len(path) == 5
