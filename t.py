import magiccube
from Solvers.alg_solver import *


# Create the cube in solved state
unscrambled = magiccube.Cube(
    3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY"
)
cube = magiccube.Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")
feil = magiccube.Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBGGGGGGGGG")

# Print the cube

# cube.rotate("F B")
# cube.rotate("U L F")
# cube.rotate("Y2 R U R' U R U2 R'")
# cube.rotate("Y2 R U R' U L U2 R'")
algSolver = AlgSolver(cube)


# Vi skal finne baser på kva som er på bufferen kor den skal og returnere den

# cube.rotate("D F' R F")
# print(cube)
# print(cube.get_piece((1, 0, 2)).get_piece_colors_str())


# piece = "YOB"
# print(f"findPiece for '{piece}' {algSolver.findpiece(piece)}")
# print(f"Get home by name '{piece}'' {algSolver.get_home_by_name(piece)}")
# print(
#    f"Get home by coords: {algSolver.get_home_by_coords(algSolver.findpiece(piece)[0])}"
# )
cube.scramble()
print(cube)
for i in range(20):
    color_str = cube.get_piece((1, 0, 2)).get_piece_colors_str()
    if "buffer" in algSolver.getalg(algSolver.getalgfromcolor(color_str)[0]):
        break
    print(algSolver.getalgfromcolor(color_str)[0])
    print(cube.get_piece((1, 0, 2)))
    cube.rotate(algSolver.getalg(algSolver.getalgfromcolor(color_str)[0]))
print(cube)
