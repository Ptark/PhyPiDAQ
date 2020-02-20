from ...config.ConfigModel import ConfigModel
from ..diagrams.DiagramItem import DiagramItem


class ThreeDimDiagramItem(DiagramItem):
    """This class models a plot diagram item"""

    def __init__(self):
        """Initialising a ThreeDimDiagramItem object"""
        name: str = "3D-Diagramm"
        description = "Stellt die gemessenen Daten als 3D-Diagramm dar"
        config = ConfigModel()

        super().__init__(name, description, config, 3)

    @staticmethod
    def get_name() -> str:
        return "3D-Diagramm"
