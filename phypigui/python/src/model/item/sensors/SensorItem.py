from __future__ import annotations

import random
import time

from abc import ABC, abstractmethod
from typing import List, Callable, Dict, NoReturn

from ...manager.ManagerModel import ManagerModel
from ..OutputItem import OutputItem
from ...config.ConfigModel import ConfigModel


class SensorItem(OutputItem, ABC):
    """This class is a superclass for all kind of sensors"""

    def __init__(self, name: str, description: str, config: ConfigModel, outputs: int, pins: List[int], sensor_config):
        """Initialising a SensorItem object

        Args:
            name (str): Name of this SensorItem
            description (str): Description of this SensorItem
            config (ConfigModel): A configuration of adjustable options for this SensorItem
            pins (List[int]): List of pin-numbers, which the hardware-sensor should be connected to
            outputs (int): Count of outputs for this SensorItem
            sensor_config: Configuration of a sensor from PhyPiDAQ
        """
        super().__init__(name, description, config, outputs)

        self._device = sensor_config
        # self._device.init()
        self._buffer: List[float] = []
        for n in range(3):
            self._buffer.append(0)
        self._last_read_time: int = 0
        self._pins: List[int] = pins

        ManagerModel.add_sensor(self)

    def __del__(self):
        #self.close()
        pass

    @property
    def device(self):
        """Configuration (from PhyPiDAQ) of a sensor, this SensorItem represents"""
        return self._device

    @property
    def buffer(self) -> List[float]:
        """Buffer, which contains the last read data from the hardware sensor"""
        return self._buffer

    @property
    def pins(self) -> List[int]:
        """List of pin-numbers, which the hardware-sensor should be connected to"""
        return self._pins

    def get_rule(self, output_number: int = 0) -> Callable[[Dict[SensorItem, List[float]]], float]:
        function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: data[self][output_number]
        return function

    def read(self) -> List[float]:
        """Read data from physical or simulated sensor and returns a List of every measured value of the sensor

        Returns:
            List[float]: List of measured values
        """
        return [random.random()] * self.get_count_of_outputs()  # for testing
        read_time: int = int(time.time() * 1000)
        read_diff = read_time - self._last_read_time
        if read_diff >= self._config.num_options[0].number:
            data: List[float] = []
            self._device.acquireData(data)
            self._buffer = data
            self._last_read_time = read_time
        return self._buffer

    def close(self) -> NoReturn:
        """Close sensor if needed"""
        self._device.closeDevice()

    @property
    def last_read_time(self) -> int:
        """Last read time of this SensorItem in milliseconds"""
        return self._last_read_time
