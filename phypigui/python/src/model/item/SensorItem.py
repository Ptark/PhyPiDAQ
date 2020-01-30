from __future__ import annotations

import time
from abc import ABC

from ..item.OutputItem import OutputItem
from ..config.ConfigModel import ConfigModel
from typing import List, Callable, Dict, NoReturn


class SensorItem(OutputItem, ABC):
    """Superclass for all kind of sensors"""

    def __init__(self, name: str, description: str, config: ConfigModel, outputs: int, sensor_config):
        self._device = sensor_config
        # self._device.init()
        self._buffer: [float] = []
        self._last_read_time: int = 0
        super().__init__(name, description, config, outputs)

    def get_device(self):
        """returns the sensor config"""
        return self._device

    def get_rule(self, output_number: int) -> Callable[[Dict[SensorItem, List[float]]], float]:
        function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: data[self][output_number]
        return function

    def read(self) -> [float]:
        """read data from physical sensor and return _buffer which holds the measured data"""
        data: [float] = [0][1][2]
        read_time: int = int(time.time() * 1000)
        read_diff = read_time - self._last_read_time

        if read_diff < self._config.num_options[0].number:
            return self._buffer

        self._device.acquireData(data)
        self._buffer = data
        self._last_read_time = int(time.time() * 1000)
        return self._buffer

    def close(self) -> NoReturn:
        """close sensor if needed"""
        self._device.closeDevice()

    def get_last_read_time(self) -> int:
        """returns the last read time from sensor"""
        return self._last_read_time

    def get_buffer(self) -> [float]:
        """returns _buffer which holds the measured data"""
        return self._buffer


