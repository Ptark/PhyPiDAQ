from typing import List

from ..item.SensorItem import SensorItem
from ..config.ConfigModel import ConfigModel
from ..config.FileOption import FileOption

class ProxySensorItem(SensorItem):
    """This class models a proxy sensor which reads from a file"""

    def __init__(self):
        """Initialize"""
        unit: str
        name: str = "Proxysensor"
        description: str = "Der Proxysensor lädt Einheit und Daten aus einer Datei und gibt sie aus."
        config: ConfigModel = ConfigModel()
        config.add_file_option(FileOption(name, description))
        super().__init__(name, description, config, 1, None)

    def set_file(self, path: str):
        pass
        # check if valid path to file
        # open file

    def get_unit(self, output_number: int = 0) -> str:
        assert self._config.file_options[0] is not None
        # return unit read from file

    def read(self) -> List[float]:
        pass
