from magiccube import Cube

from backend.Solvers.astar.astar import a_star
from backend.Solvers.astar.helpers import *
from backend.utils import *

# Setup cube
cube = Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")
cube.scramble(2)
scrambled_cube = get_cube_str(cube)

# First stage
path, counter = a_star(
    cube,
    heuristic_fn=heuristic_EO,
    create_children_fn=get_children_scrambled,
    maxdepth=13,
    is_goal_fn=is_goal_eo,
)
solution1 = [node.action for node in path]
solution1.pop(0)
print(solution1)

for move in solution1:
    cube.rotate(move)


# Second state
eo_cube = get_cube_str(cube)
path, counter = a_star(
    cube,
    heuristic_fn=heuristic_DR,
    create_children_fn=get_children_eo,
    maxdepth=11,
    is_goal_fn=is_goal_dr,
)

solution2 = [node.action for node in path]
solution2.pop(0)
print(solution2)

for move in solution2:
    cube.rotate(move)

# Final state
dr_cube = get_cube_str(cube)
path, counter = a_star(
    cube,
    heuristic_fn=heuristic_solved,
    create_children_fn=get_children_dr,
    maxdepth=11,
    is_goal_fn=is_goal_solved_cube,
)

solution3 = [node.action for node in path]
solution3.pop(0)
print(solution3)

for move in solution3:
    cube.rotate(move)

# solution1, solution2, solution3 = ["Joe"], ["Joe"], ["Joe"]
# eo_cube, dr_cube = ["mama"], ["Joe"]

with open("Saved_solution", "w", encoding="UTF-8") as file:
    file.write("----------------")
    file.write(f"First stage: {scrambled_cube}, {solution1}\n")
    file.write(f"Second stage:  {eo_cube}, {solution2}\n")
    file.write(f"Final stage:  {dr_cube}, {solution3}\n")
    file.write("----------------")
