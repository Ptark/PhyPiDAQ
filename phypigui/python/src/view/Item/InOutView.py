from PyQt5.QtWidgets import QWidget

from ..View import View


class InOutView(QWidget, View):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
