from ...config.ConfigModel import ConfigModel
from ..DiagramItems.DiagramItem import DiagramItem


class DualDiagramItem(DiagramItem):
    """This class models a plot diagram item"""

    def __init__(self):
        """Initialising a DualDiagramItem object"""
        name: str = "2D-Diagramm"
        description = "Stellt die gemessenen Daten als 2D-Diagramm dar"
        config = ConfigModel()

        super().__init__(name, description, config, 2)