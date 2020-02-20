from ...config.BoolOption import BoolOption
from ...config.NumOption import NumOption
from ...config.ConfigModel import ConfigModel
from ..diagrams.DiagramItem import DiagramItem


class BarDiagramItem(DiagramItem):
    """This class models a bar diagram item"""

    def __init__(self):
        """Initialising a BarDiagramItem object"""
        name: str = "Balkendiagramm"
        config: ConfigModel = ConfigModel()
        description: str = "Stellt die gemessenen Daten als Balkendiagramm dar"
        config.add_num_option(NumOption("y-Achsen Minimum", '', 0.0))
        config.add_num_option(NumOption("y-Achsen Maximum", '', 10.0))
        config.add_bool_option(BoolOption("Dynamische y-Achse", "Das Minimum und Maximum wird nicht mehr beachtet", True))

        super().__init__(name, description, config, 3)

    @staticmethod
    def get_name() -> str:
        return "Balkendiagramm"
