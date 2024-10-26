import * as R from "./logic/rotations"


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
 * Function that creates a preset cube with the provided preset string
 * @param {*} presetStr a string of length 54 that represents the the colors of the faces of the pieces
 * @returns a custom cube with the provided face colors
 */
export const createCustomCube = (presetStr) => {
    // Validate the input preset string
    if (typeof presetStr !== "string") {
        throw new Error("Invalid input: presetStr should be a string");
    } else if (presetStr.length !== 54) {
        throw new Error("Invalid input: presetStr should be a string of length 54");
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
        { id: 0, x: -1, y: -1, z: -1, faces: { up: "-", down: "51", left: "15", right: "-", front: "-", back: "44" } },
        { id: 1, x: -1, y: -1, z: 0, faces: { up: "-", down: "48", left: "16", right: "-", front: "-", back: "-" } },
        { id: 2, x: -1, y: -1, z: 1, faces: { up: "-", down: "45", left: "17", right: "-", front: "24", back: "-" } },
        { id: 3, x: -1, y: 0, z: -1, faces: { up: "-", down: "-", left: "12", right: "-", front: "-", back: "41" } },
        { id: 4, x: -1, y: 0, z: 0, faces: { up: "-", down: "-", left: "13", right: "-", front: "-", back: "-" } },
        { id: 5, x: -1, y: 0, z: 1, faces: { up: "-", down: "-", left: "14", right: "-", front: "21", back: "-" } },
        { id: 6, x: -1, y: 1, z: -1, faces: { up: "0", down: "-", left: "9", right: "-", front: "-", back: "38" } },
        { id: 7, x: -1, y: 1, z: 0, faces: { up: "3", down: "-", left: "10", right: "-", front: "-", back: "-" } },
        { id: 8, x: -1, y: 1, z: 1, faces: { up: "6", down: "-", left: "11", right: "-", front: "18", back: "-" } },
        { id: 9, x: 0, y: -1, z: -1, faces: { up: "-", down: "52", left: "-", right: "-", front: "-", back: "43" } },
        { id: 10, x: 0, y: -1, z: 0, faces: { up: "-", down: "49", left: "-", right: "-", front: "-", back: "-" } },
        { id: 11, x: 0, y: -1, z: 1, faces: { up: "-", down: "46", left: "-", right: "-", front: "25", back: "-" } },
        { id: 12, x: 0, y: 0, z: -1, faces: { up: "-", down: "-", left: "-", right: "-", front: "-", back: "40" } },
        { id: 14, x: 0, y: 0, z: 1, faces: { up: "-", down: "-", left: "-", right: "-", front: "22", back: "-" } },
        { id: 15, x: 0, y: 1, z: -1, faces: { up: "1", down: "-", left: "-", right: "-", front: "-", back: "37" } },
        { id: 16, x: 0, y: 1, z: 0, faces: { up: "4", down: "-", left: "-", right: "-", front: "-", back: "-" } },
        { id: 17, x: 0, y: 1, z: 1, faces: { up: "7", down: "-", left: "-", right: "-", front: "19", back: "-" } },
        { id: 18, x: 1, y: -1, z: -1, faces: { up: "-", down: "53", left: "-", right: "35", front: "-", back: "42" } },
        { id: 19, x: 1, y: -1, z: 0, faces: { up: "-", down: "50", left: "-", right: "34", front: "-", back: "-" } },
        { id: 20, x: 1, y: -1, z: 1, faces: { up: "-", down: "47", left: "-", right: "33", front: "26", back: "-" } },
        { id: 21, x: 1, y: 0, z: -1, faces: { up: "-", down: "-", left: "-", right: "32", front: "-", back: "39" } },
        { id: 22, x: 1, y: 0, z: 0, faces: { up: "-", down: "-", left: "-", right: "31", front: "-", back: "-" } },
        { id: 23, x: 1, y: 0, z: 1, faces: { up: "-", down: "-", left: "-", right: "30", front: "23", back: "-" } },
        { id: 24, x: 1, y: 1, z: -1, faces: { up: "2", down: "-", left: "-", right: "29", front: "-", back: "36" } },
        { id: 25, x: 1, y: 1, z: 0, faces: { up: "5", down: "-", left: "-", right: "28", front: "-", back: "-" } },
        { id: 26, x: 1, y: 1, z: 1, faces: { up: "8", down: "-", left: "-", right: "27", front: "20", back: "-" } },
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
