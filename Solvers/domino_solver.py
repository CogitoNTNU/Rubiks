import magiccube
from magiccube.cube import Cube
from magiccube.optimizer.move_optimizer import MoveOptimizer
from magiccube.solver.basic.solver_base import SolverException, SolverStage


class Domino_solver:
    def __init__(self, cube: Cube) -> None:
        self.cube = cube
        pass

    def check_edge(self, edge_pos: tuple):
        # Check if edge has "good" orientation
        """Doesn't work yet!"""

        # I think if we instead look at the string of the edge it will tell us everything we need to know.
        # on the top, the edge pieces are weirdly ordered. Will discuss this tomorrow
        edge = self.cube.get_piece(edge_pos)
        color1, color2 = edge[1].get_piece_colors_str()
        if (color1 == "W" or color1 == "Y") and not edge[0][1] % 2:
            # checks if the edge is in bottom or top layer and that white or yellow is pointing vertically
            # could also be checked to see if white or yellow face is lying on the top or bottom face
            print("Edge is good")
        elif (color2 == "G" or color2 == "B") and edge[0][1] % 2:
            # if middle layer position, checks if green and blue color is facing same direction as the blue and green centers.
            ...

        pass

    def check_center(self):
        # Check if center has "good" orientation
        pass

    def orientationcount(self):
        # Count the number of good orientated edges and centers

        pass
