#  Copyright (c) 2023.
#
#  02/01/23, 19:41, PacketLap.py created by Edoardo.

from ctypes import *
from typing import List

from Packets.PacketHeader import PacketHeader


class LapData(LittleEndianStructure):

    def __init__(self) -> None:
        self.m_lastLapTimeInMS: int = None
        self.m_currentLapTimeInMS: int = None
        self.m_sector1TimeInMS: int = None
        self.m_sector2TimeInMS: int = None
        self.m_lapDistance: float = None
        self.m_totalDistance: float = None
        self.m_safetyCarDelta: float = None
        self.m_carPosition: int = None
        self.m_currentLapNum: int = None
        self.m_pitStatus: int = None
        self.m_numPitStops: int = None
        self.m_sector: int = None
        self.m_currentLapInvalid: int = None
        self.m_penalties: int = None
        self.m_warnings: int = None
        self.m_numUnservedDriveThroughPens: int = None
        self.m_numUnservedStopGoPens: int = None
        self.m_gridPosition: int = None
        self.m_driverStatus: int = None
        self.m_resultStatus: int = None
        self.m_pitLaneTimerActive: int = None
        self.m_pitLaneTimeInLaneInMS: int = None
        self.m_pitStopTimerInMS: int = None
        self.m_pitStopShouldServePen: int = None

    _pack_ = 1
    _fields_ = [
        ("m_lastLapTimeInMS", c_uint32),
        ("m_currentLapTimeInMS", c_uint32),
        ("m_sector1TimeInMS", c_uint16),
        ("m_sector2TimeInMS", c_uint16),
        ("m_lapDistance", c_float),
        ("m_totalDistance", c_float),
        ("m_safetyCarDelta", c_float),
        ("m_carPosition", c_uint8),
        ("m_currentLapNum", c_uint8),
        ("m_pitStatus", c_uint8),
        ("m_numPitStops", c_uint8),
        ("m_sector", c_uint8),
        ("m_currentLapInvalid", c_uint8),
        ("m_penalties", c_uint8),
        ("m_warnings", c_uint8),
        ("m_numUnservedDriveThroughPens", c_uint8),
        ("m_numUnservedStopGoPens", c_uint8),
        ("m_gridPosition", c_uint8),
        ("m_driverStatus", c_uint8),
        ("m_resultStatus", c_uint8),
        ("m_pitLaneTimerActive", c_uint8),
        ("m_pitLaneTimeInLaneInMS", c_uint16),
        ("m_pitStopTimerInMS", c_uint16),
        ("m_pitStopShouldServePen", c_uint8)
    ]


class PacketLap(LittleEndianStructure):

    def __init__(self) -> None:
        self.m_header: PacketHeader = None
        self.m_lapData: List[LapData] = None
        self.m_timeTrialPBCarIdx: int = None
        self.m_timeTrialRivalCarIdx: int = None

    _pack_ = 1
    _fields_ = [
        ("m_header", PacketHeader),
        ("m_lapData", LapData * 22),
        ("m_timeTrialPBCarIdx", c_uint8),
        ("m_timeTrialRivalCarIdx", c_uint8)
    ]
