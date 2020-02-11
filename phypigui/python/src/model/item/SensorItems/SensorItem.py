from __future__ import annotations

import time

from abc import ABC
from typing import List, Callable, Dict, NoReturn

from ...manager.ManagerModel import ManagerModel
from ..OutputItem import OutputItem
from ...config.ConfigModel import ConfigModel


class SensorItem(OutputItem, ABC):
    """This class is a superclass for all kind of SensorItems"""

    def __init__(self, name: str, description: str, config: ConfigModel, outputs: int, sensor_config):
        """Initialising a SensorItem object

        Args:
            name (str): Name of this SensorItem
            description (str): Description of this SensorItem
            config (ConfigModel): A configuration of adjustable options for this SensorItem
            outputs (int): Count of outputs for this SensorItem
            sensor_config: Configuration of a sensor from PhyPiDAQ
        """
        super().__init__(name, description, config, outputs)

        self._device = sensor_config
        # self._device.init()
        self._buffer: List[float] = []
        self._last_read_time: int = 0

        ManagerModel.add_sensor(self)

    @property
    def device(self):
        """Configuration (from PhyPiDAQ) of a sensor, this SensorItem represents"""
        return self._device

    @property
    def buffer(self) -> List[float]:
        """Buffer, which contains the last read data from the hardware sensor"""
        return self._buffer

    def get_rule(self, output_number: int = 0) -> Callable[[Dict[SensorItem, List[float]]], float]:
        function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: data[self][output_number]
        return function

    def read(self) -> List[float]:
        """read data from physical sensor and return _buffer which holds the measured data""" # TODO doc
        data: [float] = [0][1][2]   # TODO watttt?
        read_time: int = int(time.time() * 1000)
        read_diff = read_time - self._last_read_time

        if read_diff < self._config.num_options[0].number:
            return self._buffer

        self._device.acquireData(data)
        self._buffer = data
        self._last_read_time = int(time.time() * 1000)
        return self._buffer

    def close(self) -> NoReturn:
        """Close sensor if needed""" # TODO doc
        self._device.closeDevice()

    def get_last_read_time(self) -> int:    # TODO unit of time??
        """Returns the last read time of this SensorItem

        This method return the last time read() was called for this SensorItem

        Returns:
            int: Last read time
        """
        return self._last_read_time
