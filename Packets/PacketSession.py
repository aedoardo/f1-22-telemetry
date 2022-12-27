#  Copyright (c) 2022.
#
#  27/12/22, 17:14, PacketSession.py created by Edoardo.

from ctypes import *
from typing import List

from Packets.PacketHeader import PacketHeader


class MarshalZone(LittleEndianStructure):

    def __init__(self) -> None:
        self.m_zoneStart: float = None
        self.m_zoneFlag: int = None

    _pack_ = 1
    _fields_ = [
        ("m_zoneStart", c_float),
        ("m_zoneFlag", c_uint8)
    ]


class WeatherForecastSample(LittleEndianStructure):

    def __init__(self) -> None:
        self.m_sessionType: int = None  # 0 = unknown, 1 = P1, 2 = P2, 3 = P3, 4 = Short P, 5 = Q1, 6 = Q2, 7 = Q3,
        # 8 = Short Q, 9 = OSQ, 10 = R, 11 = R2, 12 = R3, 13 = Time Trial
        self.m_timeOffset: int = None
        self.m_weather: int = None  # 0 = clear, 1 = light cloud, 2 = overcast,3 = light rain, 4 = heavy rain, 5 = storm
        self.m_trackTemperature: int = None
        self.m_trackTemperatureChange: int = None
        self.m_airTemperature: int = None
        self.m_airTemperatureChange: int = None
        self.m_rainPercentage: int = None

    _pack_ = 1
    _fields_ = [
        ("m_sessionType", c_uint8),
        ("m_timeOffset", c_uint8),
        ("m_weather", c_uint8),
        ("m_trackTemperature", c_int8),
        ("m_trackTemperatureChange", c_int8),
        ("m_airTemperature", c_int8),
        ("m_airTemperatureChange", c_int8),
        ("m_rainPercentage", c_uint8)
    ]


class PacketSession(LittleEndianStructure):

    def __init__(self):
        self.m_header: PacketHeader = None
        self.m_weather: int = None
        self.m_trackTemperature: int = None
        self.m_airTemperature: int = None
        self.m_totalLaps: int = None
        self.m_trackLength: int = None
        self.m_sessionType: int = None
        self.m_trackId: int = None
        self.m_formula: int = None
        self.m_sessionTimeLeft: int = None
        self.m_sessionDuration: int = None
        self.m_pitSpeedLimit: int = None
        self.m_gamePaused: int = None
        self.m_isSpectating: int = None
        self.m_spectatorCarIndex: int = None
        self.m_sliProNativeSupport: int = None
        self.m_numMarshalZones: int = None
        self.m_marshalZones: List[MarshalZone] = None
        self.m_safetyCarStatus: int = None
        self.m_networkGame: int = None
        self.m_numWeatherForecastSamples: int = None
        self.m_weatherForecastSamples: List[WeatherForecastSample] = None
        self.m_forecastAccuracy: int = None
        self.m_aiDifficulty: int = None
        self.m_seasonLinkIdentifier: int = None
        self.m_weekendLinkIdentifier: int = None
        self.m_sessionLinkIdentifier: int = None
        self.m_pitStopWindowIdealLap: int = None
        self.m_pitStopWindowLatestLap: int = None
        self.m_pitStopRejoinPosition: int = None
        self.m_steeringAssist: int = None
        self.m_brakingAssist: int = None
        self.m_gearBoxAssist: int = None
        self.m_pitAssist: int = None
        self.m_pitReleaseAssist: int = None
        self.m_ERSAssist: int = None
        self.m_DRSAssist: int = None
        self.m_dynamicRacingLine: int = None
        self.m_dynamicRacingLineType: int = None
        self.m_gameMode: int = None
        self.m_ruleSet: int = None
        self.m_timeOfDay: int = None
        self.m_sessionLength: int = None

    _pack_ = 1
    _fields_ = [
        ("m_header", PacketHeader),
        ("m_weather", c_uint8),
        ("m_trackTemperature", c_int8),
        ("m_airTemperature", c_int8),
        ("m_totalLaps", c_uint8),
        ("m_trackLength", c_uint16),
        ("m_sessionType", c_uint8),
        ("m_trackId", c_int8),
        ("m_formula", c_uint8),
        ("m_sessionTimeLeft", c_uint16),
        ("m_sessionDuration", c_uint16),
        ("m_pitSpeedLimit", c_uint8),
        ("m_gamePaused", c_uint8),
        ("m_isSpectating", c_uint8),
        ("m_spectatorCarIndex", c_uint8),
        ("m_sliProNativeSupport", c_uint8),
        ("m_numMarshalZones", c_uint8),
        ("m_marshalZones", MarshalZone * 21),
        ("m_safetyCarStatus", c_uint8),
        ("m_networkGame", c_uint8),
        ("m_numWeatherForecastSamples", c_uint8),
        ("m_weatherForecastSamples", WeatherForecastSample * 56),
        ("m_forecastAccuracy", c_uint8),
        ("m_aiDifficulty", c_uint8),
        ("m_seasonLinkIdentifier", c_uint32),
        ("m_weekendLinkIdentifier", c_uint32),
        ("m_sessionLinkIdentifier", c_uint8),
        ("m_pitStopWindowIdealLap", c_uint8),
        ("m_pitStopWindowLatestLap", c_uint8),
        ("m_pitStopRejoinPosition", c_uint8),
        ("m_steeringAssist", c_uint8),
        ("m_brakingAssist", c_uint8),
        ("m_gearBoxAssist", c_uint8),
        ("m_pitAssist", c_uint8),
        ("m_pitReleaseAssist", c_uint8),
        ("m_ERSAssist", c_uint8),
        ("m_DRSAssist", c_uint8),
        ("m_dynamicRacingLine", c_uint8),
        ("m_dynamicRacingLineType", c_uint8),
        ("m_gameMode", c_uint8),
        ("m_ruleSet", c_uint8),
        ("m_timeOfDay", c_uint32),
        ("m_sessionLength", c_uint8),
    ]
