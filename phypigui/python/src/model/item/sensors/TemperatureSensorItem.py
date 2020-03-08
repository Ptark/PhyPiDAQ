from enum import Enum
from typing import List

from ...config.ConfigModel import ConfigModel
from ...config.NumOption import NumOption
from ...config.EnumOption import EnumOption
from ..sensors.SensorItem import SensorItem
from phypidaq.DS18B20Config import DS18B20Config


class TemperatureSensorItem(SensorItem):
    """This class models a temperature sensor"""

    class __TemperatureUnit(Enum):
        """Enum which holds the possible units"""
        Kelvin = 'K'
        Celsius = '°C'

    def __init__(self):
        """Initialising a TemperatureSensorItem object"""
        name: str = "Temperatursensor"
        description: str = "Der Temperatursensor misst die Temperatur in Grad Celsius oder Kelvin"

        config: ConfigModel = ConfigModel()
        config.add_enum_option(EnumOption("Einheit", self.__TemperatureUnit, start_selection=1))
        config.add_num_option(NumOption("Ausleserate in Millisekunden", "", 100, SensorItem.MIN_READ_OUT_RATE,
                                        SensorItem.MAX_READ_OUT_RATE, 0))

        # data = 4, GND = 5, VCC = 9
        pins: List[int] = [4, 5, 9]

        super().__init__(name, description, config, 1, pins, DS18B20Config.DS18B20Config())

    def get_unit(self, output_number: int = 0) -> str:
        assert self._config.enum_options[0] is not None

        enum_opt = self._config.enum_options[0]
        return list(enum_opt.samples)[enum_opt.selection].value

    @staticmethod
    def get_name() -> str:
        return "Temperatursensor"
