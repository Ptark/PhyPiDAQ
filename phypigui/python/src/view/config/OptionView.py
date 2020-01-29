from abc import ABC, abstractmethod
from PyQt5 import QtWidgets, QtGui, QtCore
from typing import NoReturn, final


class OptionView(QtWidgets.QWidget):
    # style-sheet rgb value
    ERROR_COLOR: final(str) = 'rgb(255, 158, 158)'

    def __init__(self, parent: QtWidgets.QWidget, name: str):
        super().__init__(parent)
        # Group-box and its layout
        layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout(self)
        self.__box = QtWidgets.QGroupBox()
        layout.addWidget(self.__box)
        # Layout for the whole option
        self._option_layout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout(self.__box)
        # Label, which stores name of option
        self._name_label: QtWidgets.QLabel = QtWidgets.QLabel(name + ':', self)

        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        # Add label and stretch-widget to option-layout
        self._option_layout.addWidget(self._name_label, 0, QtCore.Qt.AlignLeft)
