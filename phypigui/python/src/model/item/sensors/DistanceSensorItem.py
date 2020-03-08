from typing import List

from ..sensors.SensorItem import SensorItem
from ...config.ConfigModel import ConfigModel
from ...config.NumOption import NumOption
from phypidaq.VL53LxConfig import VL53LxConfig


class DistanceSensorItem(SensorItem):
    """This class models a distance sensor"""

    def __init__(self):
        """Initialising an DistanceSensorItem object"""
        name: str = "Abstandssensor"
        description: str = "Der Abstandssensor misst den Abstand zu einem Objekt"

        config: ConfigModel = ConfigModel()
        config.add_num_option(NumOption("Ausleserate in Millisekunden", "", 100, SensorItem.MIN_READ_OUT_RATE,
                                        SensorItem.MAX_READ_OUT_RATE, 0))

        pins: List[int] = []

        super().__init__(name, description, config, 1, pins, VL53LxConfig({'range': 3}))

    def get_unit(self, output_number: int = 0) -> str:
        return "mm"

    @staticmethod
    def get_name() -> str:
        return "Abstandssensor"
