from magiccube import Cube
from backend.Solvers.astar.helpers import (
    heuristic_EO,
    heuristic_DR,
    heuristic_solved,
)


def test_heuristic_solved_on_solved_cube():
    cube = Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

    assert heuristic_solved(cube) == 0

    cube = Cube(3, "RRRRRRRRRYYYYYYYYYGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

    assert heuristic_solved(cube) == 0

    cube = Cube(3, "RRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBYYYYYYYYYWWWWWWWWW")

    assert heuristic_solved(cube) == 0


def test_heuristic_solved_one_move_away():
    cube = Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")
    cube.rotate("R")

    assert heuristic_solved(cube) == 12


def test_heuristic_solved_complex():
    cube = Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")
    cube.rotate("R U F R F")

    assert heuristic_solved(cube) == 48 - 17


def test_heuristic_DR_on_solved_cube():
    cube = Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

    assert heuristic_DR(cube) == 0


def test_heuristic_DR_complex():
    cube = Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")
    cube.rotate("R U F R F")

    assert heuristic_DR(cube) == 16 - 9


def test_heuristic_EO_on_solved_cube():
    cube = Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

    assert heuristic_EO(cube) == 0


def test_heuristic_EO_complex():
    cube = Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")
    cube.rotate("R U F R F")

    assert heuristic_EO(cube) == 4
