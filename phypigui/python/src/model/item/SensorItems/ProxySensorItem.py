from pathlib import Path
from typing import List
import os
import json

from .SensorItem import SensorItem
from ...config.ConfigModel import ConfigModel
from ...config.FileOption import FileOption


class ProxySensorItem(SensorItem):
    """This class models a proxy sensor which reads from a file"""

    def __init__(self):
        """Initialize"""
        self.unit: str = ""
        self.data: List[float] = []
        self.current_index: int = 0
        # self.readout_rate: int = 0
        # Config
        start_path: str = str(Path(".").resolve()) + "/phypigui/python/resources/data/"
        config: ConfigModel = ConfigModel()
        config.add_file_option(FileOption("Dateipfad", "Der Dateipfad der\neinzulesenden Datei",
                                          FileOption.EXISTINGFILE, "PhyPiGUI-Dateien", ["ppg"], Path(start_path)))

        name: str = "Von Datei Lesen"
        description: str = "Lädt Einheit und Daten aus einer Datei und gibt sie aus."
        super().__init__(name, description, config, 1, None)

    def set_file(self, path: Path):
        """Sets file, unit and data if the given path leads to a valid json file"""
        # self.readout_rate = 0
        self.current_index = 0
        file = path.open("r")
        loaded_json: dict = json.load(file)
        file.close()
        unit: str = loaded_json.get("unit", "")
        # readout_rate: float = loaded_json.get("readout_rate", 0)
        data_json: List[float] = loaded_json.get("data", None)
        # assert valid data format
        # assert readout_rate is not 0
        assert data_json is not None
        # set attributes
        self.unit = unit
        # self.readout_rate = readout_rate
        self.data = data_json

    def get_unit(self, output_number: int = 0) -> str:
        """Returns the unit read from the open file"""
        assert self._config.file_options[0] is not None
        self.set_file(self._config.file_options[0].path)
        # assert self.unit != ""
        return self.unit
        # return unit read from file

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
        return [self.data[current]]

    @staticmethod
    def get_name() -> str:
        return "Von Datei Lesen"
