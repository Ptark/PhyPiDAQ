from phypigui.python.src.model.item.SensorItems.SensorItem import SensorItem
from phypigui.python.src.model.config.NumOption import NumOption
from phypigui.python.src.model.config.ConfigModel import ConfigModel
# from ......phypidaq import INA219Config


# TODO: modify INA219Config and separate config for current-/voltage sensor
class CurrentSensorItem(SensorItem):
    """This class models a current sensor"""

    def __init__(self):
        """Initialising current sensor"""
        name: str = "Stromsensor"
        description: str = "Der Stromsensor misst den Strom in milliampere"

        config: ConfigModel = ConfigModel()
        config.add_num_option(NumOption("Ausleserate", "", 100))

        super().__init__(name, description, config, 1, None)  # INA219Config()

    def get_unit(self, output_number: int = 0) -> str:
        return "mA"

