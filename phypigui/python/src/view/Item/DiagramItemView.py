from abc import ABC
from typing import Final

from PyQt5.QtWidgets import QWidget

from ..Item.WorkspaceItemView import WorkspaceItemView


diagram_path = "../resources/images/items/diagram/"


class DiagramItemView(WorkspaceItemView, ABC):
    """Abstract class for displaying an item of an diagram on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    frame_path: Final[str] = ""  # TODO: frame erstellen

    def __init__(self, parent: QWidget, num_of_inputs: int = 1):
        super().__init__(parent, num_of_inputs, 0)

        # TODO: Model & DiagramView in jeder Klasse selbst hinzufügen


class TimeDiagramItemView(DiagramItemView):
    """Class for displaying an item of an time diagram on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = diagram_path + 'time.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)


class BarDiagramItemView(DiagramItemView):
    """Class for displaying an item of an bar diagram on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = diagram_path + 'bar.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent, 3)


class DualDiagramItemView(DiagramItemView):
    """Class for displaying an item of an dual diagram on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = diagram_path + 'dual.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent, 2)
