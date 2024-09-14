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


c = magiccube.Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

ass = AlgSolver(c)
