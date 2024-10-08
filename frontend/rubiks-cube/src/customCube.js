import * as R from "./logic/rotations"


export var currentCube = [];

/**
 * Function that creates a custom cube with the provided pieces
 * @param {*} pieces an array of object literal pieces that make up the cube
 * @returns a custom cube with the provided pieces
 */
const makeCustomCube = (pieces) => {
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

/**
 * Function that sets the current cube to a custom cube
 * @param {*} cube a custom cube
 * @returns None
git */
export const setCustomcCube = (cube) => {
    currentCube = cube;
};

/**
 * Function that creates a preset cube with the provided preset string
 * @param {*} presetStr a string of length 54 that represents the the colors of the faces of the pieces
 * @returns a custom cube with the provided face colors
 */
export const createCustomCube = (presetStr) => {
    // Validate the input preset string
    if (typeof presetStr !== "string") {
        throw new Error("Invalid input: presetStr should be a string");
    } else if (presetStr.length !== 54) {
        throw new Error("Invalid input: presetStr should be a string of length 72");
    }

    // Modify the preset string to work with the current colornames
    const modifiedStr = presetStr.replace(/[YROGBW]/g, match => ({
        Y: "F",
        R: "L",
        O: "R",
        G: "D",
        B: "U",
        W: "B"
    }[match]));

    // Create the preset template
    var preset = [
        { id: 0, x: -1, y: -1, z: -1, faces: { up: "-", down: "18", left: "27", right: "-", front: "-", back: "0" } },
        { id: 1, x: -1, y: -1, z: 0, faces: { up: "-", down: "19", left: "28", right: "-", front: "-", back: "-" } },
        { id: 2, x: -1, y: -1, z: 1, faces: { up: "-", down: "20", left: "29", right: "-", front: "45", back: "-" } },
        { id: 3, x: -1, y: 0, z: -1, faces: { up: "-", down: "-", left: "30", right: "-", front: "-", back: "1" } },
        { id: 4, x: -1, y: 0, z: 0, faces: { up: "-", down: "-", left: "31", right: "-", front: "-", back: "-" } },
        { id: 5, x: -1, y: 0, z: 1, faces: { up: "-", down: "-", left: "32", right: "-", front: "45", back: "-" } },
        { id: 6, x: -1, y: 1, z: -1, faces: { up: "36", down: "-", left: "33", right: "-", front: "-", back: "2" } },
        { id: 7, x: -1, y: 1, z: 0, faces: { up: "37", down: "-", left: "34", right: "-", front: "-", back: "-" } },
        { id: 8, x: -1, y: 1, z: 1, faces: { up: "38", down: "-", left: "35", right: "-", front: "47", back: "-" } },
        { id: 9, x: 0, y: -1, z: -1, faces: { up: "-", down: "21", left: "-", right: "-", front: "-", back: "3" } },
        { id: 10, x: 0, y: -1, z: 0, faces: { up: "-", down: "22", left: "-", right: "-", front: "-", back: "-" } },
        { id: 11, x: 0, y: -1, z: 1, faces: { up: "-", down: "23", left: "-", right: "-", front: "48", back: "-" } },
        { id: 12, x: 0, y: 0, z: -1, faces: { up: "-", down: "-", left: "-", right: "-", front: "-", back: "4" } },
        { id: 14, x: 0, y: 0, z: 1, faces: { up: "-", down: "-", left: "-", right: "-", front: "49", back: "-" } },
        { id: 15, x: 0, y: 1, z: -1, faces: { up: "39", down: "-", left: "-", right: "-", front: "-", back: "5" } },
        { id: 16, x: 0, y: 1, z: 0, faces: { up: "40", down: "-", left: "-", right: "-", front: "-", back: "-" } },
        { id: 17, x: 0, y: 1, z: 1, faces: { up: "41", down: "-", left: "-", right: "-", front: "50", back: "-" } },
        { id: 18, x: 1, y: -1, z: -1, faces: { up: "-", down: "24", left: "-", right: "9", front: "-", back: "6" } },
        { id: 19, x: 1, y: -1, z: 0, faces: { up: "-", down: "25", left: "-", right: "10", front: "-", back: "-" } },
        { id: 20, x: 1, y: -1, z: 1, faces: { up: "-", down: "26", left: "-", right: "11", front: "51", back: "-" } },
        { id: 21, x: 1, y: 0, z: -1, faces: { up: "-", down: "-", left: "-", right: "12", front: "-", back: "7" } },
        { id: 22, x: 1, y: 0, z: 0, faces: { up: "-", down: "-", left: "-", right: "13", front: "-", back: "-" } },
        { id: 23, x: 1, y: 0, z: 1, faces: { up: "-", down: "-", left: "-", right: "14", front: "52", back: "-" } },
        { id: 24, x: 1, y: 1, z: -1, faces: { up: "42", down: "-", left: "-", right: "15", front: "-", back: "8" } },
        { id: 25, x: 1, y: 1, z: 0, faces: { up: "43", down: "-", left: "-", right: "16", front: "-", back: "-" } },
        { id: 26, x: 1, y: 1, z: 1, faces: { up: "44", down: "-", left: "-", right: "17", front: "53", back: "-" } },
    ];

    // Fill in the preset template with the modified preset string
    preset.forEach(piece => {
        for (let face in piece.faces) {
            let faceValue = piece.faces[face];
            if (faceValue !== "-") { // Check if the face value is a number and not a dash
                let charIndex = parseInt(faceValue);
                piece.faces[face] = modifiedStr[charIndex]; // Replace with corresponding character
            }
        }
    });

    return makeCustomCube(preset);
}

export const customCubes = {
    allWhite: createCustomCube("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"),
    allBlue: createCustomCube("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"),
    allGreen: createCustomCube("GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"),
    allRed: createCustomCube("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"),
    allOrange: createCustomCube("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"),
    allYellow: createCustomCube("YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"),
    normal: createCustomCube("WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY"),
};
