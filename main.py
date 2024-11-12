import time
from datetime import timedelta

from magiccube import Cube

from backend.Solvers.astar.astar import a_star
from backend.Solvers.astar.helpers import *
from backend.utils import *

for i in range(1, 20):
    print("\n\n\n\n\n----------------")
    print(f"Scramble {i}")

    # Setup cube
    cube = Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")
    cube.scramble(i)
    moves = cube.history()
    print(f"Scramble {i}: {moves}")
    scrambled_cube = get_cube_str(cube)
    start = time.time()

    # First stage
    path, counter_EO = a_star(
        cube,
        heuristic_fn=heuristic_EO,
        create_children_fn=get_children_scrambled,
        is_goal_fn=is_goal_eo,
    )
    time_EO = time.time()
    print(f"Time to solve EO: {timedelta(seconds=time_EO - start)}")
    print(f"Nodes searched: {counter_EO}")

    solution1 = [node.action for node in path]
    solution1.pop(0)
    print(solution1)

    for move in solution1:
        cube.rotate(move)

    # Second state
    eo_cube = get_cube_str(cube)
    path, counter_DR = a_star(
        cube,
        heuristic_fn=heuristic_DR,
        create_children_fn=get_children_eo,
        is_goal_fn=is_goal_dr,
    )
    time_DR = time.time()
    print(f"Time to solve DR: {timedelta(seconds=time_DR - time_EO)}")
    print(f"Nodes searched: {counter_DR}")

    solution2 = [node.action for node in path]
    solution2.pop(0)
    print(solution2)

    for move in solution2:
        cube.rotate(move)

    # Final state
    dr_cube = get_cube_str(cube)
    path, counter_solved = a_star(
        cube,
        heuristic_fn=heuristic_solved,
        create_children_fn=get_children_dr,
        is_goal_fn=is_goal_solved_cube,
    )
    time_solved = time.time()
    print(f"Time to solve the cube: {timedelta(seconds=time_solved - time_DR)}")
    print(f"Nodes searched: {counter_solved}")

    solution3 = [node.action for node in path]
    solution3.pop(0)
    print(solution3)

    for move in solution3:
        cube.rotate(move)

    # solution1, solution2, solution3 = ["Joe"], ["Joe"], ["Joe"]
    # eo_cube, dr_cube = ["mama"], ["Joe"]

    with open("Saved_solution.txt", "a", encoding="UTF-8") as file:
        file.write("----------------\n")
        file.write(f"Scramble {i}: {moves}\n")
        file.write(f"First stage: {scrambled_cube}, {solution1}\n")
        file.write(f"Second stage:  {eo_cube}, {solution2}\n")
        file.write(f"Final stage:  {dr_cube}, {solution3}\n")
        file.write(f"Time to solve EO: {timedelta(seconds=time_EO - start)}\n")
        file.write(f"Time to solve DR: {timedelta(seconds=time_DR - time_EO)}\n")
        file.write(
            f"Time to solve the cube: {timedelta(seconds=time_solved - time_DR)}\n"
        )
        file.write(f"Total time: {timedelta(seconds=time_solved - start)}\n")
        file.write(f"Nodes searched for EO: {counter_EO}\n")
        file.write(f"Nodes searched for DR: {counter_DR}\n")
        file.write(f"Nodes searched for the cube: {counter_solved}\n")
        file.write(
            f"Total searched nodes: {counter_EO + counter_DR + counter_solved}\n"
        )
        file.write("----------------\n")
