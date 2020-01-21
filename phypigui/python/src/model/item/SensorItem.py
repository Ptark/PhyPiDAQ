from __future__ import annotations
from abc import ABC
from ..item import OutputItem
from ..config import ConfigModel, EnumOption, NumOption
from typing import List, Callable, Dict, NoReturn
from PhyPiDAQ.phypidaq.ADS1115Config import *
from PhyPiDAQ.phypidaq.MMA8451Config import *


class SensorItem(OutputItem, ABC):
    def __init__(self, name: str, description: str, config: ConfigModel, outputs: int, sensor_config):
        self._device = sensor_config
        self._device.init()
        self._buffer: [float] = []
        self._last_read_time: int = 0
        super().__init__(name, description, config, outputs)

    def get_device(self):
        return self._device

    def get_number_of_outputs(self) -> int:
        return 1

    def get_rule(self, output_number: int) -> Callable[[Dict[SensorItem, List[float]]], float]:
        function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: data[self][output_number]
        return function

    def read(self) -> [float]:
        #TODO incomplete
        data: [float] = []
        read_time: int = int(time.time() * 1000)
        read_diff = read_time - self._last_read_time

        if read_diff < self.get_num_option(self.get_id()).number:
            return self._buffer

        self._device.acquireData(data)
        self._buffer = data
        self._last_read_time = int(time.time() * 1000)
        return self._buffer

    def close(self) -> NoReturn:
        self._device.closeDevice()

    def get_last_read_time(self) -> int:
        return self._last_read_time

    def get_buffer(self) -> [float]:
        return self._buffer

    def set_buffer(self, data: [float]) -> NoReturn:
        self._buffer = data


class TemperatureSensorItem(SensorItem):
    def __init__(self):
        name: str = "Temperatursensor"
        description: str = "Der Temperatursensor misst die Temperatur in Grad Celsius oder Kelvin"
        config: ConfigModel = ConfigModel.ConfigModel()
        self._config.add_enum_option(EnumOption.EnumOption("Einheit", ('Kelvin,Celsius')))
        self._config.add_num_option(NumOption.NumOption("Ausleserate", 100))
        super().__init__(name, description, config, 1, ADS1115Config())

    def get_unit(self) -> str:
        if self._config.enum_options[0] is not None:
            e_opt: EnumOption = self._config.enum_options[0]
            if e_opt.selection == 'Kelvin':
                return "K"
            return "°C"
        return ""


class AccelerationSensorItem(SensorItem):
    def __init__(self):
        name: str = "Beschleunigungssensor"
        description: str = "Der Beschleunigungssensor misst die Beschleunigung in 3 Richtungen: x,y,z"
        config: ConfigModel = ConfigModel.ConfigModel()
        self._num_option: NumOption = self._config.add_num_option(NumOption.NumOption("Ausleserate, 100"))
        super().__init__(name, description, config, 3, MMA8451Config())

    def get_unit(self, output_number: int) -> str:
        if self._config.enum_options[output_number] is not None:
            return "m*s^2"
        return ""

