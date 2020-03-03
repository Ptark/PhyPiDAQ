import time
from pathlib import Path
from typing import List, NoReturn
import json

from .SensorItem import SensorItem
from ...config.ConfigModel import ConfigModel
from ...config.FileOption import FileOption
from ....Exceptions import PathDoesntExist


class ProxySensorItem(SensorItem):
    """This class models a proxy sensor which reads from a file"""

    def __init__(self):
        """Initialize"""
        self.unit: str = ""
        self.data: List[float] = []
        self.current_index: int = 0
        # Config
        start_path: str = str(Path(".").resolve()) + "/phypigui/python/resources/data/"
        config: ConfigModel = ConfigModel()
        config.add_file_option(FileOption("Dateipfad", "Der Dateipfad der einzulesenden Datei",
                                          FileOption.EXISTINGFILE, "PhyPiGUI-Dateien", ["ppg"], Path(start_path)))

        pins: List[int] = []

        name: str = "Von Datei Lesen"
        description: str = "Lädt Einheit und Daten aus einer Datei und gibt sie aus"
        super().__init__(name, description, config, 1, pins, None)

    def __set_file(self, path: Path):
        """Sets file, unit and data if the given path leads to a valid json file"""
        if path is None or not path.exists():
            raise PathDoesntExist(str(path), self.name)
        self.current_index = 0
        with path.open("r") as file:
            loaded_json = json.load(file)
            assert loaded_json.get("data", None) is not None
            self.unit = loaded_json.get("unit", "")
            self.data = loaded_json.get("data", {})

    def get_unit(self, output_number: int = 0) -> str:
        """Returns the unit read from the open file"""
        assert self._config.file_options[0] is not None
        self.__set_file(self._config.file_options[0].path)
        return self.unit

    def read(self) -> List[float]:
        """Read the current value from the file and increase current value by 1 or loop if too big

        Returns:
            self.data[current] (float): the current value from the file
        """
        current: int = self.current_index
        if self.current_index < len(self.data) - 1:
            self.current_index += 1
        else:
            self.current_index = 0
        self._buffer = [self.data[current]]
        return self._buffer

    def close(self) -> NoReturn:
        """Implements parent method because there is no device"""
        pass

    @staticmethod
    def get_name() -> str:
        return "Von Datei Lesen"
