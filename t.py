import magiccube
import Solvers.alg_solver as alg


# Create the cube in solved state
cube = magiccube.Cube(
    3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

# Print the cube

cube.rotate("B")

print(cube)
algthing = alg.AlgSolver(cube)


cube.rotate(algthing.solvef2l())

print(cube)