/*
 * Copyright (c) 2022.
 *
 * 27/12/22, 10:16, store.ts created by Edoardo.
 */

import {configureStore, ThunkAction, Action} from "@reduxjs/toolkit";
import {boardSlice} from "./boardSlice";
import {createWrapper} from "next-redux-wrapper"

const makeStore = () =>
    configureStore({
        reducer: {
            [boardSlice.name]: boardSlice.reducer
        },
        devTools: true
    });

export type AppStore = ReturnType<typeof makeStore>;
export type AppState = ReturnType<AppStore["getState"]>;
export type AppThunk<ReturnType = void> = ThunkAction<ReturnType, AppState, unknown, Action>;

export const wrapper = createWrapper<AppStore>(makeStore);