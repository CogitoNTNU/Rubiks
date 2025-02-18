from typing import List

import magiccube
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from magiccube.cube import Cube
from pydantic import BaseModel

# cube related imports
import backend.moves.sequence as m
from backend.Solvers.alg_solver import *
from backend.utils import get_cube_str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# defining cube related values
cube = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


# scan cube state
@app.post("/scan")
async def scan_cube():
    # global cube
    # cube = magiccube.Cube(3, cube_state)
    # return {"cube": cube_state}

    global cube
    cube = Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")
    cube.scramble()
    return {"cube": get_cube_str(cube)}


class CubeModel(BaseModel):
    cube_str: str


# load scanned cube state
@app.get("/cube", response_model=CubeModel)
def read_cube() -> CubeModel:
    return CubeModel(cube_str=get_cube_str(cube))


class Moves(BaseModel):
    moves: list[int]


# Return list of moves to solve cube
@app.get("/moves", response_model=Moves)
def solve_cube() -> Moves:
    global cube
    if cube == None:
        cube = Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")
        cube.scramble()

    solver = AlgSolver(cube)
    solution = solver.solve()

    moves = Moves(moves=m.get_mapped_sequence(solution))
    return moves
