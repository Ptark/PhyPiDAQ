from abc import ABC
from typing import Final

from PyQt5.QtWidgets import QWidget

from .WorkspaceItemView import WorkspaceItemView


operator_path = "../resources/images/items/operator/"


class OperatorItemView(WorkspaceItemView, ABC):
    """Abstract class for displaying an item of an operator on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    frame_path: Final[str] = ""  # TODO: frame erstellen

    def __init__(self, parent: QWidget, num_of_inputs: int = 2, num_of_outputs: int = 1):
        super().__init__(parent, num_of_inputs, num_of_outputs)

        # TODO: Model in jeder Klasse selbst hinzufügen


class AdditionOperatorItemView(OperatorItemView):
    """Class for displaying an item of an addition operator on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = operator_path + 'addition.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)


class SubtractionOperatorItemView(OperatorItemView):
    """Class for displaying an item of an subtraction operator on the workspace

        Attributes (QWidget):
            parent: A parent widget.
    """
    icon_path: Final[str] = operator_path + 'subtraction.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)


class MultiplicationOperatorItemView(OperatorItemView):
    """Class for displaying an item of an multiplication operator on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = operator_path + 'multiplication.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)


class DivisionOperatorItemView(OperatorItemView):
    """Class for displaying an item of an division operator on the workspace

        Attributes:
            parent: A parent widget.
    """
    icon_path: Final[str] = operator_path + 'division.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)


class AbsoluteOperatorItemView(OperatorItemView):
    """Class for displaying an item of an absolute operator on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: Final[str] = operator_path + 'absolute.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent, 1)
