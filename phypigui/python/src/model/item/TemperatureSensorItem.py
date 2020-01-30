from enum import Enum

from ..item.SensorItem import SensorItem
from ..config.ConfigModel import ConfigModel
from ..config.EnumOption import EnumOption
from ..config.NumOption import NumOption
# from ......phypidaq import DS18B20Config


class TemperatureSensorItem(SensorItem):
    """Class models a temperature sensor"""

    def __init__(self):
        name: str = "Temperatursensor"
        description: str = "Der Temperatursensor misst die Temperatur in Grad Celsius oder Kelvin"
        config: ConfigModel = ConfigModel()
        config.add_enum_option(EnumOption("Einheit", _TemperatureUnit))
        config.add_num_option(NumOption("Ausleserate", "", 100))
        super().__init__(name, description, config, 1, None)  # DS18B20Config())

    def get_unit(self, output_number: int = 0) -> str:
        """Returns the currently selected unit"""
        assert self._config.enum_options[0] is not None
        assert output_number != 0
        enum_opt = self._config.enum_options[0]
        return enum_opt.samples[enum_opt.selection]


class _TemperatureUnit(Enum):
    """Enum which holds the possible units"""
    KELVIN = 'Kelvin'
    CELSIUS = 'Celsius'
