/*
 * Copyright (c) 2022.
 *
 * 27/12/22, 10:37, BoardComponent.tsx created by Edoardo.
 */

import homeStyles from '../../styles/Home.module.css'
import {BoardState, DriverData} from "../../store/boardSlice";
import boardComponentStyles from '../../styles/BoardComponent.module.css';
import {TEAMSLOGOS} from "../../constants/teamsLogos";
import {TYRES} from "../../constants/tyres";

export default function BoardComponent(props: BoardState) {
    return(
        <section className={[homeStyles.screen].join(" ")}>
            <div className={[homeStyles.generalBox, boardComponentStyles.pilots].join(" ")}>
                <span>Drivers board</span>
                <table className={[boardComponentStyles.pilotsTable].join(" ")}>
                    <thead>
                    <tr>
                        <th>#</th>
                        <th>Team</th>
                        <th>Driver</th>
                        <th>Sector 1</th>
                        <th>Sector 2</th>
                        <th>Sector 3</th>
                        <th>Best lap</th>
                        <th>Tyres</th>
                    </tr>
                    </thead>
                    <tbody>
                    {props.boardState.map((value, index) => {
                        return(<tr key={index}>
                            <td>{index + 1}</td>
                            <td>
                                <div className={[boardComponentStyles.teamImage].join(" ")} style={{
                                    backgroundImage: `url('${TEAMSLOGOS[value[1].teamName].src}')`,
                                    width: 30,
                                    height: 30,
                                    backgroundSize: "contain !important",
                                    backgroundRepeat:"no-repeat !important"}} />
                            </td>
                            <td>
                                {value[1].name}
                            </td>
                            <td style={{color: value[1].isBestSector1 ? "purple" : "white"}}>{value[1].sector1 != -1 ? value[1].sector1Formatted : "00:000"}</td>
                            <td style={{color: value[1].isBestSector2 ? "purple" : "white"}}>{value[1].sector2 != -1 ? value[1].sector2Formatted : "00:000"}</td>
                            <td style={{color: value[1].isBestSector3 ? "purple" : "white"}}>{value[1].sector3 != -1 ? value[1].sector3Formatted : "00:000"}</td>
                            <td style={{color: index == 0 && value[1].bestLapTimeInMS != -1 ? "purple" : "white"}}>{value[1].bestLapTimeInMS != -1 ? value[1].bestLapTimeFormatted : "00:00:000"}</td>
                            <td style={{display: "flex", justifyContent: "center"}}>
                                {value[1].tyreCompound != -1 &&
                                    <div className={[boardComponentStyles.tyre].join(" ")}>
                                        <div
                                            style={{borderColor: TYRES[value[1].tyreCompound][0]}}
                                            className={[boardComponentStyles.leftHalf].join(" ")}></div>
                                        <div
                                            style={{borderColor: TYRES[value[1].tyreCompound][0]}}
                                            className={[boardComponentStyles.rightHalf].join(" ")}></div>
                                        <b style={{color: "white", fontWeight: "bold"}}>{TYRES[value[1].tyreCompound][1]}</b>
                                    </div>
                                }
                            </td>
                        </tr>)
                    })}
                    </tbody>
                </table>

            </div>
        </section>
    )
}