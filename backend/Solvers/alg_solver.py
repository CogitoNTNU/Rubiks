import magiccube
from magiccube.cube import Cube, Face
from magiccube.optimizer.move_optimizer import MoveOptimizer

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
    "M": "F",
    "N": "R' F",
    "O": "R2 F",
    "P": "R F",
    "Q": "R D'",
    "R": "buffer",
    "S": "D F'",
    "T": "R",
    "U": "D",
    "V": "R R'",
    "W": "D'",
    "X": "D2",
    "a": "M2",
    "b": "R U R' U'",
    "c": "U2 M' U2 M'",
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
    "s": "M2 D U R2 U' M' U R2 U' M D'",
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
    "YR": "vo",
    "YB": "ws",
    "YO": "xg",
    "OWB": "EAR",
    "RWB": "NBQ",
    "RWG": "MCJ",
    "OWG": "FDI",
    "OYB": "HXS",
    "RYB": "OWT",
    "RYG": "PVK",
    "OYG": "GUL",
}
special_cases = ["a", "c", "i", "q", "s", "w"]


# innitialize solver
class AlgSolver:
    def __init__(self, cube: Cube, scramble=0) -> None:
        self.cube = cube
        self.solution = []
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
        if coords == ((1, 1, 1)):
            return (1, 1, 1)
        return self.unscrambled.find_piece(str(self.cube.get_piece(coords)))[0]

    def get_color_by_coords(self, coords):
        return self.cube.get_piece(coords).get_piece_colors_str()

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
            elif "2" not in alg_list[i] and len(alg_list) > 0:
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

    def getalgsbystr(self, letters) -> str:
        # gets the algorithm for a list of letters
        algs = ""
        for letter in letters:
            algs += self.getalg(letter) + " "
        return algs

    def getalgfromcolor(self, letters):
        keys = algs_from_color.keys()  # gets the different corner color combinations
        if len(letters) == 2:
            if letters in keys:
                return algs_from_color[letters]
            else:
                letters = letters[::-1]
                if letters in keys:
                    return algs_from_color[letters][::-1]
                else:
                    return None
        elif len(letters) == 3:
            possibleAlg1 = [key for key in keys if letters[0] in key and len(key) == 3]
            possibleAlg2 = [key for key in keys if letters[1] in key and len(key) == 3]
            possibleAlg3 = [key for key in keys if letters[2] in key and len(key) == 3]
            correctKey = str(
                set(possibleAlg1)
                .intersection(set(possibleAlg2))
                .intersection(set(possibleAlg3))
            )[2:-2]
            if letters[0] == correctKey[0]:
                return algs_from_color[correctKey]
            elif letters[0] == correctKey[1]:
                return (
                    algs_from_color[correctKey][1]
                    + algs_from_color[correctKey][2]
                    + algs_from_color[correctKey][0]
                )
            elif letters[0] == correctKey[2]:
                return (
                    algs_from_color[correctKey][2]
                    + algs_from_color[correctKey][0]
                    + algs_from_color[correctKey][1]
                )
            return None

    def cyclebreak(self):
        # breaks the cycle if the buffer returns to home.
        for _, value in algs_from_color.items():
            if (
                value[0] not in self.solution
                and value[1] not in self.solution
                and not value[0].isupper()
            ) and "buffer" not in self.getalg(value[0]):
                print(value[0], "cycle break")
                self.cube.rotate(self.getalg(value[0]))
                self.solution.append(value[0])

                return True
        return False

    def cyclebreakcorners(self):
        #
        # breaks the cycle if the buffer returns to home.
        for _, value in algs_from_color.items():
            if len(value) == 2:
                continue
            # for every color combination
            if (
                value[0] not in self.solution
                and value[1] not in self.solution
                and value[2] not in self.solution
                and not value[0].islower()
            ) and "buffer" not in self.getalg(
                value[0]
            ):  #
                print(value[0], "cycle break")
                self.cube.rotate(self.getalg(value[0]))
                self.solution.append(value[0])

                return True
        return False

    def solveedges(self):
        for _ in range(16):
            color_str = self.getalgfromcolor(
                self.cube.get_piece((1, 0, 2)).get_piece_colors_str()
            )
            if "buffer" in self.getalg(color_str[0]):
                for edge in [
                    piece
                    for piece in self.cube.get_all_pieces()
                    if len(self.cube.get_piece(piece).get_piece_colors_str()) == 2
                ]:
                    if self.get_home_by_coords(edge) == edge:
                        continue
                bool = self.cyclebreak()
                if not bool:
                    return True
                continue

            # print(self.cube.get_piece((1, 0, 2)))
            # print(color_str[0])
            if color_str[0] == "c" and len(self.solution) % 2:
                self.cube.rotate(self.getalg("w"))
                self.solution.append("w")
            elif color_str[0] == "w" and len(self.solution) % 2:
                self.cube.rotate(self.getalg("c"))
                self.solution.append("c")
            elif color_str[0] == "i" and len(self.solution) % 2:
                self.cube.rotate(self.getalg("s"))
                self.solution.append("s")
            elif color_str[0] == "s" and len(self.solution) % 2:
                self.cube.rotate(self.getalg("i"))
                self.solution.append("i")
            else:
                self.cube.rotate(self.getalg(color_str[0]))
                self.solution.append(color_str[0])

    def solvecorners(self):
        if len(self.solution) % 2 == 1:
            print("parity")
            self.cube.rotate("D' L2 D M2 D' L2 D")
        for _ in range(14):
            color_str = self.getalgfromcolor(  # gets alg from the buffer piece
                self.cube.get_piece((0, 2, 0)).get_piece_colors_str()
            )
            if (
                self.getalg(color_str[0]) in self.solution
            ):  # checks if the move is already done for the solution
                continue
            if "buffer" in self.getalg(
                color_str[0]
            ):  # cycle break if buffer returns to home
                self.cyclebreakcorners()
                continue

            self.cube.rotate(self.getalg(color_str[0]))
            self.solution.append(color_str[0])

    def solve(self) -> str:
        # solves the cube by using a blind method
        self.solveedges()
        self.solvecorners()
        return "".join(self.getalgsbystr(self.solution))
