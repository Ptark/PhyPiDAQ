import os
import time
import json
from pathlib import Path
from typing import Dict, List, NoReturn

from ..sensors.SensorItem import SensorItem
from ...config.ConfigModel import ConfigModel
from ...config.FileOption import FileOption
from ..diagrams.DiagramItem import DiagramItem


class WriteToFileItem(DiagramItem):
    """This class models a write to file item"""

    def __init__(self):
        """Initialising a WriteToFileItem object"""
        self.path: str = ""
        self.loaded_json: dict = {}

        name: str = "In Datei schreiben"
        description: str = "Schreibt die gemessenen Daten in eine Datei " \
                           "und speichert diese am Ende des Messdurchlaufes ab"

        dir_path: str = str(Path(".").resolve()) + "/phypigui/python/resources/data/"
        config: ConfigModel = ConfigModel()
        config.add_file_option(FileOption("Speicherpfad", "Ordner, indem die\nAuslesedatei erstellt wird",
                                          FileOption.DIR, "", None, Path(dir_path)))
        super().__init__(name, description, config, 1)

    def calculate_functions(self) -> NoReturn:
        """Override method in superclass to add path creation of file"""
        super().calculate_functions()
        self.path = str(self._config.file_options[0].path) + os.path.sep + self._unit[0] + str(time.time()) + ".ppg"
        self.loaded_json = {
            "unit": self._unit[0],
            "data": []
        }

    def calculate(self, sensor_data: Dict[SensorItem, List[float]]) -> NoReturn:
        """Override method in superclass to add writing to file"""
        super().calculate(sensor_data)
        self.loaded_json["data"].append(self._data[0])

    def stop(self):
        """Override method in superclass. Write accumulated json to file"""
        with open(self.path, "w+") as file:
            json.dump(self.loaded_json, file)

    @staticmethod
    def get_name() -> str:
        return "In Datei schreiben"


