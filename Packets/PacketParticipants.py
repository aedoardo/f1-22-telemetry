#  Copyright (c) 2022.
#
#  25/12/22, 10:55, PacketParticipants.py created by Edoardo.

from ctypes import *
from typing import List

from Packets.PacketHeader import PacketHeader


class ParticipantData(LittleEndianStructure):

    def __init__(self) -> None:
        self.m_aiControlled: int = None
        self.m_driverId: int = None
        self.m_networkId: int = None
        self.m_teamId: int = None
        self.m_myTeam: int = None
        self.m_raceNumber: int = None
        self.m_nationality: int = None
        self.m_name: str = None
        self.m_yourTelemetry: int = None

    _pack_ = 1
    _fields_ = [
        ("m_aiControlled", c_uint8),
        ("m_driverId", c_uint8),
        ("m_networkId", c_uint8),
        ("m_teamId", c_uint8),
        ("m_myTeam", c_uint8),
        ("m_raceNumber", c_uint8),
        ("m_nationality", c_uint8),
        ("m_name", c_char * 48),
        ("m_yourTelemetry", c_uint8)
    ]


class PacketParticipants(LittleEndianStructure):

    def __init__(self) -> None:

        self.m_header: PacketHeader = None
        self.m_numActiveCars: int = None
        self.m_participants: List[ParticipantData] = None

    _pack_ = 1
    _fields_ = [
        ("m_header", PacketHeader),
        ("m_numActiveCars", c_uint8),
        ("m_participants", ParticipantData * 22)
    ]
