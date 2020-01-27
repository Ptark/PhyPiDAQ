from ......phypidaq.MMA8451Config import MMA8451Config
from ..config import NumOption, ConfigModel
from ..item import SensorItem


class AccelerationSensorItem(SensorItem):
    def __init__(self):
        name: str = "Beschleunigungssensor"
        description: str = "Der Beschleunigungssensor misst die Beschleunigung in 3 Richtungen: x,y,z"
        config: ConfigModel = ConfigModel.ConfigModel()
        self._num_option: NumOption = self._config.add_num_option(NumOption.NumOption("Ausleserate, 100"))
        super().__init__(name, description, config, 3, MMA8451Config())

    def get_unit(self, output_number: int) -> str:
        if self._config.enum_options[output_number] is not None:
            return "m*s^2"
        return ""

