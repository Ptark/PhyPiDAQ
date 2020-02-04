from abc import ABC
from typing import Final

from PyQt5.QtWidgets import QWidget

from ...model.item.AccelerationSensorItem import AccelerationSensorItem
from ...model.item.DistanceSensorItem import DistanceSensorItem
from ...model.item.ForceSensorItem import ForceSensorItem
from ...model.item.SensorItem import SensorItem
from ...model.item.TemperatureSensorItem import TemperatureSensorItem
from .WorkspaceItemView import WorkspaceItemView


sensor_path = "../resources/images/items/sensor/"


class SensorItemView(WorkspaceItemView, ABC):
    """Abstract class for displaying an item of a sensor on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    def __init__(self, parent: QWidget):
        self._model: SensorItem

        super().__init__(parent, [], self._model.get_output_ids(), True)


class TemperatureSensorItemView(SensorItemView):
    """Class for displaying an item of a temperature sensor on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = sensor_path + 'temperature.svg'

    def __init__(self, parent: QWidget):
        self._model: TemperatureSensorItem = TemperatureSensorItem()

        super().__init__(parent)


class ForceSensorItemView(SensorItemView):
    """Class for displaying an item of a force sensor on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = sensor_path + 'force.svg'

    def __init__(self, parent: QWidget):
        self._model: ForceSensorItem = ForceSensorItem()

        super().__init__(parent)


class DistanceSensorItemView(SensorItemView):
    """Class for displaying an item of a distance sensor on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = sensor_path + 'distance.svg'

    def __init__(self, parent: QWidget):
        self._model: DistanceSensorItem = DistanceSensorItem()

        super().__init__(parent)


class AccelerationSensorItemView(SensorItemView):
    """Class for displaying an item of an acceleration sensor on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = sensor_path + 'acceleration.svg'

    def __init__(self, parent: QWidget):
        self._model: AccelerationSensorItem = AccelerationSensorItem()

        super().__init__(parent)
