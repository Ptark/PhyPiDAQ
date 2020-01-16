from typing import Final

from PyQt5.QtWidgets import QWidget

from ..Item.WorkspaceItemView import WorkspaceItemView


diagram_path = "../resources/images/icons/diagram/"


class DiagramItemView(WorkspaceItemView):
    FRAME_PATH: Final[str] = ""  # TODO: frame erstellen

    def __init__(self, parent: QWidget):
        super().__init__(parent)

        # TODO: Model & DiagramView in jeder Klasse selbst hinzufügen


class TimeDiagramItemView(DiagramItemView):
    icon_path: str = diagram_path + 'time.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)


class BarDiagramItemView(DiagramItemView):
    icon_path: str = diagram_path + 'bar.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)


class DualDiagramItemView(DiagramItemView):
    icon_path: str = diagram_path + 'dual.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)
