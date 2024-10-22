import numpy as np
from Solvers.alg_solver import *

from magiccube.cube import Cube
from magiccube.optimizer.move_optimizer import MoveOptimizer
import magiccube
from magiccube.cube_base import Face


class Domino_solver:
    def __init__(self, cube: Cube) -> None:
        self.cube = cube
        self.unscrambled = magiccube.Cube(
            3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY"
        )
        self.value = 0

    def check_corners(self):
        check_top_and_bottom_face_orientation = []

        # Corner coords specified in clockwise order
        top_corners = [(0, 2, 0), (2, 2, 0), (2, 2, 2), (0, 2, 2)]
        bottom_corners = [(0, 0, 0), (2, 0, 0), (0, 2, 2), (0, 0, 2)]
        for corner_coords in top_corners:
            corner_piece = self.cube.get_piece(corner_coords)
            print(f"Corner piece at {corner_coords}: {corner_piece}")

            # Check which of the corner pieces (white/yellow) are good or bad
            colors = corner_piece.get_piece_colors_str()[1]
            if "W" == colors or "Y" == colors:
                check_top_and_bottom_face_orientation.append(True)
            else:
                check_top_and_bottom_face_orientation.append(False)

        for corner_coords in bottom_corners:
            corner_piece = self.cube.get_piece(corner_coords)
            print(f"Corner piece at {corner_coords}: {corner_piece}")

            # Check which of the corner pieces (white/yellow) are good or bad
            colors = corner_piece.get_piece_colors_str()[1]
            if "W" == colors or "Y" == colors:
                check_top_and_bottom_face_orientation.append(True)
            else:
                check_top_and_bottom_face_orientation.append(False)
        return check_top_and_bottom_face_orientation

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
            pass

        pass

    def check_center(self):
        # Check if center has "good" orientation
        pass

    def orientationcount(self):
        # Count the number of good orientated edges and centers
        pass

    def get_face_by_center(self, face: str):
        face = self.cube.get_face(Face[face])
        ans = "".join("".join(str(color) for color in row) for row in face)
        ans = "".join([ans[x] for x in range(6, len(ans), 7)])
        return ans

    def color_edge_count_on_face(self, color: str = "Y", face: str = "L"):
        f = self.get_face_by_center(face)
        return sum([1 for x in range(1, 9, 2) if f[x] == color])

    def color_corner_count_on_face(self, color: str = "Y", face: str = "L"):
        f = self.get_face_by_center(face)
        return sum([1 for x in range(0, 9, 2) if f[x] == color and x != 4])

    def update_value(self, move):
        pass

    # sjekke om de 4 brikkene har bra orientasjon, om rett farge er rett
    # maske for hor mange brikker som har god orientrasjon, matrise som esieer hvor mange som har god orientrasjon
    # God: midt edges:
    def good_orientation(self):
        # Check if the cube has good orientation
        pass

    ## God orientasjon. Sjekk brikke OG, BO, RB, GR, dersom over eller under: farge skal vere feil, dersom på side, farge skal være rett

    ## OG = 0, GR = 1, RB = 2, BO = 3

    def mid_4_good(self):
        colors = ["OG", "GR", "RB", "BO"]
        for i in range(4):
            cur = l[i]
            if AlgSolver(self.cube).findpiece(colors[i]):
                pass

        # right/left slice -> se på fargen som peker "ut"

        print(AlgSolver(self.cube).findpiece("OG"))
        return 1
