from enum import Enum

from ..item.SensorItem import SensorItem
from ..config.NumOption import NumOption
from ..config.EnumOption import EnumOption
# from ......phypidaq import DS18B20Config
from ..config.ConfigModel import ConfigModel


class TemperatureSensorItem(SensorItem):
    """This class models a temperature sensor"""

    class __TemperatureUnit(Enum):
        """Enum which holds the possible units"""
        KELVIN = 'Kelvin'
        CELSIUS = 'Celsius'

    def __init__(self):
        """Initialising a TemperatureSensorItem object"""
        name: str = "Temperatursensor"
        description: str = "Der Temperatursensor misst die Temperatur in Grad Celsius oder Kelvin"

        config: ConfigModel = ConfigModel()
        config.add_enum_option(EnumOption("Einheit", self.__TemperatureUnit))
        config.add_num_option(NumOption("Ausleserate", "", 100))

        super().__init__(name, description, config, 1, None)  # DS18B20Config())

    def get_unit(self, output_number: int = 0) -> str:
        assert self._config.enum_options[0] is not None
        assert output_number != 0

        enum_opt = self._config.enum_options[0]
        return enum_opt.samples[enum_opt.selection]
