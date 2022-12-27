/*
 * Copyright (c) 2022.
 *
 * 27/12/22, 18:04, sessionSlice.ts created by Edoardo.
 */

import {createSlice} from "@reduxjs/toolkit"
import {AppState} from "./store";

export interface SessionState {

    airTemperature?: number,
    trackTemperature?: number,
    trackLength?: number,
    trackId?: number,
    trackName?: string,
    sessionType?: number,
    sessionTypeName?: string,
    timeLeftInSeconds?: number,
    timeLeftFormatted?: string,
    weather?: number
}


const initialState: SessionState = {

};

export const sessionSlice = createSlice({
    name: "session",
    initialState,
    reducers: {
        setSessionState(state, action) {
            return action.payload
        }
    }
});

export const { setSessionState } = sessionSlice.actions;
export const selectSessionState = (state: AppState) => state.session;
export default sessionSlice.reducer;