from typing import List
import os
import json

from ..config.NumOption import NumOption
from ..item.SensorItem import SensorItem
from ..config.ConfigModel import ConfigModel
from ..config.FileOption import FileOption


class ProxySensorItem(SensorItem):
    """This class models a proxy sensor which reads from a file"""

    def __init__(self):
        """Initialize"""
        self.unit: str = ""
        self.data: List[float] = []
        self.current_value: int = 0
        name: str = "Proxysensor"
        description: str = "Der Proxysensor lädt Einheit und Daten aus einer Datei und gibt sie aus."
        config: ConfigModel = ConfigModel()
        config.add_file_option(FileOption(name, description))  # TODO Optionsbeschreibung
        config.add_num_option(NumOption("Ausleserate", "", 0))
        super().__init__(name, description, config, 1, None)

    def set_file(self, path: str):
        """Sets file, unit and data if the given path leads to a valid json file"""
        assert(os.path.isfile(path))
        unit = ""
        self._config.num_options[0].number = 0
        self.current_value = 0
        file = open(path, "r")
        raw_json: str = file.read()
        file.close()
        loaded_json: dict = json.loads(raw_json)

        new_unit: str = loaded_json.get("unit", "")
        readout_rate: float = loaded_json.get("readout_rate", 0)
        data_json: List[float] = loaded_json.get("data", None)
        assert new_unit is not ""
        assert readout_rate is not 0
        assert data_json is not None
        unit = new_unit
        self._config.num_options[0].number = readout_rate
        data = data_json

    def get_unit(self, output_number: int = 0) -> str:
        """Returns the unit read from the open file"""
        assert self._config.file_options[0] is not None
        assert self.unit is not ""
        return self.unit
        # return unit read from file

    def read(self) -> float:
        """Read the current value from the file and increase current value by 1 or loop if too big

        Returns:
            self.data[current] (float): the current value from the file
        """
        current: int = self.current_value
        if self.current_value < len(self.data) - 1:
            self.current_value += 1
        else:
            self.current_value = 0
        return self.data[current]
