import magiccube
from Solvers.alg_solver import *
from Solvers.domino_solver import *


# initialize cube
cube_white_top = magiccube.Cube(
    3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY"
)
cube_yellow_top = magiccube.Cube(
    3, "YYYYYYYYYOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBWWWWWWWWW"
)


print(cube_white_top)

algsolver = AlgSolver(cube_white_top)
domino_solver = Domino_solver(cube_white_top)


domino_solver.cube.scramble()
print(domino_solver.cube)

print("-" * 100)
print("Top face")
print(domino_solver.check_corners())
print("-" * 100)
