from ..item.SensorItem import SensorItem
from ..config import ConfigModel, NumOption
# from phypidaq.VL53LxConfig import VL53LxConfig


class DistanceSensorItem(SensorItem):
    """This class models a distance sensor"""

    def __init__(self):
        """Initialising an DistanceSensorItem object"""
        name: str = "Abstandssensor"
        description: str = "Der Abstandssensor misst den Abstand zu einem Objekt"

        config: ConfigModel = ConfigModel.ConfigModel()
        config.add_num_option(NumOption.NumOption("Ausleserate", "", 100))

        super().__init__(name, description, config, 1, None)  # VL53LxConfig())

    def get_unit(self, output_number: int = 0) -> str:
        return "mm"
