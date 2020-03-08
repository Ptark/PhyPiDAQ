from typing import List

from ...config.ConfigModel import ConfigModel
from ...config.NumOption import NumOption
from ..sensors.SensorItem import SensorItem
from phypidaq.TCS34725Config import TCS34725Config


class RGBSensorItem(SensorItem):
    """This class models a rgb sensor"""

    def __init__(self):
        """Initialising rgb sensor"""
        name: str = "RGB Sensor"
        description: str = "Der RGB Sensor detektiert Farben und gibt ihre Farbanteile für rot, grün und blau an"

        config: ConfigModel = ConfigModel()
        config.add_num_option(NumOption("Ausleserate in Millisekunden", "", 100, SensorItem.MIN_READ_OUT_RATE,
                                        SensorItem.MAX_READ_OUT_RATE, 0))

        pins: List[int] = []

        super().__init__(name, description, config, 1, pins, TCS34725Config())

    def get_unit(self, output_number: int = 0) -> str:
        return "RGB"

    @staticmethod
    def get_name() -> str:
        return "RGB Sensor"
