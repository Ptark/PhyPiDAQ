from ..item.SensorItem import SensorItem
from ..config.ConfigModel import ConfigModel
from ..config.EnumOption import EnumOption
from ..config.NumOption import NumOption
from ......phypidaq.ADS1115Config import ADS1115Config


class ForceSensorItem(SensorItem):
    def __init__(self):
        name: str = "Kraftsensor"
        description: str = "Der Kraftsensor misst die Kraft in Newton"
        config: ConfigModel = ConfigModel.ConfigModel()
        self.__config.add_num_option(NumOption.NumOption("Ausleserate", 100))
        super().__init__(name, description, config, 1, MMA845xConfig())

    def get_unit(self) -> str:
        """Returns the unit Newton"""
        return "Newton"
