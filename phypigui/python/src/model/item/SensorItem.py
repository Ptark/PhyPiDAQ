from __future__ import annotations

import time
from abc import ABC

from ..item import OutputItem
from ..config import ConfigModel, EnumOption, NumOption
from typing import List, Callable, Dict, NoReturn


class SensorItem(OutputItem, ABC):
    def __init__(self, name: str, description: str, config: ConfigModel, outputs: int, sensor_config):
        self._device = sensor_config
        self._device.init()
        self._buffer: [float] = []
        self._last_read_time: int = 0
        super().__init__(name, description, config, outputs)

    def get_device(self):
        return self._device

    def get_rule(self, output_number: int) -> Callable[[Dict[SensorItem, List[float]]], float]:
        function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: data[self][output_number]
        return function

    def read(self) -> [float]:
        data: [float] = [0]
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


