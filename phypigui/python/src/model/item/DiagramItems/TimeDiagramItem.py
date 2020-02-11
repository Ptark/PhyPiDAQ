from ...config.ConfigModel import ConfigModel
from ..DiagramItems.DiagramItem import DiagramItem


class TimeDiagramItem(DiagramItem):
    """This class models a timing diagram item"""

    def __init__(self):
        """Initialising a TimeDiagramItem object"""
        name: str = "Zeitdiagramm"
        description = "Stellt die gemessenen Daten als Zeitdiagramm dar"
        config = ConfigModel()

        super().__init__(name, description, config, 1)