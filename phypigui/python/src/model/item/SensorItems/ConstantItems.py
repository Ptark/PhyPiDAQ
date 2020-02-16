import math

from enum import Enum
from typing import List, Dict, Callable

from .SensorItem import SensorItem
from ...config.ConfigModel import ConfigModel
from ...config.EnumOption import EnumOption
from ...config.NumOption import NumOption


class NatureConstantItem(SensorItem):
    """This class models an item, which has a constant value (pi or e)"""

    class NatureConstants(Enum):
        pi = math.pi
        e = math.e

    def __init__(self):
        """Initialising an NatureConstantItem object"""

        name: str = "Naturkonstantenelement"
        description: str = "Dieses Element gibt eine der folgenden Naturkonstanten aus"

        config: ConfigModel = ConfigModel()
        config.add_enum_option(EnumOption("Konstante", self.NatureConstants))

        pins: List[int] = []

        super().__init__(name, description, config, 1, pins, None)

    def get_rule(self, output_number: int = 0) -> Callable[[Dict[SensorItem, List[float]]], float]:
        return lambda data: list(self._config.enum_options[0].samples)[self._config.enum_options[0].selection].value

    def get_unit(self, output_number: int = 0) -> str:
        return ""

    @staticmethod
    def get_name() -> str:
        return "Naturkonstantenelement"


class ConstantItem(SensorItem):
    """This class models an item, which has a constant value set by the user"""

    def __init__(self):
        """Initialising a ConstantItem object"""

        name: str = "Konstantenelement"
        description: str = "Dieses Element gibt eine der vom Benutzer einstellbare Konstante aus"

        config: ConfigModel = ConfigModel()
        config.add_num_option(NumOption("Konstante"))

        pins: List[int] = []

        super().__init__(name, description, config, 1, pins, None)

    def get_rule(self, output_number: int = 0) -> Callable[[Dict[SensorItem, List[float]]], float]:
        return lambda data: self._config.num_options[0].number

    def get_unit(self, output_number: int = 0) -> str:
        return ""

    @staticmethod
    def get_name() -> str:
        return "Konstantenelement"
