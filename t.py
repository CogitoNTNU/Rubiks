import magiccube
from Solvers.alg_solver import *


# initialize cube
cube = magiccube.Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")


# cube.rotate("R U R2 F' R U R U' R' F R U' R' ")
print(cube)
algSolver = AlgSolver(cube)

print(algSolver.get_home_by_coords((2, 2, 2)))
print(algSolver.get_color_by_coords((2, 2, 2)))

# print(algSolver.getalg(algSolver.getalgfromcolor(letters)))

# for i in range(8):
#     letters = list(algSolver.get_color_by_coords((2, 2, 2)))
#     cube.rotate(algSolver.getalg(algSolver.getalgfromcolor(letters)))


print(algSolver.get_unformated_string())

# print(algSolver.cube)
# algSolver.solveedges()
# print(algSolver.cube)
# print(algSolver.solution, len(algSolver.solution))
# algSolver.solvecorners()
# print(algSolver.cube)
# print(algSolver.solution, len(algSolver.solution))
