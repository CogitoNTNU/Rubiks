import magiccube
from Solvers.alg_solver import *


# initialize cube
cube = magiccube.Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")
cube1 = magiccube.Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")
cube2 = magiccube.Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")
cube3 = magiccube.Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")


cube1.rotate("R U R2 F' R U R U' R' F R U' R' ")
cube.scramble()
print(cube)
algSolver = AlgSolver(cube)

print(algSolver.get_home_by_coords((2, 2, 2)))
print(algSolver.get_color_by_coords((2, 2, 2)))


print(algSolver.cube)
algSolver.solveedges()
print(algSolver.cube)
print(algSolver.solution, len(algSolver.solution))
algSolver.solvecorners()
print(algSolver.cube)
print(algSolver.solution, len(algSolver.solution))
