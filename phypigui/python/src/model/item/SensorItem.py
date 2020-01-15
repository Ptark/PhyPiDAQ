from __future__ import annotations
from abc import ABC, abstractmethod
from ..item import OutputItem
from ..item import Output
from ..config import ConfigModel, EnumOption, NumOption
from typing import List, Callable, Dict, NoReturn


class SensorItem(OutputItem, ABC):
    def __init__(self, buffer: [float], last_read_time: int):
        super(self).__init__()
        self._buffer = buffer
        self._last_read_time = last_read_time

    def get_number_of_outputs(self) -> int:
        return 1

    def get_rule(self, output_number: int) -> Callable[[Dict[SensorItem, List[float]]], float]:
        function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: data[self][output_number]
        return function

    def read(self) -> [float]:
        #TODO
        pass

    def close(self) -> NoReturn:
        #TODO
        pass

    def get_last_read_time(self) -> int:
        return self._last_read_time

    def get_buffer(self) -> [float]:
        return self._buffer


class TemperatureSensorItem(SensorItem):
    def __init__(self):
        super().__init__([None], 0)
        self._name: str = "Temperatursensor"
        self._description: str = "Der Temperatursensor misst die Temperatur in Grad Celsius oder Kelvin"
        self._outputs: [Output] = [Output.Output()]
        self._config: ConfigModel = ConfigModel.ConfigModel()
        self.__enum_option: EnumOption = self._config.add_enum_option(EnumOption.EnumOption("Einheit",('Kelvin,Celsius')))
        self.__num_option: NumOption = self._config.add_num_option(NumOption.NumOption("Ausleserate",100))

    def get_unit(self) -> str:
        if self._config.get_enum_options()[0] is not None:
            eOpt: EnumOption.NumOption = self._config.get_enum_options()[0]
            if eOpt.get_selection() == 'Kelvin':
                return "K"
            return "°C"
        return ""


class AccelerationSensorItem(SensorItem):
    def __init__(self):
        super().__init__([None] * 3, 0)
        self._name: str = "Beschleunigungssensor"
        self._description: str = "Der Beschleunigungssensor misst die Beschleunigung in 3 Richtungen: x,y,z"
        self._outputs: [Output] = [Output.Output()] * 3
        self._config: ConfigModel = ConfigModel.ConfigModel()
        self._num_option: NumOption = self._config.add_num_option(NumOption.NumOption("Ausleserate, 100"))

    def get_unit(self, output_number: int) -> str:
        if self._config.get_enum_options()[output_number] is not None:
            return "m*s^2"
        return ""

