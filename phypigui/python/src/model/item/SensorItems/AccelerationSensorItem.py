from ...config.NumOption import NumOption
from .SensorItem import SensorItem
from ...config.ConfigModel import ConfigModel
# from ......phypidaq.MMA8451Config import MMA8451Config


class AccelerationSensorItem(SensorItem):
    """This class models an acceleration sensor"""

    def __init__(self):
        """Initialising an AccelerationSensorItem object"""

        name: str = "Beschleunigungssensor"
        description: str = "Der Beschleunigungssensor misst die Beschleunigung in 3 Richtungen: x,y,z"

        config: ConfigModel = ConfigModel()
        config.add_num_option(NumOption("Ausleserate", "", 100))

        super().__init__(name, description, config, 3, None)  # MMA8451Config())

    def get_unit(self, output_number: int = 0) -> str:
        return "m*s^2"

    @staticmethod
    def get_name() -> str:
        return "Beschleunigungssensor"
