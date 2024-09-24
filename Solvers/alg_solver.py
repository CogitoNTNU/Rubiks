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
            3, "WWWWWWWWWRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBYYYYYYYYY"
        )

    def findpiece(self, piece):
        # Find a piece based on the colors of the piece
        # i.e "BRY" gives 0,0,0 in uscrambled (yellow bottom white top)
        return self.cube.find_piece(piece)

    def get_home_by_coords(self, coords):
        # Finds where a piece from a coordinate belongs based on its coords
        return self.unscrambled.find_piece(str(self.cube.get_piece(coords)))[0]

    def get_home_by_name(self, piece: str):
        # Finds where a piece from a coordinate belongs based on its name
        return self.unscrambled.find_piece(piece)[0]

    # def get_edge_

    def get_letter(
        self,
    ):
        pass

    def getalg(letter):
        # Based on what letter is given,
        # this finds the algorithm to solve the pieces
        pass

    def getlettercenter(self, coords):
        # Gives a memorization letter based on the letterscheme
        # where the pcenter iece should go
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
# print("DB")
