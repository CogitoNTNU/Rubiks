from typing import List

import backend.moves.sequence as m
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# cube related imports
from Solvers.alg_solver import *
from magiccube.cube import Cube
import magiccube

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
async def scan_cube(cube_state: str):
    # global cube
    # cube = magiccube.Cube(3, cube_state)
    # return {"cube": cube_state}

    global cube
    cube = Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")
    cube.scramble()

    return {"cube": AlgSolver.get_cube_str(cube)}


class CubeModel(BaseModel):
    cube_str: str

    def __init__(self):
        global cube
        self.cube_str = AlgSolver.get_cube_str(cube)


# load scanned cube state
@app.get("/cube", response_model=CubeModel)
def read_cube() -> CubeModel:
    cube = CubeModel()

    return cube


class Moves(BaseModel):
    moves: list[int]


# Return list of moves to solve cube
@app.get("/moves", response_model=Moves)
def solve_cube() -> Moves:
    global cube
    solver = AlgSolver(cube)
    solution = solver.solve()
    moves = Moves(moves=m.get_mapped_sequence("R U R' U'"))

    # moves = Moves(moves=m.get_mapped_sequence(solution))

    return {"moves": moves}
