import Head from 'next/head'
import Image from 'next/image'
import { Inter } from '@next/font/google'
import styles from '../styles/Home.module.css'
import io from "socket.io-client";
import {useDispatch, useSelector} from "react-redux";
import {selectBoardState, setBoardState} from "../store/boardSlice";
import BoardComponent from "./components/BoardComponent";

const inter = Inter({ subsets: ['latin'] });

let socket = io("localhost:3001", {transports: ["websocket"]})

export default function Home() {

    const boardState = useSelector(selectBoardState);
    const dispatch = useDispatch();

    socket.on("send_board", (data) => {
        dispatch(setBoardState(data));
    });

    return (
        <>
            <Head>
                <title>F1 2022 - Live Game Dashboard</title>
                <meta name="description" content="Generated by create next app" />
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <link rel="icon" href="/favicon.ico" />
            </Head>
            {boardState.length <= 0 &&
                <div className={[styles.main].join(" ")}>
                    <div className={[styles.spin].join(" ")}></div>
                    <div className={[styles.loadingText].join(" ")}>
                        Loading dashboard data...
                    </div>
                </div>
            }

            {boardState.length > 0 &&
                <>
                    <BoardComponent boardState={boardState}/>
                </>
            }
        </>
    )
}