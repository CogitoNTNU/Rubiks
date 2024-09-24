import magiccube
from Solvers.alg_solver import AlgSolver


# Create the cube in solved state
unscrambled = magiccube.Cube(
    3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY"
)
cube = magiccube.Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")


# Print the cube

cube.rotate("B")

cube.rotate("Y2 R U R' U R U2 R'")
cube.rotate("Y2 R U R' U L U2 R'")


# print(cube)
# cube.get_piece((2, 2, 1))
# print(cube.get_piece((2, 2, 1)))
test = AlgSolver(cube)
print(unscrambled.find_piece(str(cube.get_piece((2, 2, 1))))[0])
print(test.get_home((2, 2, 1)))
# print(test.get_home((2, 2, 1)))
print(unscrambled)
