from PyQt5 import QtWidgets, QtCore
from typing import NoReturn, final


class OptionView(QtWidgets.QWidget):
    # style-sheet rgb value
    ERROR_COLOR: final(str) = 'rgb(255, 158, 158)'

    def __init__(self, parent: QtWidgets.QWidget, name: str, description: str):
        super().__init__(parent)
        # Group-box and its layout
        self.__box = QtWidgets.QGroupBox()
        if name == '':
            self.__box.setTitle(name)
        else:
            self.__box.setTitle(name + ':')
        layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.__box, 0, QtCore.Qt.AlignTop)
        # Layout for the whole option
        self._option_layout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout(self.__box)
        # Label, which stores name of option
        self._description_label: QtWidgets.QLabel = QtWidgets.QLabel(description, self)

        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        # Add description-label to option-layout
        self._option_layout.addWidget(self._description_label, 0, QtCore.Qt.AlignLeft)
