from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# scan cube state
@app.get("/scan")
def scan_cube():
    return {"scan": "scan"}


# load scanned cube state
@app.get("/cube")
def read_cube():
    return {"cube": "cube"}


# Return list of moves to solve cube
@app.get("/moves")
def solve_cube():
    return {"moves": "moves"}
