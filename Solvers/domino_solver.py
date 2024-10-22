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
        bottom_corners = [(0, 0, 0), (2, 0, 0), (2, 0, 2), (0, 0, 2)]
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
        self.results = np.zeros(12)

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
        return sum([1 for x in range(0, 9, 2) if f[x] == color and x != 4])

    def update_value(self, move):
        pass

    # sjekke om de 4 brikkene har bra orientasjon, om rett farge er rett
    # maske for hor mange brikker som har god orientrasjon, matrise som esieer hvor mange som har god orientrasjon
    # God: midt edges:
    def good_orientation(self):
        # Check if the cube has good orientation
        pass

    def get_edges(self, color: str = "Y", face: str = "L")->list:
        pass
        
            
    def check_edge_orientation(self, edge) -> bool:
        if(edge[1]=="1"):
        return False
        
        pass

    """
    Rekkefølg i edges:{
    Edge: (0, 0, 1), colors: OY
    Edge: (0, 1, 0), colors: OB
    Edge: (0, 1, 2), colors: OG
    Edge: (0, 2, 1), colors: OW
    Edge: (1, 0, 0), colors: YB
    Edge: (1, 0, 2), colors: YG
    Edge: (1, 2, 0), colors: WB
    Edge: (1, 2, 2), colors: WG
    Edge: (2, 0, 1), colors: RY
    Edge: (2, 1, 0), colors: RB
    Edge: (2, 1, 2), colors: RG
    Edge: (2, 2, 1), colors: RW
    }
    """
    
    #dei 4 i midten -> se om rett farge stikker ut
    def check_all_edges(self):

        up_or_low_edges = [(0,0,1), (0,2,1), (1,0,0), (1,0,2), (1,2,0), (1,2,2), (2,0,1), (2,2,1)]
        mid_edges = [(0,1,0), (0,1,2), (2,1,0), (2,1,2)]
        
        for i in range(8):
            self.results[i] = self.check_edge_orientation(up_or_low_edges[i])
       
        for i in range(4):
            #self.results[i+8] = ("W" in self.get_home_by_coords(mid_edges(i)) or "Y" in self.get_home_by_coords(mid_edges(i)))
            self.results[i+8] = check_mid_edges(mid_edges[i])
        return self.results
    #Rød/oransj kan ikkje på topp eller bunn, kvit/gul kan ikkje i midten og fargen må vere lik?
    #kan ikkje ver kvite eller gule på r/l

    def check_mid_edges(self, tuple: coords)->list:
        ("W" in self.get_home_by_coords(mid_edges(i)) or "Y" in self.get_home_by_coords(mid_edges(i)))
        # return [(check_edge_orientation(edge) for edge in edges)] (må fikse edges-lista)


    def color_edge_count_on_face(self, color: str = "Y", face: str = "L"):
        f = self.get_face_by_center(face)
        return sum([1 for x in range(1, 9, 2) if f[x] == color])
            cur = l[i]
            if AlgSolver(self.cube).findpiece(colors[i]):
                pass

        # right/left slice -> se på fargen som peker "ut"

        print(AlgSolver(self.cube).findpiece("OG"))
        return 1
