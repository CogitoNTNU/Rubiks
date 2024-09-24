from magiccube.cube import Cube
from magiccube.optimizer.move_optimizer import MoveOptimizer
import magiccube


# innitialize solver
class AlgSolver:
    def __init__(self, cube: Cube, scramble=0) -> None:
        self.cube = cube
        self.solution = None
        self.scramble = scramble
        self.cornermem = None
        self.centers = None
        self.unscrambled = magiccube.Cube(
            3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW"
        )

    def findpiece(self, piece):
        # Find a piece based on the colors of the piece
        # i.e "BRW" gives 0,0,0 in uscrambled (white bottom yellow top)
        return self.cube.find_piece(piece)

    def get_home(self, coords):
        # Finds where a piece from a coordinate belongs
        return self.unscrambled.find_piece(str(self.cube.get_piece(coords)))[0]

    def getalg(letter):
        # Based on what letter is given,
        # this finds the algorithm to solve the pieces
        pass

    def getlettercenter(self, coords):
        # Gives a memorization letter based on the letterscheme
        # where the center piece should go
        pass

    def getlettercorner(self, coords):
        # Gives a memortization based on the letterscheme
        # where a corner piece should go
        pass

    def cyclebreak(self):
        # Solves a cycle by choosing a random piece that hasnt been solved
        # and moving the buffer to that spot
        pass


c = magiccube.Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

ass = AlgSolver(c)
