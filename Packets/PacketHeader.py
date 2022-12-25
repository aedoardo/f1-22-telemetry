#  Copyright (c) 2022.
#
#  25/12/22, 10:53, PacketHeader.py created by Edoardo.

from ctypes import *


class PacketHeader(LittleEndianStructure):

    _pack_ = 1
    _fields_ = [
        ("m_packetFormat", c_uint16),
        ("m_gameMajorVersion", c_uint8),
        ("m_gameMinorVersion", c_uint8),
        ("m_packetVersion", c_uint8),
        ("m_packetId", c_uint8),
        ("m_sessionUID", c_uint64),
        ("m_sessionTime", c_float),
        ("m_frameIdentifier", c_uint32),
        ("m_playerCarIndex", c_uint8),
        ("m_secondaryPlayerCarIndex", c_uint8)
    ]

    def __init__(self) -> None:
        self.m_packetFormat: int = None
        self.m_gameMajorVersion: int = None
        self.m_gameMinorVersion: int = None
        self.m_packetVersion: int = None
        self.m_packetId: int = None
        self.m_sessionUID: int = None
        self.m_sessionTime: float = None
        self.m_frameIdentifier: int = None
        self.m_playerCarIndex: int = None
        self.m_secondaryPlayerCarIndex: int = None
