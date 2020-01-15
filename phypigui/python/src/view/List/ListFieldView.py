from typing import NoReturn

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout


class ListFieldView(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.__tab = QTabWidget()
        self.init_ui()

    def init_ui(self) -> NoReturn:
        self.__tab.setElideMode(Qt.ElideRight)

        self.__tab.addTab(QWidget(), "&Sensoren")
        self.__tab.addTab(QWidget(), "&Operatoren")
        self.__tab.addTab(QWidget(), "&Diagramme")

        layout = QVBoxLayout()
        layout.addWidget(self.__tab)
        self.setLayout(layout)
