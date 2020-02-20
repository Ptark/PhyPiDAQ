from ...config.NumOption import NumOption
from ...config.ConfigModel import ConfigModel
from ..diagrams.DiagramItem import DiagramItem


class TimeDiagramItem(DiagramItem):
    """This class models a timing diagram item"""

    def __init__(self):
        """Initialising a TimeDiagramItem object"""
        name: str = "Zeitdiagramm"
        description = "Stellt die gemessenen Daten als Zeitdiagramm dar"
        config = ConfigModel()
        config.add_num_option(NumOption("Angezeigte Sekunden", '', 10.0, min=1.0, max=30.0))

        super().__init__(name, description, config, 1)

    @staticmethod
    def get_name() -> str:
        return "Zeitdiagramm"
