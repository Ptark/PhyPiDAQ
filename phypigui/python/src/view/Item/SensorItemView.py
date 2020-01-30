from abc import ABC
from typing import Final

from PyQt5.QtWidgets import QWidget

from .WorkspaceItemView import WorkspaceItemView


sensor_path = "../resources/images/items/sensor/"


class SensorItemView(WorkspaceItemView, ABC):
    """Abstract class for displaying an item of a sensor on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    frame_path: Final[str] = ""  # TODO: frame erstellen

    def __init__(self, parent: QWidget, num_of_outputs: int = 1):
        super().__init__(parent, 0, num_of_outputs, True)

        # TODO: Model in jeder Klasse selbst hinzufügen


class TemperatureSensorItemView(SensorItemView):
    """Class for displaying an item of a temperature sensor on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = sensor_path + 'temperature.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)


class ForceSensorItemView(SensorItemView):
    """Class for displaying an item of a force sensor on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = sensor_path + 'force.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)


class DistanceSensorItemView(SensorItemView):
    """Class for displaying an item of a distance sensor on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = sensor_path + 'distance.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)


class AccelerationSensorItemView(SensorItemView):
    """Class for displaying an item of an acceleration sensor on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = sensor_path + 'acceleration.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)
