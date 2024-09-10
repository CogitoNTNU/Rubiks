from magiccube.cube import Cube
from magiccube.optimizer.move_optimizer import MoveOptimizer
from magiccube.solver.basic.solver_base import SolverException, SolverStage
from magiccube.solver.basic.solver_stages import ConditionAction, stage_recenter_down, stage_recenter_front, stage_white_cross, \
    stage_white_corner, stage_2nd_layer, stage_top_cross, stage_order_top_cross, \
    stage_order_top_corners, stage_turn_top_corners
import alg_base
import magiccube

#Possible stages for the CFOP solve
#Trenger å definere :
# Hvit kryss, F2L (kan brytes opp i to deler, usikker på hvilken som er best), gult kryss, OLL, PLL
Stages ={

}


#innitialize solver
class AlgSolver:
    def __init__(self, cube: Cube  ) -> None:
        self.cube = cube
    def findpiece(self, piece):
        #Find 
        return self.cube.find_piece(piece)
    def getpiece(self, coords=(0,0,0)):
        return self.cube.get_piece(coords)
    
    def getstate(self):
        pass
    
    def solve(self):
        pass
    def getalg():
        pass

    
c = magiccube.Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

ass = AlgSolver(c)