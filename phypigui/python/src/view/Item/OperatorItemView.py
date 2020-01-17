from abc import ABC
from typing import Final

from PyQt5.QtWidgets import QWidget

from .WorkspaceItemView import WorkspaceItemView


operator_path = "../resources/images/items/operator/"


class OperatorItemView(WorkspaceItemView, ABC):
    FRAME_PATH: Final[str] = ""  # TODO: frame erstellen

    def __init__(self, parent: QWidget, num_of_inputs: int = 2, num_of_outputs: int = 1):
        super().__init__(parent, num_of_inputs, num_of_outputs)

        # TODO: Model in jeder Klasse selbst hinzufügen


class AdditionOperatorItemView(OperatorItemView):
    icon_path: str = operator_path + 'addition.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)


class SubtractionOperatorItemView(OperatorItemView):
    icon_path: str = operator_path + 'subtraction.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)


class MultiplicationOperatorItemView(OperatorItemView):
    icon_path: str = operator_path + 'multiplication.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)


class DivisionOperatorItemView(OperatorItemView):
    icon_path: str = operator_path + 'division.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)


class AbsoluteOperatorItemView(OperatorItemView):
    icon_path: str = operator_path + 'absolute.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent, 1)
