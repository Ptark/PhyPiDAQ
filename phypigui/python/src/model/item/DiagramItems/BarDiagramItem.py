from phypigui.python.src.model.config.ConfigModel import ConfigModel
from phypigui.python.src.model.item.DiagramItems.DiagramItem import DiagramItem


class BarDiagramItem(DiagramItem):
    """This class models a bar diagram item"""

    def __init__(self):
        """Initialising a BarDiagramItem object"""
        name: str = "Balkendiagramm"
        config: ConfigModel = ConfigModel()
        description: str = "Stellt die gemessenen Daten als Balkendiagramm dar"

        super().__init__(name, description, config, 3)