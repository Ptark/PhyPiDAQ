from typing import List

from ...config.ConfigModel import ConfigModel
from ...config.NumOption import NumOption
from ..sensors.SensorItem import SensorItem
from phypidaq.INA219Config import INA219Config


class VoltageSensorItem(SensorItem):
    """This class models a voltage sensor"""

    def __init__(self):
        """Initialising voltage sensor"""
        name: str = "Spannungssensor"
        description: str = "Der Spannungssensor misst die Spannung in Volt"

        config: ConfigModel = ConfigModel()
        config.add_num_option(NumOption("Ausleserate in Millisekunden", "", 100, SensorItem.MIN_READ_OUT_RATE,
                                        SensorItem.MAX_READ_OUT_RATE, 0))

        pins: List[int] = []

        super().__init__(name, description, config, 1, pins, INA219Config())

    def get_unit(self, output_number: int = 0) -> str:
        return "V"

    @staticmethod
    def get_name() -> str:
        return "Spannungssensor"
