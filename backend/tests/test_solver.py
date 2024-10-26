import magiccube
from backend.Solvers.alg_solver import AlgSolver


def run_3bld():
    print("[INFO] Running 3bld")


def test_solver_solves():

    c = magiccube.Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

    solver = AlgSolver(c)
    solution = solver.solve()
    assert solution is not None
    assert isinstance(solution, str)
