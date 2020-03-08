from typing import List

from ...config.ConfigModel import ConfigModel
from ...config.NumOption import NumOption
from ..sensors.SensorItem import SensorItem
# from phypidaq.MMA845xConfig import MMA845xConfig


class ForceSensorItem(SensorItem):
    """This class models a force sensor"""

    def __init__(self):
        """Initialising an ForceSensorItem object"""
        name: str = "Kraftsensor"
        description: str = "Der Kraftsensor misst die Kraft in Newton"

        config: ConfigModel = ConfigModel()
        config.add_num_option(NumOption("Ausleserate", "", 100))

        pins: List[int] = []

        super().__init__(name, description, config, 1, pins, None)  # MMA845xConfig())

    def get_unit(self, output_number: int = 0) -> str:
        return "N"

    @staticmethod
    def get_name() -> str:
        return "Kraftsensor"
