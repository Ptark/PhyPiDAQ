from phypigui.python.src.model.item.SensorItems.SensorItem import SensorItem
from phypigui.python.src.model.config.NumOption import NumOption
from phypigui.python.src.model.config.ConfigModel import ConfigModel
# from ......phypidaq import INA219Config


class VoltageSensorItem(SensorItem):
    """This class models a voltage sensor"""

    def __init__(self):
        """Initialising voltage sensor"""
        name: str = "Spannungssensor"
        description: str = "Der Spannungssensor misst die Spannung in Volt"

        config: ConfigModel = ConfigModel()
        config.add_num_option(NumOption("Ausleserate", "", 100))

        super().__init__(name, description, config, 1, None)  # INA219Config()

    def get_unit(self, output_number: int = 0) -> str:
        return "V"
