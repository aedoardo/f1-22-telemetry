#  Copyright (c) 2022.
#
#  25/12/22, 10:54, BoardManager.py created by Edoardo.
from typing import Dict, Union
from operator import *
from math import inf

from Constants.teams import TEAMS
from Managers.ParticipantsManager import Participant
from Managers.SessionHistoryManager import Lap


class BoardManager:
    def __init__(self) -> None:
        self._board: Dict[int, Union[str, int]] = {}

    def get_board(self) -> Dict[int, Dict[str, Union[str, int]]]:
        return self._board

    def get_ordered_board(self) -> Dict[int, Dict[str, Union[str, int]]]:
        return sorted(self._board.items(),
                      key=lambda kv: kv[1]['bestLapTimeInMS'] if kv[1]["bestLapTimeInMS"] != -1 else 99999999)

    def _lap_time_formatted(self, milliseconds: int, isSector: bool = False) -> str:
        minutes, seconds_and_ms = divmod(milliseconds, 60000)
        seconds, milliseconds = divmod(seconds_and_ms, 1000)

        if not isSector or minutes > 0:
            return f"{minutes:02}:{seconds:02}:{milliseconds:03}"
        else:
            return f"{seconds:02}:{milliseconds:03}"

    def _is_best_sector(self, sectorTime: int, name: str, sectorNumber: int):
        mapSectors = {0: "sector1", 1: "sector2", 2: "sector3"}
        for pilot in self._board:

            if self._board[pilot]["name"] == name:
                continue

            if mapSectors[sectorNumber] in self._board[pilot]:
                if sectorTime > self._board[pilot][mapSectors[sectorNumber]] != -1:
                    return False

        return True

    def receive_update(self, participants: Dict[int, Participant],
                       laps: Dict[int, Dict[int, Lap]],
                       bestLaps: Dict[int, int]) -> None:

        if len(participants) == len(laps) and len(bestLaps) == len(participants):
            for idx, _ in enumerate(participants):
                participant: Participant = participants[_]
                bestLapIndex: int = bestLaps[idx]

                if bestLapIndex in laps[idx]:
                    bestLap: Lap = laps[idx][bestLapIndex]
                    self._board[idx] = {
                        "name": participant.m_name.decode("utf-8"),
                        "team": participant.m_teamId,
                        "bestLapTimeInMS": bestLap.get_lap_time_in_ms(),
                        "sector1": bestLap.get_sector_one_time_in_ms(),
                        "sector2": bestLap.get_sector_snd_in_ms(),
                        "sector3": bestLap.get_sector_thrd_in_ms(),
                        "teamName": TEAMS[participant.m_teamId],
                        "bestLapTimeFormatted": self._lap_time_formatted(bestLap.get_lap_time_in_ms()),
                        "sector1Formatted": self._lap_time_formatted(bestLap.get_sector_one_time_in_ms(), True),
                        "sector2Formatted": self._lap_time_formatted(bestLap.get_sector_snd_in_ms(), True),
                        "sector3Formatted": self._lap_time_formatted(bestLap.get_sector_thrd_in_ms(), True),
                        "isBestSector1": self._is_best_sector(bestLap.get_sector_one_time_in_ms(),
                                                              participant.m_name.decode("utf-8"), 0),
                        "isBestSector2": self._is_best_sector(bestLap.get_sector_snd_in_ms(),
                                                              participant.m_name.decode("utf-8"), 1),
                        "isBestSector3": self._is_best_sector(bestLap.get_sector_thrd_in_ms(),
                                                              participant.m_name.decode("utf-8"), 2),
                    }
                else:
                    self._board[idx] = {
                        "name": participant.m_name.decode("utf-8"),
                        "team": participant.m_teamId,
                        "bestLapTimeInMS": -1,
                        "sector1": -1,
                        "sector2": -1,
                        "sector3": -1,
                        "teamName": TEAMS[participant.m_teamId],
                        "bestLapTimeFormatted": "",
                        "sector1Formatted": "",
                        "sector2Formatted": "",
                        "sector3Formatted": "",
                        "isBestSector1": False,
                        "isBestSector2": False,
                        "isBestSector3": False
                    }
