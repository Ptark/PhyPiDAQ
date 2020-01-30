from abc import ABC
from typing import Final

from PyQt5.QtWidgets import QWidget

from ...model.item.DiagramItem import DiagramItem, TimeDiagramItem, BarDiagramItem
from ..Item.WorkspaceItemView import WorkspaceItemView


diagram_path = "../resources/images/items/diagram/"


class DiagramItemView(WorkspaceItemView, ABC):
    """Abstract class for displaying an item of an diagram on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    def __init__(self, parent: QWidget, num_of_inputs: int = 1):
        super().__init__(parent, num_of_inputs, 0)

        self._model: DiagramItem = None


class TimeDiagramItemView(DiagramItemView):
    """Class for displaying an item of an time diagram on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = diagram_path + 'time.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self._model: TimeDiagramItem = TimeDiagramItem()


class BarDiagramItemView(DiagramItemView):
    """Class for displaying an item of an bar diagram on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = diagram_path + 'bar.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent, 3)

        self._model: BarDiagramItem = BarDiagramItem()


class DualDiagramItemView(DiagramItemView):
    """Class for displaying an item of an dual diagram on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = diagram_path + 'dual.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent, 2)
        # TODO: DualDiagramItem im Model existiert noch nicht
        # self._model: DualDiagramItem = DualDiagramItem()
