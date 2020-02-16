from ...config.BoolOption import BoolOption
from ...config.NumOption import NumOption
from ...config.ConfigModel import ConfigModel
from ..DiagramItems.DiagramItem import DiagramItem


class DualDiagramItem(DiagramItem):
    """This class models a plot diagram item"""

    def __init__(self):
        """Initialising a DualDiagramItem object"""
        name: str = "2D-Diagramm"
        description = "Stellt die gemessenen Daten als 2D-Diagramm dar"
        config = ConfigModel()
        config.add_num_option(NumOption("x-Achsen Minimum", '', -10.0))
        config.add_num_option(NumOption("x-Achsen Maximum", '', 10.0))
        config.add_num_option(NumOption("y-Achsen Minimum", '', -10.0))
        config.add_num_option(NumOption("y-Achsen Maximum", '', 10.0))
        config.add_num_option(NumOption("Maximale Anzahl an Punkten", '', 10, min=1, max=40, decimals=0))
        config.add_bool_option(BoolOption("Dynamische Achsenabschnitte", "Die Minima und Maxima werden nicht mehr beachtet", True))
        config.add_bool_option(BoolOption("Punkte verbinden", '', True))

        super().__init__(name, description, config, 2)

    @staticmethod
    def get_name() -> str:
        return "2D-Diagramm"
