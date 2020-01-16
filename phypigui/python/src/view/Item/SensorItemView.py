from typing import Final

from PyQt5.QtWidgets import QWidget, QLabel

from .WorkspaceItemView import WorkspaceItemView


class SensorItemView(WorkspaceItemView):
    FRAME_PATH: Final[str] = ""  # TODO: frame erstellen

    def __init__(self, parent: QWidget):
        super().__init__(parent)

        # TODO: Model in jeder Klasse selbst hinzufügen
        # TODO: Icons


class TemperatureSensorItemView(SensorItemView):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        lab = QLabel("Temperature", self)


class ForceSensorItemView(SensorItemView):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        lab = QLabel("Force", self)


class DistanceSensorItemView(SensorItemView):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        lab = QLabel("Distance", self)


class AccelerationSensorItemView(SensorItemView):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        lab = QLabel("Acceleration", self)