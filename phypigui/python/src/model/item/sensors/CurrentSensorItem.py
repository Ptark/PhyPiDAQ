from typing import List

from ...config.ConfigModel import ConfigModel
from ...config.NumOption import NumOption
from ..sensors.SensorItem import SensorItem
# from phypidaq.INA219Config import INA219Config


# TODO: modify INA219Config and separate config for current-/voltage sensor
class CurrentSensorItem(SensorItem):
    """This class models a current sensor"""

    def __init__(self):
        """Initialising current sensor"""
        name: str = "Stromstärkesensor"
        description: str = "Der Stromstärkesensor misst die Stromstärke in milliampere"

        config: ConfigModel = ConfigModel()
        config.add_num_option(NumOption("Ausleserate in Millisekunden", "", 100, 10, 10000, 0))

        pins: List[int] = []

        super().__init__(name, description, config, 1, pins, None)  # INA219Config()

    def get_unit(self, output_number: int = 0) -> str:
        return "mA"

    @staticmethod
    def get_name() -> str:
        return "Stromstärkesensor"
