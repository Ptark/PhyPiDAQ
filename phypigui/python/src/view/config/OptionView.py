from PyQt5 import QtWidgets


class OptionView(QtWidgets.QWidget):

    def __init__(self, parent: QtWidgets.QWidget, name: str):
        super().__init__(parent)
        self.__label: QtWidgets.QLabel = QtWidgets.QLabel(name, self)
