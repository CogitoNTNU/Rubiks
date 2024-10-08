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
    "V": " ",
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
    "WGO": "DIF",
    "YOB": "XHS",
    "YBR": "WTO",
    "YRG": "VPK",
    "YGO": "ULG",
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
        # Finds where a piece from a coordinate belongs based on its coords
        return self.unscrambled.find_piece(str(self.cube.get_piece(coords)))[0]

    def get_color_by_coords(self, coords):
        return self.cube.get_piece(coords).get_piece_colors_str()

    def get_home_by_name(self, piece: str):
        # Finds where a piece from a coordinate belongs based on its name
        return self.unscrambled.find_piece(piece)[0]

    def get_unformated_string(self) -> str:
        # gets a unformated string of the cube
        pass

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

    def getalgsbystr(self, letters):
        # gets the algorithm for a list of letters
        algs = ""
        for letter in letters:
            algs += self.getalg(letter) + " "
        return algs

    def getalgfromcolor(self, letters):
        keys = algs_from_color.keys()
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
            if letters in keys:
                return algs_from_color[letters]
            if letters[0] + letters[2] + letters[1] in keys:
                return (
                    algs_from_color[letters[0] + letters[2] + letters[1]][0]
                    + algs_from_color[letters[0] + letters[2] + letters[1]][2]
                    + algs_from_color[letters[0] + letters[2] + letters[1]][1]
                )
            if letters[1] + letters[0] + letters[2] in keys:
                return (
                    algs_from_color[letters[1] + letters[0] + letters[2]][1]
                    + algs_from_color[letters[1] + letters[0] + letters[2]][0]
                    + algs_from_color[letters[1] + letters[0] + letters[2]][2]
                )
            if letters[1] + letters[2] + letters[0] in keys:
                return (
                    algs_from_color[letters[1] + letters[2] + letters[0]][1]
                    + algs_from_color[letters[1] + letters[2] + letters[0]][2]
                    + algs_from_color[letters[1] + letters[2] + letters[0]][0]
                )
            if letters[2] + letters[0] + letters[1] in keys:
                return (
                    algs_from_color[letters[2] + letters[0] + letters[1]][2]
                    + algs_from_color[letters[2] + letters[0] + letters[1]][0]
                    + algs_from_color[letters[2] + letters[0] + letters[1]][1]
                )
            if letters[2] + letters[1] + letters[0] in keys:
                return (
                    algs_from_color[letters[2] + letters[1] + letters[0]][2]
                    + algs_from_color[letters[2] + letters[1] + letters[0]][1]
                    + algs_from_color[letters[2] + letters[1] + letters[0]][0]
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

            print(self.cube.get_piece((1, 0, 2)))
            print(color_str[0])
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
        for _ in range(12):
            color_str = self.getalgfromcolor(
                self.cube.get_piece((0, 2, 0)).get_piece_colors_str()
            )
            # print(self.cube.get_piece((0, 2, 0)).get_piece_colors_str())
            print(color_str)
            if (
                self.getalg(color_str[0]) in self.solution
                or self.getalg(color_str[1]) in self.solution
                or self.getalg(color_str[2]) in self.solution
            ):
                print("Already in solution")
                break
            if "buffer" in self.getalg(color_str[0]):
                if not bool:
                    return True
                self.cyclebreak()
                continue
            print(color_str[0], "Alg to perform", self.getalg(color_str[0]))
            self.cube.rotate(self.getalg(color_str[0]))
            self.solution.append(color_str[0])

        print(self.cube)

    def solve(self) -> str:
        # TODO: put everything together
        return ""


# ________________________________________________________________________________________
if __name__ == "__main__":
    c = magiccube.Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

    solver = AlgSolver(c)
    solver.solve()
    # print("DB")

"""Stdout Cube Print implementation"""
import os
from enum import Enum
from magiccube.cube_base import Color, Face

C_RESET = "\x1b[0;0m"
# C_BG="\x1b[48;5;231m"


class Terminal(Enum):
    default = 0
    x256 = 1


class CubePrintStr:
    """Prints a cube to stdout"""

    _xterm256_color_map = {
        Color.G: "\x1b[48;5;40m\x1b[38;5;232m",
        Color.B: "\x1b[48;5;21m\x1b[38;5;7m",
        Color.R: "\x1b[48;5;196m\x1b[38;5;232m",
        Color.O: "\x1b[48;5;208m\x1b[38;5;232m",
        Color.Y: "\x1b[48;5;226m\x1b[38;5;232m",
        Color.W: "\x1b[48;5;248m\x1b[38;5;232m",
    }

    def __init__(self, cube):
        self.cube = cube
        self.term = (
            Terminal.x256
            if os.environ.get("TERM") == "xterm-256color"
            else Terminal.default
        )

    def _format_color(self, color: Color):
        """Format color to TTY
        Only print colors on supported terminals (xterm-256color)
        """
        formated_color = " " + color.name + " "

        if self.term == Terminal.x256:
            formated_color = (
                CubePrintStr._xterm256_color_map.get(color, "")
                + formated_color
                + C_RESET
            )

        return formated_color

    def _print_top_down_face(self, cube, face):
        result = ""
        for index, color in enumerate(cube.get_face_flat(face)):
            if index % cube.size == 0:
                result += " " * ((3 * cube.size))

            result += self._format_color(color)

            if index % cube.size == cube.size - 1:
                result += " " * ((2 * 3 * cube.size))
                result += "\n"
        return result

    def print_cube(self):
        "Print the cube to stdout"
        cube = self.cube

        # flatten midle layer
        print_order_mid = zip(
            cube.get_face(Face.L),
            cube.get_face(Face.F),
            cube.get_face(Face.R),
            cube.get_face(Face.B),
        )

        # TOP
        result = self._print_top_down_face(cube, Face.U)
        # MID
        for line in print_order_mid:
            for line_index, face_line in enumerate(line):
                for face_line_index, color in enumerate(face_line):
                    result += self._format_color(color)

                    if face_line_index % cube.size == cube.size - 1:
                        result += ""

        # BOTTOM
        result += self._print_top_down_face(cube, Face.D)
        return result
