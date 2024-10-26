from backend.Solvers.astar.node import Node
from magiccube import Cube
from backend.Solvers.astar.helpers import (
    heuristic_EO,
    heuristic_DR,
    heuristic_solved,
)


def test_heuristic_solved_on_solved_cube():
    cube = Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")
    node = Node(cube, None, None, 0, 0)

    assert heuristic_solved(node) == 0

    cube = Cube(3, "RRRRRRRRRYYYYYYYYYGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")
    node = Node(cube, None, None, 0, 0)

    assert heuristic_solved(node) == 0

    cube = Cube(3, "RRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBYYYYYYYYYWWWWWWWWW")
    node = Node(cube, None, None, 0, 0)

    assert heuristic_solved(node) == 0


def test_heuristic_solved_one_move_away():
    cube = Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")
    cube.rotate("R")

    node = Node(cube, None, None, 0, 0)

    assert heuristic_solved(node) == 12


def test_heuristic_solved_complex():
    cube = Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")
    cube.rotate("R U F R F")

    node = Node(cube, None, None, 0, 0)

    assert heuristic_solved(node) == 48 - 17


def test_heuristic_DR_on_solved_cube():
    cube = Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")
    node = Node(cube, None, None, 0, 0)

    assert heuristic_DR(node) == 0


def test_heuristic_DR_complex():
    cube = Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")
    cube.rotate("R U F R F")

    node = Node(cube, None, None, 0, 0)

    assert heuristic_DR(node) == 16 - 9


def test_heuristic_EO_on_solved_cube():
    cube = Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")
    node = Node(cube, None, None, 0, 0)

    assert heuristic_EO(node) == 0


def test_heuristic_EO_complex():
    cube = Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")
    cube.rotate("R U F R F")

    node = Node(cube, None, None, 0, 0)

    assert heuristic_EO(node) == 4
