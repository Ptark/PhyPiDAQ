from typing import List, NoReturn

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from numpy import random

# from python.src.model.item import DiagramItem
from .DiagramView import DiagramView
from .MaximizeButton import MaximizeButtonView
from .StartButtonView import StartButtonView


class DiagramFieldView(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.__list: List[DiagramView]

        self.__vertical_layout = QVBoxLayout()
        self.__horizontal_layout = QHBoxLayout()

        self.__horizontal_layout.addWidget(StartButtonView(self))
        self.__horizontal_layout.addStretch(1)
        self.__horizontal_layout.addWidget(MaximizeButtonView(self))

        self.__vertical_layout.addLayout(self.__horizontal_layout)
        self.__vertical_layout.addStretch(1)

        # self.init_example_diagrams()
        self.setLayout(self.__vertical_layout)

    def init_example_diagrams(self):
        a = DiagramView(self, DiagramItem.TimeDiagramItem)
        b = DiagramView(self, DiagramItem.TimeDiagramItem)
        c = DiagramView(self, DiagramItem.TimeDiagramItem)

        self.add_diagram(a)
        self.add_diagram(b)
        self.add_diagram(c)
        self.__test_diag(a)
        self.__test_diag(b)
        # self.delete_diagram(c)
        # self.delete_diagram(b)

    def add_diagram(self, diagram: DiagramView) -> NoReturn:
        if len(self.list) < 3:
            self.__list.append(diagram)
            self.__vertical_layout.addWidget(diagram)

    def delete_diagram(self, diagram: DiagramView) -> NoReturn:
        self.__list.remove(diagram)
        self.__vertical_layout.removeWidget(diagram)

    def __test_diag(self, diag: DiagramView):
        for i in range(40):
            diag.update_diagram(random.random())
