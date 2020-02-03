from abc import ABC
from typing import Final, NoReturn

from PyQt5.QtWidgets import QWidget

from ..DiagramField.DiagramFieldView import DiagramFieldView
from ..DiagramField.DiagramView import DiagramView
from ...model.item.DiagramItem import DiagramItem, TimeDiagramItem, BarDiagramItem, DualDiagramItem
from ..Item.WorkspaceItemView import WorkspaceItemView


diagram_path = "../resources/images/items/diagram/"


class DiagramItemView(WorkspaceItemView, ABC):
    """Abstract class for displaying an item of an diagram on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    def __init__(self, parent: QWidget):
        self._diagram = DiagramView()
        DiagramFieldView.add_diagram(self._diagram)

        self._model: DiagramItem

        super().__init__(parent, self._model.get_count_of_inputs(), 0)


    def delete(self) -> NoReturn:
        DiagramFieldView.delete_diagram(self._diagram)
        super().delete()


class TimeDiagramItemView(DiagramItemView):
    """Class for displaying an item of an time diagram on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = diagram_path + 'time.svg'

    def __init__(self, parent: QWidget):
        self._model: TimeDiagramItem = TimeDiagramItem()

        super().__init__(parent)


class BarDiagramItemView(DiagramItemView):
    """Class for displaying an item of an bar diagram on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = diagram_path + 'bar.svg'

    def __init__(self, parent: QWidget):
        self._model: BarDiagramItem = BarDiagramItem()

        super().__init__(parent)


class DualDiagramItemView(DiagramItemView):
    """Class for displaying an item of an dual diagram on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = diagram_path + 'dual.svg'

    def __init__(self, parent: QWidget):
        self._model: DualDiagramItem = DualDiagramItem()

        super().__init__(parent)
