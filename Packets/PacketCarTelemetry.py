#  Copyright (c) 2023.
#
#  02/01/23, 19:27, PacketCarTelemetry.py created by Edoardo.

from ctypes import *
from typing import List

from Packets.PacketHeader import PacketHeader


class CarTelemetryData(LittleEndianStructure):

    def __init__(self) -> None:
        self.m_speed: int = None
        self.m_throttle: float = None
        self.m_steer: float = None
        self.m_brake: float = None
        self.m_clutch: int = None
        self.m_gear: int = None
        self.m_engineRPM: int = None
        self.m_drs: int = None
        self.m_revLightsPercent: int = None
        self.m_revLightsBitValue: int = None
        self.m_brakesTemperature: List[int] = []
        self.m_tyresSurfaceTemperature: List[int] = []
        self.m_tyresInnerTemperature: List[int] = []
        self.m_engineTemperature: int = None
        self.m_tyresPressure: List[float] = []
        self.m_surfaceType: List[int] = []

    _pack_ = 1
    _fields_ = [
        ("m_speed", c_uint16),
        ("m_throttle", c_float),
        ("m_steer", c_float),
        ("m_brake", c_float),
        ("m_clutch", c_uint8),
        ("m_gear", c_int8),
        ("m_engineRPM", c_uint16),
        ("m_drs", c_uint8),
        ("m_revLightsPercent", c_uint8),
        ("m_revLightsBitValue", c_uint16),
        ("m_brakesTemperature", c_uint16 * 4),
        ("m_tyresSurfaceTemperature", c_uint8 * 4),
        ("m_tyresInnerTemperature", c_uint8 * 4),
        ("m_engineTemperature", c_uint16),
        ("m_tyresPressure", c_float * 4),
        ("m_surfaceType", c_uint8 * 4)
    ]


class PacketCarTelemetry(LittleEndianStructure):

    def __init__(self) -> None:
        self.m_header: PacketHeader = None
        self.m_carTelemetryData: List[CarTelemetryData] = None
        self.m_mfdPanelIndex: int = None
        self.m_mfdPanelIndexSecondaryPlayer: int = None
        self.m_suggestedGear: int = None

    _pack_ = 1
    _fields_ = [
        ("m_header", PacketHeader),
        ("m_carTelemetryData", CarTelemetryData * 22),
        ("m_mfdPanelIndex", c_uint8),
        ("m_mfdPanelIndexSecondaryPlayer", c_uint8),
        ("m_suggestedGear", c_uint8)
    ]
