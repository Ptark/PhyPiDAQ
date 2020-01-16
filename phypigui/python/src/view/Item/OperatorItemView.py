from typing import Final

from PyQt5.QtWidgets import QWidget, QLabel

from .WorkspaceItemView import WorkspaceItemView


class OperatorItemView(WorkspaceItemView):
    FRAME_PATH: Final[str] = ""  # TODO: frame erstellen

    def __init__(self, parent: QWidget):
        super().__init__(parent)

        # TODO: Model in jeder Klasse selbst hinzufügen
        # TODO: Icons


class AdditionOperatorItemView(OperatorItemView):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        lab = QLabel("Addition", self)


class SubtractionOperatorItemView(OperatorItemView):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        lab = QLabel("Subtraction", self)


class MultiplicationOperatorItemView(OperatorItemView):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        lab = QLabel("Multiplication", self)


class DivisionOperatorItemView(OperatorItemView):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        lab = QLabel("Division", self)


class AbsoluteOperatorItemView(OperatorItemView):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        lab = QLabel("Absolute", self)
