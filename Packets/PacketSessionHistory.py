#  Copyright (c) 2022.
#
#  25/12/22, 10:55, PacketSessionHistory.py created by Edoardo.

from ctypes import *
from typing import List

from Packets.PacketHeader import PacketHeader


class LapHistoryData(LittleEndianStructure):

    def __init__(self):
        self.m_lapTimeInMS: int = None
        self.m_sector1TimeInMS: int = None
        self.m_sector2TimeInMS: int = None
        self.m_sector3TimeInMS: int = None
        self.m_lapValidBitFlags: int = None

    _pack_ = 1
    _fields_ = [
        ("m_lapTimeInMS", c_uint32),
        ("m_sector1TimeInMS", c_uint16),
        ("m_sector2TimeInMS", c_uint16),
        ("m_sector3TimeInMS", c_uint16),
        ("m_lapValidBitFlags", c_uint8)
    ]


class TyreStintHistoryData(LittleEndianStructure):

    def __init__(self):
        self.m_endLap: int = None
        self.m_tyreActualCompound: int = None
        self.m_tyreVisualCompound: int = None

    _pack_ = 1
    _fields_ = [
        ("m_endLap", c_uint8),
        ("m_tyreActualCompound", c_uint8),
        ("m_tyreVisualCompound", c_uint8)
    ]


class PacketSessionHistory(LittleEndianStructure):

    def __init__(self):
        self.m_header: PacketHeader = None
        self.m_carIdx: int = None
        self.m_numLaps: int = None
        self.m_numTyreStints: int = None
        self.m_bestLapTimeLapNum: int = None
        self.m_bestSector1LapNum: int = None
        self.m_bestSector2LapNum: int = None
        self.m_bestSector3LapNum: int = None
        self.m_lapHistoryData: List[LapHistoryData] = []
        self.m_tyreStintsHistoryData: List[TyreStintHistoryData] = []

    _pack_ = 1
    _fields_ = [
        ("m_header", PacketHeader),
        ("m_carIdx", c_uint8),
        ("m_numLaps", c_uint8),
        ("m_numTyreStints", c_uint8),
        ("m_bestLapTimeLapNum", c_uint8),
        ("m_bestSector1LapNum", c_uint8),
        ("m_bestSector2LapNum", c_uint8),
        ("m_bestSector3LapNum", c_uint8),
        ("m_lapHistoryData", LapHistoryData * 100),
        ("m_tyreStintsHistoryData", TyreStintHistoryData * 8)
    ]