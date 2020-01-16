from typing import Final

from PyQt5.QtWidgets import QWidget

from .WorkspaceItemView import WorkspaceItemView


sensor_path = "../resources/images/icons/sensor/"


class SensorItemView(WorkspaceItemView):
    FRAME_PATH: Final[str] = ""  # TODO: frame erstellen

    def __init__(self, parent: QWidget):
        super().__init__(parent)

        # TODO: Model in jeder Klasse selbst hinzufügen


class TemperatureSensorItemView(SensorItemView):
    icon_path: str = sensor_path + 'temperature.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)


class ForceSensorItemView(SensorItemView):
    icon_path: str = sensor_path + 'force.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)


class DistanceSensorItemView(SensorItemView):
    icon_path: str = sensor_path + 'distance.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)


class AccelerationSensorItemView(SensorItemView):
    icon_path: str = sensor_path + 'acceleration.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)
