import magiccube
from magiccube.cube import Cube
from magiccube.cube_base import Face


class Domino_solver:

    def __init__(self, cube: Cube) -> None:
        self.cube = cube
        self.copy = Cube(3, self.get_unformated_string())
        self.value = 0
        self.edges = [
            (0, 0, 1),
            (0, 1, 0),
            (0, 1, 2),
            (0, 2, 1),
            (1, 0, 0),
            (1, 0, 2),
            (1, 2, 0),
            (1, 2, 2),
            (2, 0, 1),
            (2, 1, 0),
            (2, 1, 2),
            (2, 2, 1),
        ]

    def get_unformated_string(self):
        cube = self.cube
        faces = [
            cube.get_face(Face.U),
            cube.get_face(Face.L),
            cube.get_face(Face.F),
            cube.get_face(Face.R),
            cube.get_face(Face.B),
            cube.get_face(Face.D),
        ]
        result = "".join(
            "".join("".join(str(color) for color in row) for row in face)
            for face in faces
        )
        ans = [result[x] for x in range(6, len(result), 7)]
        ans = "".join(ans)
        return ans  # Returnerer kver blokk på samme format som når man initialiserer ei kube

    def get_face_by_center(self, face: str):
        new_face = self.cube.get_face(Face[face])
        ans = "".join("".join(str(color) for color in row) for row in new_face)
        ans = "".join([ans[x] for x in range(6, len(ans), 7)])
        return ans

    def color_edge_count_on_face(self, color: str = "Y", face: str = "L"):
        f = self.get_face_by_center(face)
        return sum([1 for x in range(1, 9, 2) if f[x] == color])

    def color_corner_count_on_face(self, color: str = "Y", face: str = "L"):
        f = self.get_face_by_center(face)
        return sum([1 for x in range(0, 9, 2) if f[x] == color and x != 4])

    def get_color_by_coords(self, coords):
        return self.cube.get_piece(coords).get_piece_colors_str()

    def get_key_sticker(self, edge: str, rotated):
        '''
        Kan sjekke index edge[unrotated] (Når rotert vil vi bruke index 1, viss ikkje index 0)
        unRotatedGreen = "G", unRotatedBlue = "B"
        rotatedOrange = "O", rotatedRed = "R"'''
        
        if "W" in edge:
            return "W"
        elif "Y" in edge:
            return "Y"
        elif ("B" in edge) and (not rotated):
            return "B"
        elif ("G" in edge) and (not rotated):
            return "G"
        elif ("O" in edge) and (rotated):
            return "O"
        elif ("R" in edge) and (rotated):
            return "R"

    def check_all_edges(self, rotated: bool):
        tot = 0
        for i in range(0, 12):
            cur = self.edges[i]
            col = self.get_color_by_coords(cur)
            key = self.get_key_sticker(col, rotated)
            if not rotated:
                if cur[0] == 1 and col[0] == key:
                    tot += 1
                elif cur[0] != 1 and col[1] == key:
                    tot += 1
            else:
                if cur[2] == 1 and col[1] == key:
                    tot += 1
                elif cur[2] != 1 and col[0] == key:
                    tot += 1
        return tot
