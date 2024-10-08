import * as R from "./logic/rotations"


export var currentCube = [];

const allWhitePreset = [
    { id: 0, x: -1, y: -1, z: -1, faces: { up: "-", down: "B", left: "B", right: "-", front: "-", back: "B" } },
    { id: 1, x: -1, y: -1, z: 0, faces: { up: "-", down: "B", left: "B", right: "-", front: "-", back: "-" } },
    { id: 2, x: -1, y: -1, z: 1, faces: { up: "-", down: "B", left: "B", right: "-", front: "B", back: "-" } },
    { id: 3, x: -1, y: 0, z: -1, faces: { up: "-", down: "-", left: "B", right: "-", front: "-", back: "B" } },
    { id: 4, x: -1, y: 0, z: 0, faces: { up: "-", down: "-", left: "B", right: "-", front: "-", back: "-" } },
    { id: 5, x: -1, y: 0, z: 1, faces: { up: "-", down: "-", left: "B", right: "-", front: "B", back: "-" } },
    { id: 6, x: -1, y: 1, z: -1, faces: { up: "B", down: "-", left: "B", right: "-", front: "-", back: "B" } },
    { id: 7, x: -1, y: 1, z: 0, faces: { up: "B", down: "-", left: "B", right: "-", front: "-", back: "-" } },
    { id: 8, x: -1, y: 1, z: 1, faces: { up: "B", down: "-", left: "B", right: "-", front: "B", back: "-" } },
    { id: 9, x: 0, y: -1, z: -1, faces: { up: "-", down: "B", left: "-", right: "-", front: "-", back: "B" } },
    { id: 10, x: 0, y: -1, z: 0, faces: { up: "-", down: "B", left: "-", right: "-", front: "-", back: "-" } },
    { id: 11, x: 0, y: -1, z: 1, faces: { up: "-", down: "B", left: "-", right: "-", front: "B", back: "-" } },
    { id: 12, x: 0, y: 0, z: -1, faces: { up: "-", down: "-", left: "-", right: "-", front: "-", back: "B" } },
    { id: 14, x: 0, y: 0, z: 1, faces: { up: "-", down: "-", left: "-", right: "-", front: "B", back: "-" } },
    { id: 15, x: 0, y: 1, z: -1, faces: { up: "B", down: "-", left: "-", right: "-", front: "-", back: "B" } },
    { id: 16, x: 0, y: 1, z: 0, faces: { up: "B", down: "-", left: "-", right: "-", front: "-", back: "-" } },
    { id: 17, x: 0, y: 1, z: 1, faces: { up: "B", down: "-", left: "-", right: "-", front: "B", back: "-" } },
    { id: 18, x: 1, y: -1, z: -1, faces: { up: "-", down: "B", left: "-", right: "B", front: "-", back: "B" } },
    { id: 19, x: 1, y: -1, z: 0, faces: { up: "-", down: "B", left: "-", right: "B", front: "-", back: "-" } },
    { id: 20, x: 1, y: -1, z: 1, faces: { up: "-", down: "B", left: "-", right: "B", front: "B", back: "-" } },
    { id: 21, x: 1, y: 0, z: -1, faces: { up: "-", down: "-", left: "-", right: "B", front: "-", back: "B" } },
    { id: 22, x: 1, y: 0, z: 0, faces: { up: "-", down: "-", left: "-", right: "B", front: "-", back: "-" } },
    { id: 23, x: 1, y: 0, z: 1, faces: { up: "-", down: "-", left: "-", right: "B", front: "B", back: "-" } },
    { id: 24, x: 1, y: 1, z: -1, faces: { up: "B", down: "-", left: "-", right: "B", front: "-", back: "B" } },
    { id: 25, x: 1, y: 1, z: 0, faces: { up: "B", down: "-", left: "-", right: "B", front: "-", back: "-" } },
    { id: 26, x: 1, y: 1, z: 1, faces: { up: "B", down: "-", left: "-", right: "B", front: "B", back: "-" } },
]

export const presets = {
    allWhite: allWhitePreset,
};

export const makeCustomCube = (pieces) => {
    // Validate the input pieces
    if (!Array.isArray(pieces)) {
        throw new Error("Invalid input: pieces should be an array");
    }

    // Create the cube with the provided pieces
    const cube = pieces.map((piece, index) => ({
        id: index,
        x: piece.x,
        y: piece.y,
        z: piece.z,
        faces: piece.faces,
        accTransform3: piece.accTransform3 || R.Identity,
    }));

    return cube;
};

export const setCustomPreset = (cubePreset) => {
    currentCube = makeCustomCube(cubePreset);
};
