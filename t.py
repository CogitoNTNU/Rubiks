import magiccube
from Solvers.alg_solver import *


# initialize cube
cube = magiccube.Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")
cube1 = magiccube.Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")
cube2 = magiccube.Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")
cube3 = magiccube.Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")


# cube.rotate("R U R2 F' R U R U' R' F R U' R' ")

cube.scramble()
print(cube)

algSolver = AlgSolver(cube)

print(algSolver.solve())
print(algSolver.cube)
