from magiccube.cube import Cube
from magiccube.optimizer.move_optimizer import MoveOptimizer
from magiccube.solver.basic.solver_base import SolverException, SolverStage
from magiccube.solver.basic.solver_stages import (
    ConditionAction,
    stage_recenter_down,
    stage_recenter_front,
    stage_white_cross,
    stage_white_corner,
    stage_2nd_layer,
    stage_top_cross,
    stage_order_top_cross,
    stage_order_top_corners,
    stage_turn_top_corners,
)
import alg_base
import magiccube

Stages = {}


# innitialize solver
class AlgSolver:
    def __init__(self, cube: Cube, scramble) -> None:
        self.cube = cube
        self.solution = None
        self.scramble = scramble
        self.cornermem = None
        self.centers = None

    def findpiece(self, piece):
        # Find a piece based on the colors of the piece
        # i.e "BRW" gives 0,0,0 in uscrambled (white bottom yellow top)
        return self.cube.find_piece(piece)

    def getpiece(self, coords=(0, 0, 0)):
        return self.cube.get_piece(coords)

    def getstate(self):
        pass

    
    def findedge(self):
        pass
    def get_corners(self):
        """returns coordinates and colors of all corners"""
        pieces = list(self.cube.get_all_pieces().items())
        corners = [(key,value) for key,value in pieces if not key[0]%2 and not key[1]%2 and not key[2]%2]
        return corners
    def solve(self):
        pass

    def getalg(letter):
        # Based on what letter is given,
        # this finds the algorithm to solve the pieces
        pass

    def getletter(self):
        # Based on what findpiece returns,
        # this function gives a memorization letter
        # where the piece should go
        pass

    def solvecross(self):
        """Solves the white cross"""
        i = 0
        while i<1000:
            self.cube.rotate(self.moves[i])
            if not self.cube.find_piece("WB")[0] == (1,0,0) and not self.cube.find_piece("WB")[0] == (0,1,0) and not self.cube.find_piece("WB")[0] == (0,0,1):
                self.cube.rotate(self.moves[i])
                self.cube.rotate(self.moves[i])
                self.cube.rotate(self.moves[i])
            else:
                self.cube.rotate(self.moves[i])
                self.cube.rotate(self.moves[i])
                self.cube.rotate(self.moves[i])
                break
            i+=1
        return self.moves[i]
    def solvef2l(self):
        """Solves the first two layers of the cube"""
        faces = self.cube.get_all_faces()
        corners = self.get_corners()

        print(corners)

        #solve the green and red corner
        #print(faces)
        #print(faces[Face.F])
        return ""

c = magiccube.Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

ass = AlgSolver(c)
