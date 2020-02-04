from ..item.SensorItem import SensorItem
from ..config.ConfigModel import ConfigModel
from ..config.FileOption import FileOption

class ProxySensorItem(SensorItem):
    """This class models a proxy sensor which reads from a file"""

    def __init__(self):
        """Initialize"""
        name: str = "ProxySensor"
        description: str = "Der Proxysensor lädt Einheit und Daten aus einer Datei und gibt sie aus."

        config: ConfigModel = ConfigModel()
        config.add_file_option(FileOption(name, description))
        super().__init__(name, description, config, 1, None)
