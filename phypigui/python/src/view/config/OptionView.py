from abc import ABC, abstractmethod
from PyQt5 import QtWidgets
from typing import NoReturn


class OptionView(QtWidgets.QWidget):

    def __init__(self, parent: QtWidgets.QWidget, name: str):
        super().__init__(parent)
        self._layout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout(self)
        self._name_label: QtWidgets.QLabel = QtWidgets.QLabel(name + ':', self)
        self._stretch: QtWidgets.QWidget = QtWidgets.QWidget(self)
        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        self._stretch.setMinimumWidth(10)
        self._layout.addWidget(self._name_label)
        self._layout.addWidget(self._stretch, 10)
