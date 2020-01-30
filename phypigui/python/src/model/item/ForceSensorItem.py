from ..item.SensorItem import SensorItem
from ..config.ConfigModel import ConfigModel
from ..config.NumOption import NumOption
# from ......phypidaq.MMA845xConfig import MMA845xConfig


class ForceSensorItem(SensorItem):
    """Class models a force sensor"""
    def __init__(self):
        name: str = "Kraftsensor"
        description: str = "Der Kraftsensor misst die Kraft in Newton"
        config: ConfigModel = ConfigModel()
        config.add_num_option(NumOption("Ausleserate", 100))
        super().__init__(name, description, config, 1, None)  # MMA845xConfig())

    def get_unit(self, output_number: int = 0) -> str:
        """Returns the unit Newton"""
        return "N"
