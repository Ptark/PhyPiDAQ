from typing import Final

from PyQt5.QtWidgets import QWidget, QLabel

from ..Item.WorkspaceItemView import WorkspaceItemView


class DiagramItemView(WorkspaceItemView):
    FRAME_PATH: Final[str] = ""  # TODO: frame erstellen

    def __init__(self, parent: QWidget):
        super().__init__(parent)

        # TODO: Model & DiagramView in jeder Klasse selbst hinzufügen
        # TODO: Icons


class TimeDiagramItemView(DiagramItemView):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        lab = QLabel("Time", self)


class BarDiagramItemView(DiagramItemView):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        lab = QLabel("Bar", self)


class DualDiagramItemView(DiagramItemView):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        lab = QLabel("Dual", self)
