import magiccube
from backend.Solvers.alg_solver import AlgSolver
from backend.Solvers.astar.helpers import get_children_dr, heuristic_DR, is_goal_dr
from backend.Solvers.domino_solver import Domino_solver
from backend.Solvers.astar.astar import ida_star 
from magiccube import Cube
from backend.Solvers.astar.node import Node



# Helper function to create a solved cube node
def create_solved_node():
    # Assuming a solved cube is represented by Cube(size=3, solved_state=True) or similar
    solved_cube = Cube(3)  # Create a solved cube instance
    node = Node(state=solved_cube, parent=None, action=None, path_cost=0, depth=0)
    return node

def test_solve_solved_cube():
    solved_cube = create_solved_node()
    path = ida_star(solved_cube.state, heuristic_DR, get_children_dr, is_goal_dr )
    assert len(path)==1

