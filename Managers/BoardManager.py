#  Copyright (c) 2022.
#
#  25/12/22, 10:54, BoardManager.py created by Edoardo.
from typing import Dict, Union
from operator import *

from Managers.ParticipantsManager import Participant
from Managers.SessionHistoryManager import Lap


class BoardManager:
    def __init__(self) -> None:
        self._board: Dict[int, Union[str, int]] = {}

    def get_board(self) -> Dict[int, Dict[str, Union[str, int]]]:
        return self._board

    def get_ordered_board(self) -> Dict[int, Dict[str, Union[str, int]]]:
        return sorted(self._board.items(), key=lambda kv: getitem(kv[1], 'bestLapTimeInMS'))

    def receive_update(self, participants: Dict[int, Participant],
                       laps: Dict[int, Dict[int, Lap]],
                       bestLaps: Dict[int, int]) -> None:

        for idx, _ in enumerate(participants):
            if idx in participants:
                participant: Participant = participants[idx]

                if idx in bestLaps:
                    bestLapIndex: int = bestLaps[idx]

                    if idx in laps and bestLapIndex in laps[idx]:
                        bestLap: Lap = laps[idx][bestLapIndex]
                        self._board[idx] = {
                            "name": participant.m_name,
                            "team": participant.m_teamId,
                            "bestLapTimeInMS": bestLap.get_lap_time_in_ms(),
                            "sector1": bestLap.get_sector_one_time_in_ms(),
                            "sector2": bestLap.get_sector_snd_in_ms(),
                            "sector3": bestLap.get_sector_thrd_in_ms(),
                        }
