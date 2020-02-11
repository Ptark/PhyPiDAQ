from ...config.ConfigModel import ConfigModel
from ...config.NumOption import NumOption
from ..SensorItems.SensorItem import SensorItem
# from ......phypidaq import TCS34725Config


class RGBSensorItem(SensorItem):
    """This class models a rgb sensor"""

    def __init__(self):
        """Initialising rgb sensor"""
        name: str = "RGB Sensor"
        description: str = "Der RGB Sensor detektiert Farben und gibt ihre Farbanteile für rot, grün und blau an"

        config: ConfigModel = ConfigModel()
        config.add_num_option(NumOption("Ausleserate", "", 100))

        super().__init__(name, description, config, 1, None)  # TCS34725Config

    def get_unit(self, output_number: int = 0) -> str:
        return "rot grün blau"