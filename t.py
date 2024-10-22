import magiccube
from Solvers.alg_solver import *
import numpy as np


# initialize cube
cube = magiccube.Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")
cube1 = magiccube.Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBYYYYYYYBYY")
cube2 = magiccube.Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")
cube3 = magiccube.Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")

print(cube)
cube.scramble()

algSolver = AlgSolver(cube).solve()
print(cube)
print(algSolver)

# cube.rotate("R U R2 F' R U R U' R' F R U' R' ")

# print(cube3)
# edges = [(0,0,1), (0,1,0), (0,1,2), (0,2,1), (1,0,0), (1,0,2), (1,2,0), (1,2,2), (2,0,1), (2,1,0), (2,1,2), (2,2,1)]
# algSolver = AlgSolver(cube3)
# for edge in edges:
#     print(f"Edge: {edge}, colors: {algSolver.get_color_by_coords(edge)}")

# print(cube1)
# print(algSolver1.get_color_by_coords((0, 0, 0)))
# print(algSolver1.get_color_by_coords((2, 2, 2)))
l = np.zeros(12)
l[3] = True
print(l)
