import time
import json
from pathlib import Path
from typing import Dict, List

from ..SensorItems.SensorItem import SensorItem
from ...config.ConfigModel import ConfigModel
from ..DiagramItems.DiagramItem import DiagramItem


class WriteToFileItem(DiagramItem):
    """This class models a write to file item"""

    def __init__(self):
        """Initialising a WriteToFileItem object"""
        name: str = "In Datei schreiben"
        config: ConfigModel = ConfigModel()
        description: str = "Schreibt die gemessenen Daten in eine Datei " \
                           "und speichert diese am Ende des Messdurchlaufes ab"
        dir_path = Path('.')
        self.dir_path: str = str(dir_path.resolve()) + "/phypigui/python/resources/data/"
        self.path: str = ""
        self.loaded_json: dict = {}
        super().__init__(name, description, config, 1)

    def calculate_functions(self) -> bool:
        """Override method in superclass to add path creation of file"""
        success = super().calculate_functions()
        if success:
            self.path = self.dir_path + self._unit[0] + str(time.time()) + ".ppg"
            self.loaded_json = {
                "unit": self._unit[0],
                "data": []
            }
        return success

    def calculate(self, sensor_data: Dict[SensorItem, List[float]]) -> bool:
        """Override method in superclass to add writing to file"""
        success = super().calculate(sensor_data)
        if success:
            self.loaded_json["data"].append(self.data[0])
        return success

    def stop(self):
        """Override method in superclass. Write accumulated json to file"""
        with open(self.path, "w+") as file:
            json.dump(self.loaded_json, file)

    @staticmethod
    def get_name() -> str:
        return "In Datei schreiben"


