/*
 * Copyright (c) 2022.
 *
 * 27/12/22, 10:03, boardSlice.ts created by Edoardo.
 */

import {createSlice} from "@reduxjs/toolkit"
import {AppState} from "./store";

export interface DriverData {
    bestLapTimeInMS: number,
    name: string,
    sector1: number,
    sector2: number,
    sector3: number,
    team: number,
    teamName: string,
    bestLapTimeFormatted: string,
    sector1Formatted: string,
    sector2Formatted: string,
    sector3Formatted: string,
    isBestSector1: boolean,
    isBestSector2: boolean,
    isBestSector3: boolean
}

export interface BoardState {
    boardState: [[number, DriverData]] | []
}

const initialState: BoardState = {
    boardState: []
};

export const boardSlice = createSlice({
    name: "board",
    initialState,
    reducers: {
        setBoardState(state, action) {
            state.boardState = action.payload
        }
    }
});

export const { setBoardState } = boardSlice.actions;
export const selectBoardState = (state: AppState) => state.board.boardState;
export default boardSlice.reducer;