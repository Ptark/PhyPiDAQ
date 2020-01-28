from phypidaq.MMA8451Config import MMA8451Config
from ..config import NumOption, ConfigModel
from ..item import SensorItem


class AccelerationSensorItem(SensorItem):
    """Class models an acceleration sensor"""

    def __init__(self):
        name: str = "Beschleunigungssensor"
        description: str = "Der Beschleunigungssensor misst die Beschleunigung in 3 Richtungen: x,y,z"
        config: ConfigModel = ConfigModel.ConfigModel()
        self._num_option: NumOption = self._config.add_num_option(NumOption.NumOption("Ausleserate, 100"))
        super().__init__(name, description, config, 3, MMA8451Config())

    def get_unit(self, output_number: int) -> str:
        """Returns the unit with the direction of the given output"""
        direction = ["x", "y", "z"]
        return "(" + direction[output_number] + "): m / s^2"

