from magiccube.cube import Cube
from magiccube.optimizer.move_optimizer import MoveOptimizer
from magiccube.solver.basic.solver_base import SolverException, SolverStage
from magiccube.solver.basic.solver_stages import ConditionAction, stage_recenter_down, stage_recenter_front, stage_white_cross, \
    stage_white_corner, stage_2nd_layer, stage_top_cross, stage_order_top_cross, \
    stage_order_top_corners, stage_turn_top_corners
import alg_base

#Possible stages for the CFOP solve
#Trenger å definere :
# Hvit kryss, F2L (kan brytes opp i to deler, usikker på hvilken som er best), gult kryss, OLL, PLL
Stages ={

}


#innitialize solver
class AlgSolver:
    def __init__(self, cube: Cube  ) -> None:
        self.cube = cube
        self.moves = ("R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "D", "D'", "D2", "F", "F'", "F2", "B", "B'", "B2")
        pass
    def findpiece(self):
        #Find 
        pass
    def findedge(self):
        pass
    def findcorner(self):
        pass
    def solve(self):
        pass
    def getalg():
        pass
    def solvecross(self):
        while self.cube.find_piece("WB")[0] == (1,0,0):

