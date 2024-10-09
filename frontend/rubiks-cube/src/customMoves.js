import * as L from "./logic"

import { globals } from "./three-app"


export const getMoves = (moves) => {
    // Validate the input 
    if (!Array.isArray(moves)) {
        throw new Error("Invalid input: moves should be an array")
    }

    const perCubeSizeData = L.PER_CUBE_SIZE_DATA.get(globals.cubeSize)
    // const moves = moveStr.split(" ")
    const moveList = moves.map(move => {
        return perCubeSizeData.moves[move]
    })
    return moveList
}
