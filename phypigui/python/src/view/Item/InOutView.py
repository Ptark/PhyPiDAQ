from PyQt5.QtWidgets import QWidget

from ..View import View


class InOutViewMeta(type(QWidget), type(View)):
    pass


class InOutView(QWidget, View, metaclass=InOutViewMeta):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
