from enum import Enum

from ..item import SensorItem
from ..config import ConfigModel, EnumOption, NumOption
from ......phypidaq import DS18B20Config


class TemperatureSensorItem(SensorItem):
    """Class models a temperature sensor"""

    def __init__(self):
        name: str = "Temperatursensor"
        description: str = "Der Temperatursensor misst die Temperatur in Grad Celsius oder Kelvin"
        config: ConfigModel = ConfigModel.ConfigModel()
        config.add_enum_option(EnumOption.EnumOption("Einheit", _TemperatureUnit))
        config.add_num_option(NumOption.NumOption("Ausleserate", 100))
        super().__init__(name, description, config, 1, DS18B20Config())

    def get_unit(self) -> str:
        """Returns the currently selected unit"""
        assert self.__config.enum_options[0] is not None
        enum_opt = self.__config.enum_options[0]
        return enum_opt.get_samples(enum_opt.selection)


class _TemperatureUnit(Enum):
    """Enum which holds the possible units"""
    KELVIN = 'Kelvin'
    CELSIUS = 'Celsius'
