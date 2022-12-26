#  Copyright (c) 2022.
#
#  25/12/22, 10:53, SessionHistoryManager.py created by Edoardo.

from typing import Dict

from Packets.PacketSessionHistory import PacketSessionHistory, LapHistoryData


class Lap:

    def __init__(self, _lapTimeInMS: int, _sector1TimeInMS: int, _sector2TimeInMS: int, _sector3TimeInMS: int,
                 _validLap: int):
        self._lapTimeInMS: int = _lapTimeInMS
        self._sector1TimeInMS: int = _sector1TimeInMS
        self._sector2TimeInMS: int = _sector2TimeInMS
        self._sector3TimeInMS: int = _sector3TimeInMS
        self._isValid: int = _validLap

    def get_lap_time_in_ms(self) -> int:
        return self._lapTimeInMS

    def get_sector_one_time_in_ms(self) -> int:
        return self._sector1TimeInMS

    def get_sector_snd_in_ms(self) -> int:
        return self._sector2TimeInMS

    def get_sector_thrd_in_ms(self) -> int:
        return self._sector3TimeInMS


class SessionHistoryManager:

    def __init__(self):
        self._laps: Dict[int, Dict[int, Lap]] = {}
        self._bestLaps: Dict[int, int] = {}

    def get_laps(self) -> Dict[int, Dict[int, Lap]]:
        return self._laps

    def get_best_laps(self) -> Dict[int, int]:
        return self._bestLaps

    def handle_data_packet(self, packet: PacketSessionHistory):
        carIdx: int = packet.m_carIdx
        if carIdx not in self._laps:  # if we do not have data for this car, then initialize in the dict.
            self._laps[carIdx] = {}

        if carIdx not in self._bestLaps or carIdx in self._bestLaps \
                and packet.m_bestLapTimeLapNum != self._bestLaps[carIdx]:  # add the bestLap for this carIdx
            self._bestLaps[carIdx] = packet.m_bestLapTimeLapNum

        index: int
        lapData: LapHistoryData
        for (index, lapData) in enumerate(packet.m_lapHistoryData):
            if lapData.m_lapTimeInMS > 0:  # save lap only if it is a completed lap.
                self._laps[carIdx][(index + 1)] = Lap(lapData.m_lapTimeInMS, lapData.m_sector1TimeInMS,
                                                      lapData.m_sector2TimeInMS, lapData.m_sector3TimeInMS,
                                                      lapData.m_lapValidBitFlags)
