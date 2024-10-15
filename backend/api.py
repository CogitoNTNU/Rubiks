from typing import List

import moves.sequence as m
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


# scan cube state
@app.get("/scan")
def scan_cube():
    return {"scan": "scan"}

class Cube(BaseModel):
    cube: str

# load scanned cube state
@app.get("/cube", response_model=Cube)
def read_cube() -> Cube:
    return Cube(cube="WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")


class Moves(BaseModel):
    moves: list[int]

# Return list of moves to solve cube
@app.get("/moves", response_model=Moves)
def solve_cube() -> Moves:
    return Moves(moves=m.get_mapped_sequence("R U R' U'"))
