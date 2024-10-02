import magiccube
from Solvers.alg_solver import *


# initialize cube
cube = magiccube.Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")


# cube.rotate("R U R2 F' R U R U' R' F R U' R' ")
cube.scramble()
algSolver = AlgSolver(cube)



print(algSolver.cube)
algSolver.solveedges()
print(algSolver.cube)
print(algSolver.solution, len(algSolver.solution))
# algSolver.solvecorners()
# print(algSolver.cube)
# print(algSolver.solution, len(algSolver.solution))
