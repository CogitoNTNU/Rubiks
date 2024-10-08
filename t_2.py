import magiccube
from Solvers.alg_solver import *
from Solvers.domino_solver import *


# initialize cube
cube = magiccube.Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")


# cube.rotate("R U R2 F' R U R U' R' F R U' R' ")

# print(cube)
algsolver = AlgSolver(cube)
print(algsolver.get_home_by_name("RWG"))
cube.scramble()
print(cube)

# letters = str(algsolver.get_color_by_coords((2, 2, 2)))

# print(algsolver.getalgfromcolor(letters))
# print(algsolver.getalgsbystr(algsolver.getalgfromcolor(letters)))
# print("-" * 100)
# for i in range(8):
#     letters = str(algsolver.get_color_by_coords((2, 2, 2)))
#     cube.rotate(algsolver.getalgsbystr(algsolver.getalgfromcolor(letters)))
#     print(cube)

# print()
# for i in range(8):
#     letters = list(algsolver.get_color_by_coords((2, 2, 2)))
#     cube.rotate(algsolver.getalg(algsolver.getalgfromcolor(letters)))


# print(algsolver.get_unformated_string())
# Default: kvite og gole på venstre face

dom = Domino_solver(cube)
print(dom.color_count_on_face("Y", "L"))
