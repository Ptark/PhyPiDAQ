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
        self.__unit: str = ""
        self.__read_out_rate = SensorItem.MIN_READ_OUT_RATE
        self.__data: List[float] = []
        self.__current_index: int = -1
        # Config
        start_path: str = str(Path(".").resolve()) + "/phypigui/python/resources/data/"
        config: ConfigModel = ConfigModel()
        config.add_file_option(FileOption("Dateipfad", "Der Dateipfad der\neinzulesenden Datei",
                                          FileOption.EXISTINGFILE, "PhyPiGUI-Dateien", ["ppg"], Path(start_path)))

        pins: List[int] = []

        name: str = "Von Datei Lesen"
        description: str = "Lädt Einheit und Daten aus einer Datei und gibt sie aus"
        super().__init__(name, description, config, 1, pins, None)

    def __set_file(self, path: Path):
        """Sets file, unit and data if the given path leads to a valid json file"""
        if path is None or not path.exists():
            raise PathDoesntExist(str(path), self._name)
        self.__current_index = 0
        with path.open("r") as file:
            loaded_json = json.load(file)
            assert loaded_json.get("data", None) is not None
            self.__unit = loaded_json.get("unit", "")
            try:
                self.__read_out_rate = loaded_json.get("rate")
            except Exception:
                self.__read_out_rate = SensorItem.MIN_READ_OUT_RATE
            self.__data = loaded_json.get("data", {})

    def get_unit(self, output_number: int = 0) -> str:
        """Returns the unit read from the open file"""
        assert self._config.file_options[0] is not None
        self.__set_file(self._config.file_options[0].path)
        return self.__unit

    def read(self) -> List[float]:
        """Read the current value from the file and increase current value by 1 or loop if too big

        Returns:
            self.data[current] (float): the current value from the file
        """

        if len(self.__data) != 0:
            read_time: int = int(time.time() * 1000)
            read_diff: int = read_time - self._last_read_time
            increment: int = round(read_diff / self.__read_out_rate)
            if increment > 1:
                self._last_read_time = read_time
                self.__current_index += increment
                self.__current_index %= len(self.__data)
                self._buffer = [self.__data[self.__current_index]]
            return self._buffer
        return [0]

    def close(self) -> NoReturn:
        """Implements parent method because there is no device"""
        pass

    @staticmethod
    def get_name() -> str:
        return "Von Datei Lesen"
