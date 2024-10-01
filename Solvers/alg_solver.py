from magiccube.cube import Cube
from magiccube.optimizer.move_optimizer import MoveOptimizer
import magiccube

letters = {
    "A": "buffer",
    "B": "R2",
    "C": "F2 D",
    "D": "F2",
    "E": "buffer",
    "F": "F' D",
    "G": "F'",
    "H": "D' R",
    "I": "F R'",
    "J": "R'",
    "K": "R' D'",
    "L": "F2 R'",
    "M": "R D'",
    "N": "R' F",
    "O": "R2 F",
    "P": "F F",
    "Q": "R D'",
    "R": "buffer",
    "S": "D F'",
    "T": "R",
    "U": "D",
    "V": "",
    "W": "D'",
    "X": "D2",
    "a": "M2",
    "b": "R U R' U'",
    "c": "U B' R U' B M2 B' U R' B U'",
    "d": "L' U' L U",
    "e": "B L' B'",
    "f": "B L2 B'",
    "g": "B L B'",
    "h": "L B L' B'",
    "i": "D M' U R2 U' M U R2 U' D' M2",
    "j": "U R U'",
    "k": "buffer",
    "l": "U' L' U",
    "m": "B' R B",
    "n": "R' B' R B",
    "o": "B' R' B",
    "p": "B' R2 B",
    "q": "U B' R U' B M2 B' U R' B U'",
    "r": "U' L U",
    "s": " M2' D U R2 U' M' U R2 U' M D'",
    "t": "U R' U'",
    "u": "buffer",
    "v": "U R2 U'",
    "w": "M U2 M U2",
    "x": "U' L2 U",
}
algs_from_color = {
    "WG": "ci",
    "WO": "de",
    "WB": "aq",
    "WR": "bm",
    "GO": "lf",
    "GR": "jp",
    "BR": "tn",
    "BO": "rh",
    "YG": "uk",
    "YR": "ov",
    "YB": "ws",
    "YO": "xg",
    "WOB": "AER",
    "RWB": "BQN",
    "RWG": "CMJ",
    "WGO": "DIF",
    "YOB": "XSH",
    "YBR": "WTO",
    "YRG": "VPK",
    "YGO": "ULG",
}
special_cases = ["a", "c", "i", "q", "s", "w"]


# innitialize solver
class AlgSolver:
    def __init__(self, cube: Cube, scramble=0) -> None:
        self.cube = cube
        self.solution = None
        self.scramble = scramble
        self.cornermem = None
        self.centers = None
        self.unscrambled = magiccube.Cube(
            3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY"
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

    def reversealg(self, alg: str):
        # reverses the given algorithm
        alg_list = alg.split(" ")
        alg_list.reverse()
        for i in range(len(alg_list)):
            if "'" in alg_list[i]:
                alg_list[i] = alg_list[i].replace("'", "")
            elif "2" not in alg_list[i]:
                alg_list[i] = alg_list[i] + "'"
        return " ".join(alg_list)

    def getalg(self, letter: str):
        """
        Finds an algorithm to solve case Based on what letter is given.
        this finds the algorithm to solve the pieces
        """
        if letter in special_cases:
            return letters[letter]
        alg_str = ""
        if letter == letter.upper():  # is a corner
            alg_str += letters[letter]
            alg_str += " R U' R' U' R U R' F' R U R' U' R' F R "
            alg_str += self.reversealg(letters[letter])
        else:  # is an edge
            alg_str += letters[letter]
            alg_str += " M2 "
            alg_str += self.reversealg(letters[letter])

        return alg_str

    def getalgs(self, letters):
        # gets the algorithm for a list of letters
        algs = ""
        for letter in letters.split(" "):
            algs += self.getalg(letter) + " "
        return algs

    def getlettercenter(self, coords):
        # Gives a memorization letter based on the letterscheme
        # where the center piece should go
        pass

    def getalgfromcolor(self, letters):
        keys = algs_from_color.keys()
        if len(letters) == 2:
            if letters in keys:
                return algs_from_color[letters]
            else:
                letters = letters[::-1]
                if letters in keys:
                    return algs_from_color[letters]
                else:
                    return None
        elif len(letters) == 3:
            for _ in range(2):
                letters = letters[1:] + letters[0]
                if letters in keys:
                    return algs_from_color[letters]
            letters = letters[0] + letters[2] + letters[1]
            for _ in range(2):
                letters = letters[1:] + letters[0]
                if letters in keys:
                    return algs_from_color[letters]
            return None

    def getlettercorner(self, coords):
        # Gives a memortization based on the letterscheme
        # where a corner piece should go
        pass

    def cyclebreak(self):
        # Solves a cycle by choosing a random piece that hasnt been solved
        # and moving the buffer to that spot
        pass

    def solve(self) -> str:
        # TODO: put everything together
        return ""


if __name__ == "__main__":
    c = magiccube.Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

    solver = AlgSolver(c)
    solver.solve()
    # print("DB")
