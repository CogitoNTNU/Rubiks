# Rubiks Cube Solver

<div align="center">

![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/CogitoNTNU/Rubiks/actions/workflows/ci.yml)
![GitHub top language](https://img.shields.io/github/languages/top/CogitoNTNU/Rubiks)
![GitHub language count](https://img.shields.io/github/languages/count/CogitoNTNU/Rubiks)
[![Project Version](https://img.shields.io/badge/version-1.0.0-blue)](https://img.shields.io/badge/version-1.0.0-blue)

</div>

## Description

![Rubiks Cube](docs/images/rubiks.gif)

This project aims to solve a Rubik's cube through different methods. A fully functioning web frontend for visualization of the cube state and the solution process (stripped down and modified version of [taylorjg/rubiks-cube](https://github.com/taylorjg/rubiks-cube) <3). A corresponding Fast API backend that provides required data to the frontend.

### Blind method

Using the 3 algorithms solves the cube piece by pice. Used as a baseline.

### A-star

Using A* search though the extremely large state space of all possible rubik's cubes. This is split up in stages to limit possible states to look through (all set up in main.py):

1. Scrambled to Edge Orientation (EO)
2. EO to Domino Reduction (DR)
3. DR to Solved

We later found out we had some wrong domain assumptions because of which stage 2 never finishes, but by splitting them up in stages we drastically reduce the search space and which makes this promising. More tweaks and work needed.

## How to run and install

To simply test out the project a docker compose file has been provided. Run it with:

```bash
docker compose up -d --build
```

And open at ```localhost:3000``` which will generate a random scramble and proceed to solve it with the Blind method.

If you wish to work on the project clone the repo. For the backend and logic you will need to set up [Poetry](https://python-poetry.org/), follow the [environment.md](docs/manuals/environment.md) for further guidance. The different helping objects and functions used to solve the cube are found in ```backend/Solvers```. Fast API is set up in ```backend/api.py```. [Magicube](https://pypi.org/project/magiccube/) package is widelly used so might be a good idea to get familiar with it.

For the frontend its a bit of a mess. Most things happen in ```frontend/src/three-app.js``` with additional logic we separated located in ```frontend/src/customCube.js```

Dependencies are installed with:

```bash
npm i
```

And run the frontend from the /frontend folder with:

```bash
npm start
```

## Team

The team behind this project is a group of seven students at NTNU Trondheim from various study backgrounds. All a members of Cogito NTNU fall 2024.

<table align="center">
    <tr>
        <td align="center">
                <a href="https://github.com/Eduard-Prokhorikhin">
                        <img src="https://github.com/Eduard-Prokhorikhin.png?size=100" width="100px;" alt="Eduard-Prokhorikhin"/><br />
                        <sub><b>Eduard Prokhorikhin</b></sub>
                </a>
        </td>
        <td align="center">
                <a href="https://github.com/1rideee">
                        <img src="https://github.com/1rideee.png?size=100" width="100px;" alt="1rideee"/><br />
                        <sub><b>Einride Osland</b></sub>
                </a>
        </td>
        <td align="center">
                <a href="https://github.com/Baykugan">
                        <img src="https://github.com/Baykugan.png?size=100" width="100px;" alt="Baykugan"/><br />
                        <sub><b>Even Ytterli Tokle</b></sub>
                </a>
        </td>
        <td align="center">
                <a href="https://github.com/GustavNat">
                        <img src="https://github.com/GustavNat.png?size=100" width="100px;" alt="GustavNat"/><br />
                        <sub><b>Gustav Natvig</b></sub>
                </a>
        </td>
        <td align="center">
                <a href="https://github.com/kienple">
                        <img src="https://github.com/kienple.png?size=100" width="100px;" alt="kienple"/><br />
                        <sub><b>Kien Le</b></sub>
                </a>
        </td>
        <td align="center">
                <a href="https://github.com/Vetlebrur">
                        <img src="https://github.com/Vetlebrur.png?size=100" width="100px;" alt="Vetlebrur"/><br />
                        <sub><b>Vetle</b></sub>
                </a>
        </td>
        <td align="center">
                <a href="https://github.com/Viljen789">
                        <img src="https://github.com/Viljen789.png?size=100" width="100px;" alt="Viljen789"/><br />
                        <sub><b>Viljen789</b></sub>
                </a>
        </td>
    </tr>
</table>
