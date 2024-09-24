import magiccube
from Solvers.alg_solver import AlgSolver


# Create the cube in solved state
unscrambled = magiccube.Cube(
    3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY"
)
cube = magiccube.Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")


# Print the cube

cube.rotate("B")
# cube.rotate("U L F")
# cube.rotate("Y2 R U R' U R U2 R'")
# cube.rotate("Y2 R U R' U L U2 R'")
algSolver = AlgSolver(cube)


# Vi skal finne baser på kva som er på bufferen kor den skal og returnere den

print(cube)

piece = "YOB"
print(f"findPiece for '{piece}' {algSolver.findpiece(piece)}")
print(f"Get home by name '{piece}'' {algSolver.get_home_by_name(piece)}")
print(f"Get home by coords: {algSolver.get_home_by_coords(algSolver.findpiece(piece)[0])}")



