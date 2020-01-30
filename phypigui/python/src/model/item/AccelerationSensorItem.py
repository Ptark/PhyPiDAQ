# from ......phypidaq.MMA8451Config import MMA8451Config
from ..config.ConfigModel import ConfigModel
from ..config.NumOption import NumOption
from ..item.SensorItem import SensorItem


class AccelerationSensorItem(SensorItem):
    """Class models an acceleration sensor"""
    def __init__(self):
        name: str = "Beschleunigungssensor"
        description: str = "Der Beschleunigungssensor misst die Beschleunigung in 3 Richtungen: x,y,z"
        config: ConfigModel = ConfigModel()
        config.add_num_option(NumOption("Ausleserate", "", 100))
        super().__init__(name, description, config, 3, None)  # MMA8451Config())

    def get_unit(self, output_number: int = 0) -> str:
        """Returns unit for acceleration"""
        return "m*s^2"

