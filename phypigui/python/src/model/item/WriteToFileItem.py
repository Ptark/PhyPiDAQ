from ..config.ConfigModel import ConfigModel
from .DiagramItem import DiagramItem


class WriteToFileItem(DiagramItem):
    """This class models a write to file item"""

    def __init__(self):
        """Initialising a WriteToFileItem object"""
        name: str = "In Datei schreiben"
        config: ConfigModel = ConfigModel()
        description: str = "Schreibt die gemessenen Daten in eine Datei " \
                           "und speichert diese am Ende des Messduchlaufes ab"
        super().__init__(name, description, config, 1)

    def set_file(self):
        pass

