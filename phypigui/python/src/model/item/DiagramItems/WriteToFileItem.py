import time
import json
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
        self.folder_path: str = "../../../../resources/data/"
        self.path: str = ""
        self.file = None
        super().__init__(name, description, config, 1)

    def calculate_functions(self) -> bool:
        """Override method in superclass to add path creation of file"""
        success = super().calculate_functions()
        if success:
            self.path = self.folder_path + str(time.time())
            file_stub = {
                "unit": self._unit[0],
                # "readout_rate": 100,
                "data": []
            }
            file = open(self.path, "w")
            file.write(json.dumps(file_stub))
            file.close()
        return success

    def calculate(self, sensor_data: Dict[SensorItem, List[float]]) -> bool:
        """Override method in superclass to add writing to file"""
        success = super().calculate(sensor_data)
        if success:
            file = open(self.path, "w")
            raw_json = file.read()
            loaded_json = json.loads(raw_json)
            loaded_json["data"].append(self._data[0])
            raw_json = json.dumps(loaded_json)
            file.write(raw_json)
            file.close()
        return success

    @staticmethod
    def get_name() -> str:
        return "In Datei schreiben"

