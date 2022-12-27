/*
 * Copyright (c) 2022.
 *
 * 27/12/22, 16:14, teamsLogos.ts created by Edoardo.
 */

import mercedes from '../images/teams/mercedes.jpg'
import ferrari from '../images/teams/ferrari.jpg'
import alfaRomeo from '../images/teams/alfa-romeo.jpg'
import alphaTauri from '../images/teams/alpha-tauri.jpg'
import alpine from '../images/teams/alpine.jpg'
import astonMartin from '../images/teams/aston-martin.jpg'
import haas from '../images/teams/haas.jpg'
import mclaren from '../images/teams/mclaren.jpg'
import redbull from '../images/teams/redbull.jpg'
import williams from '../images/teams/williams.jpg'
import {StaticImageData} from "next/image";

export const TEAMSLOGOS: {[key: string]: StaticImageData} = {
    "Mercedes": mercedes,
    "Ferrari": ferrari,
    "Red Bull Racing": redbull,
    "Williams": williams,
    "McLaren": mclaren,
    "Alfa Romeo": alfaRomeo,
    "Aston Martin": astonMartin,
    "Haas": haas,
    "Alpha Tauri": alphaTauri,
    "Alpine": alpine
};
