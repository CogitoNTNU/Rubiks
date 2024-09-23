import magiccube
from Solvers.alg_solver import AlgSolver


# Create the cube in solved state
unscrambled = magiccube.Cube(
    3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW"
)
cube = magiccube.Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

# Print the cube

# cube.rotate("B")
# cube.rotate("U L F")
# cube.rotate("Y2 R U R' U R U2 R'")
# cube.rotate("Y2 R U R' U L U2 R'")


# print(cube)
# cube.get_piece((2, 2, 1))
# print(cube.get_piece((2, 2, 1)))
test = AlgSolver(cube)
print(cube.get_piece((2, 2, 1)))
print(cube.get_piece((1, 2, 2)).get_piece_colors_str(), "ah")
print(cube.get_piece((0, 2, 1)))
print(cube.get_piece((1, 2, 0)))
print(cube)
# print(test.get_home((2, 2, 1)))
