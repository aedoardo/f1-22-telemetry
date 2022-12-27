/*
 * Copyright (c) 2022.
 *
 * 27/12/22, 17:54, SessionComponent.tsx created by Edoardo.
*/

import sessionComponentStyles from '../../styles/SessionComponent.module.css';
import {SessionState} from "../../store/sessionSlice";
import {WEATHER} from "../../constants/weather";

interface SessionProps {
    data: SessionState
}

export default function SessionComponent(props: SessionProps) {
    return(
        <div className={[sessionComponentStyles.info].join(" ")}>
            <div className={[sessionComponentStyles.sessionName].join(" ")}>
                <span>🏁 {props.data.sessionTypeName}</span>
                <span style={{marginLeft: 10}}>
                    {props.data.timeLeftFormatted}
                </span>
            </div>
            <div className={[sessionComponentStyles.sessionName].join(" ")}>
               🛣️ {props.data.trackName}
            </div>
            <div className={[sessionComponentStyles.sessionName].join(" ")}>
                🌡️ Air: {props.data.airTemperature}°
            </div>
            <div className={[sessionComponentStyles.sessionName].join(" ")}>
                🌡️ Track: {props.data.trackTemperature}°
            </div>
            <div className={[sessionComponentStyles.sessionName].join(" ")}>
                {WEATHER[props.data.weather != undefined ? props.data.weather : 0]} Current weather
            </div>
        </div>
    )
}
