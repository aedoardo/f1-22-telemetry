#  Copyright (c) 2022.
#
#  25/12/22, 10:59, MainManager.py created by Edoardo.

import sys, os

from ctypes import *
from typing import Dict, Tuple, Union, Type, Any
from time import time
from socketio import Client

from Managers.BoardManager import BoardManager
from Managers.ParticipantsManager import ParticipantsManager
from Managers.SessionHistoryManager import SessionHistoryManager
from Packets.PacketHeader import PacketHeader
from Packets.PacketLobbyInfo import PacketLobbyInfo
from Packets.PacketParticipants import PacketParticipants
from Packets.PacketSessionHistory import PacketSessionHistory


class PacketsManager:

    def __init__(self):
        self._currentFrameIdentifier: int = -1
        self._participantsManager: ParticipantsManager = ParticipantsManager()
        self._sessionHistoryManager: SessionHistoryManager = SessionHistoryManager()
        self._boardManager: BoardManager = BoardManager()
        self._socketIoClient: Client = Client()
        self._socketIoClient.connect("http://localhost:3001")

        self._dispatcher: Dict[
            int, Tuple[Union[Type[PacketLobbyInfo], Type[PacketParticipants]]], Union[Type[ParticipantsManager]]] = {
            4: (PacketParticipants, self._participantsManager),
            9: (PacketLobbyInfo,),
            11: (PacketSessionHistory, self._sessionHistoryManager)
        }

        self._webDispatch: Dict[str, Tuple[Any, float]] = {
            "send_board": (self._boardManager.get_ordered_board, 1)
        }

        self._webDispatchTimings: Dict[str, float] = {
            "send_board": time()
        }

    def onData(self, data: bytes) -> None:
        dataBuffer = create_string_buffer(data, size=2048)
        headerData: PacketHeader = PacketHeader.from_buffer_copy(dataBuffer)

        if self._currentFrameIdentifier == -1:
            self._currentFrameIdentifier = headerData.m_frameIdentifier

        if self._currentFrameIdentifier > headerData.m_frameIdentifier:
            print("Flashback occurred.")  # TODO: handle the flashback.

        self._currentFrameIdentifier = headerData.m_frameIdentifier

        if headerData.m_packetId in self._dispatcher:
            packet: Union[PacketLobbyInfo, PacketParticipants] = self._dispatcher[headerData.m_packetId][
                0].from_buffer_copy(dataBuffer)
            manager: Union[ParticipantsManager] = self._dispatcher[headerData.m_packetId][1]
            manager.handle_data_packet(packet)

        self._boardManager.receive_update(self._participantsManager.get_participants(),
                                          self._sessionHistoryManager.get_laps(),
                                          self._sessionHistoryManager.get_best_laps())

        for message in self._webDispatch:
            currentTime: float = time()
            waitingTime: float = self._webDispatch[message][1]

            if currentTime - self._webDispatchTimings[message] >= waitingTime:
                self._socketIoClient.emit(
                    message, self._webDispatch[message][0]()
                )

                self._webDispatchTimings[message] = currentTime

