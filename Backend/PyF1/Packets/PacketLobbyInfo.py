#  Copyright (c) 2022.
#
#  25/12/22, 10:55, PacketLobbyInfo.py created by Edoardo.

from ctypes import *
from typing import List

from Backend.PyF1.Packets import PacketHeader


class LobbyInfoData(LittleEndianStructure):

    def __init__(self) -> None:
        self.m_aiControlled: int = None
        self.m_teamId: int = None
        self.m_nationality: int = None
        self.m_name: str = None
        self.m_carNumber: int = None
        self.m_readyStatus: int = None  # 0 = not ready, 1 = ready, 2 = spectating

    _pack_ = 1
    _fields_ = [
        ("m_aiControlled", c_uint8),
        ("m_teamId", c_uint8),
        ("m_nationality", c_uint8),
        ("m_name", c_char * 48),
        ("m_carNumber", c_uint8),
        ("m_readyStatus", c_uint8)
    ]


class PacketLobbyInfo(LittleEndianStructure):

    def __init__(self) -> None:
        self.m_header: PacketHeader = None
        self.m_numPlayers: int = None
        self.m_lobbyPlayers: List[LobbyInfoData] = None  # 22 players max.

    _pack_ = 1
    _fields_ = [
        ("m_header", PacketHeader),
        ("m_numPlayers", c_uint8),
        ("m_lobbyPlayers", LobbyInfoData * 22)
    ]
