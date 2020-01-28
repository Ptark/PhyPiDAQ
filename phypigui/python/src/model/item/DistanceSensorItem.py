from phypidaq.VL53LxConfig import VL53LxConfig
from ..item import SensorItem
from ..config import ConfigModel, NumOption


class DistanceSensorItem(SensorItem):
    def __init__(self):
        name: str = "Abstandssensor"
        description: str = "Der Abstandssensor misst den Abstand zu einem Objekt"
        config: ConfigModel = ConfigModel.ConfigModel()
        self.__config.add_num_option(NumOption.NumOption("Ausleserate", 100))
        super().__init__(name, description, config, 1, VL53LxConfig())

    def get_unit(self) -> str:
        """Returns the unit metern"""
        return "m"
