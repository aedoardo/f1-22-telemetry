#  Copyright (c) 2022.
#
#  27/12/22, 17:35, SessionManager.py created by Edoardo.
from typing import Union, Dict

from Constants.sessions import SESSION_TYPES
from Constants.tracks import TRACKS
from Packets.PacketSession import PacketSession


class SessionManager:

    def __init__(self) -> None:
        self._data: Dict[str, Union[str, int, float]] = {}

    def _convert_seconds(self, seconds: int) -> str:
        minutes: int = seconds // 60
        seconds: int = seconds % 60

        return f"{minutes:02d}:{seconds:02d}"

    def handle_data_packet(self, packet: PacketSession) -> None:
        self._data = {
            "airTemperature": packet.m_airTemperature,
            "trackTemperature": packet.m_trackTemperature,
            "trackLength": packet.m_trackLength,
            "trackId": packet.m_trackId,
            "trackName": TRACKS[packet.m_trackId],
            "sessionType": packet.m_sessionType,
            "sessionTypeName": SESSION_TYPES[packet.m_sessionType],
            "timeLeftInSeconds": packet.m_sessionTimeLeft,
            "timeLeftFormatted": self._convert_seconds(packet.m_sessionTimeLeft),
            "weather": packet.m_weather
        }

    def get_session_data(self) -> Dict[str, Union[str, int, float]]:
        return self._data
