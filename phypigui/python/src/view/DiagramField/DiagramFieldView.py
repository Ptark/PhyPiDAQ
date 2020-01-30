from typing import List, NoReturn

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from PyQt5.QtGui import QCloseEvent, QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QDialog, QGridLayout
from numpy import random

# from python.src.model.item import DiagramItem
from .DiagramView import DiagramView
from .StartButtonView import StartButtonView


class DiagramFieldView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.__list: List[DiagramView] = []
        self.__dialog = None

        self.__vertical_layout = QVBoxLayout()
        self.__horizontal_layout = QHBoxLayout()
        self.__init_max_button()
        self.__horizontal_layout.addWidget(StartButtonView(self))
        self.__horizontal_layout.addStretch(1)
        self.__horizontal_layout.addWidget(self.__maximize_button)

        self.__vertical_layout.addLayout(self.__horizontal_layout)
        self.__vertical_layout.addStretch(1)
        self.init_example_diagrams()
        self.setLayout(self.__vertical_layout)
        self.__maximize_button.clicked.connect(self.on_click)

    def init_example_diagrams(self):
        a = DiagramView(self)
        b = DiagramView(self)
        c = DiagramView(self)

        self.add_diagram(a)
        self.add_diagram(b)
        self.add_diagram(c)
        self.__test_diag(a)
        self.__test_diag(b)
        # self.delete_diagram(c)
        # self.delete_diagram(b)

    def add_diagram(self, diagram: DiagramView) -> NoReturn:
        if len(self.__list) < 3:
            self.__list.append(diagram)
            self.__vertical_layout.addWidget(diagram)

    def delete_diagram(self, diagram: DiagramView) -> NoReturn:
        self.__list.remove(diagram)
        self.__vertical_layout.removeWidget(diagram)

    def __test_diag(self, diag: DiagramView):
        for _ in range(50):
            diag.update_diagram(random.random())

    def on_click(self):
        self.__dialog = Dialog(self.__list)
        self.__dialog.close_signal.connect(self.__update_diagrams)
        self.__maximize_button.clearFocus()

    def __init_max_button(self):
        icon = QtGui.QIcon("../resources/images/buttons/maximize.svg")

        self.__maximize_button = QPushButton()
        self.__maximize_button.setFixedSize(31, 31)
        self.__maximize_button.setIcon(icon)

    @pyqtSlot()
    def __update_diagrams(self):
        for diagram in self.__list:
            self.__vertical_layout.addWidget(diagram)


class Dialog(QWidget):
    close_signal = pyqtSignal()

    def __init__(self, list: List[DiagramView]):
        super().__init__()

        self.__init_ui(list)

    def __init_ui(self, list: List[DiagramView]):
        minimize_button = QtWidgets.QPushButton()
        minimize_button.setIcon(QIcon("../resources/images/buttons/minimize.svg"))
        minimize_button.setFixedSize(31, 31)
        minimize_button.clicked.connect(self.__minimize_on_click)

        horizontal_layout = QHBoxLayout()
        for diagram in list:
            horizontal_layout.addWidget(diagram)

        central_layout = QGridLayout()
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(horizontal_layout)
        central_layout.addWidget(central_widget, 1, 0)
        central_layout.addWidget(minimize_button, 0, 1)

        self.setLayout(central_layout)

        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.showMaximized()

    def __minimize_on_click(self):
        self.close()

    def closeEvent(self, event: QCloseEvent):
        self.close_signal.emit()
