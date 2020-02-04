from abc import ABC
from typing import Final

from PyQt5.QtWidgets import QWidget

from ...model.item.OperatorItem import OperatorItem, AdditionOperatorItem, SubtractionOperatorItem, \
    MultiplicationOperatorItem, DivisionOperatorItem, AbsoluteOperatorItem
from .WorkspaceItemView import WorkspaceItemView


operator_path = "../resources/images/items/operator/"


class OperatorItemView(WorkspaceItemView, ABC):
    """Abstract class for displaying an item of an operator on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    def __init__(self, parent: QWidget):
        self._model: OperatorItem

        super().__init__(parent, self._model.get_input_ids(), self._model.get_output_ids())


class AdditionOperatorItemView(OperatorItemView):
    """Class for displaying an item of an addition operator on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = operator_path + 'addition.svg'

    def __init__(self, parent: QWidget):
        self._model: AdditionOperatorItem = AdditionOperatorItem()

        super().__init__(parent)


class SubtractionOperatorItemView(OperatorItemView):
    """Class for displaying an item of an subtraction operator on the workspace

        Attributes (QWidget):
            parent: A parent widget.
    """
    icon_path: Final[str] = operator_path + 'subtraction.svg'

    def __init__(self, parent: QWidget):
        self._model: SubtractionOperatorItem = SubtractionOperatorItem()

        super().__init__(parent)


class MultiplicationOperatorItemView(OperatorItemView):
    """Class for displaying an item of an multiplication operator on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = operator_path + 'multiplication.svg'

    def __init__(self, parent: QWidget):
        self._model: MultiplicationOperatorItem = MultiplicationOperatorItem()

        super().__init__(parent)


class DivisionOperatorItemView(OperatorItemView):
    """Class for displaying an item of an division operator on the workspace

        Attributes:
            parent: A parent widget.
    """
    icon_path: Final[str] = operator_path + 'division.svg'

    def __init__(self, parent: QWidget):
        self._model: DivisionOperatorItem = DivisionOperatorItem()

        super().__init__(parent)


class AbsoluteOperatorItemView(OperatorItemView):
    """Class for displaying an item of an absolute operator on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = operator_path + 'absolute.svg'

    def __init__(self, parent: QWidget):
        self._model: AbsoluteOperatorItem = AbsoluteOperatorItem()

        super().__init__(parent)
