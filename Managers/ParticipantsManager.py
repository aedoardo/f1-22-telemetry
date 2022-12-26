#  Copyright (c) 2022.
#
#  25/12/22, 10:55, ParticipantsManager.py created by Edoardo.

from typing import Dict

from Packets.PacketParticipants import PacketParticipants


class Participant:

    def __init__(self, _aiControlled: int, _driverId: int, _networkId: int, _teamId: int, _myTeam: int, _raceNumber: int,
                 _nationality: int, _name: bytes, _yourTelemetry: int) -> None:

        self.m_aiControlled: int = _aiControlled  # 1 if AI, 0 if human
        self.m_driverId: int = _driverId
        self.m_networkId: int = _networkId
        self.m_teamId: int = _teamId
        self.m_myTeam: int = _myTeam
        self.m_raceNumber: int = _raceNumber
        self.m_nationality: int = _nationality
        self.m_name: bytes = _name
        self.m_yourTelemetry: int = _yourTelemetry


class ParticipantsManager:

    def __init__(self) -> None:
        self._participants: Dict[int, Participant] = {}

    def _get_participant(self, index) -> Participant:
        return self._participants[index]

    def _add_participant(self, index: int, data: Participant) -> None:
        self._participants[index]: Participant = data

    def get_participants(self) -> Dict[int, Participant]:
        return self._participants

    def handle_data_packet(self, packet: PacketParticipants) -> None:

        if not self._participants:  # we need to initialize all the participant.
            for (index, _participant) in enumerate(packet.m_participants):
                if _participant.m_name.decode("utf-8") != "":
                    newParticipant = Participant(_participant.m_aiControlled, _participant.m_driverId,
                                                 _participant.m_networkId, _participant.m_teamId, _participant.m_myTeam,
                                                 _participant.m_raceNumber, _participant.m_nationality, _participant.m_name,
                                                 _participant.m_yourTelemetry) # initialize a new Participant class.

                    self._participants[index] = newParticipant

            print("Participants data initialized successfully.")





