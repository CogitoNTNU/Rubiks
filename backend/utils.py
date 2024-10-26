from magiccube import Cube
from magiccube.cube import Face


def get_cube_str(cube: Cube) -> str:
    faces = [
        cube.get_face(Face.U),
        cube.get_face(Face.L),
        cube.get_face(Face.F),
        cube.get_face(Face.R),
        cube.get_face(Face.B),
        cube.get_face(Face.D),
    ]
    result = "".join(
        "".join("".join(str(color) for color in row) for row in face) for face in faces
    )
    ans = [result[x] for x in range(6, len(result), 7)]
    ans = "".join(ans)
    return ans
