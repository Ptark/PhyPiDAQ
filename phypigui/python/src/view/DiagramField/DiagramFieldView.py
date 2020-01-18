from typing import List, NoReturn

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from numpy import random

from python.src.model.item import DiagramItem
from python.src.view.DiagramField.DiagramView import DiagramView
from python.src.view.DiagramField.MaximizeButton import MaximizeButtonView


class DiagramFieldView(QWidget):
    list = []
    vertical_layout: QVBoxLayout = QVBoxLayout()

    def __init__(self, parent):
        super().__init__(parent)
        self.list: List[DiagramView]

        self.vertical_layout = QVBoxLayout()
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addStretch(2)

        self.maxButton = MaximizeButtonView(self)

        self.horizontal_layout.addWidget(self.maxButton)
        self.vertical_layout.addLayout(self.horizontal_layout)

        self.init_example_diagrams()
        self.setLayout(self.vertical_layout)

    def init_example_diagrams(self):
        a = DiagramView(self, DiagramItem.TimeDiagramItem)
        b = DiagramView(self, DiagramItem.TimeDiagramItem)
        c = DiagramView(self, DiagramItem.TimeDiagramItem)

        self.add_diagram(a)
        self.add_diagram(b)
        self.add_diagram(c)
        self.test_diag(a)
        self.test_diag(b)
        # self.delete_diagram(c)
        # self.delete_diagram(b)

    def add_diagram(self, diagram: DiagramView) -> NoReturn:
        if len(self.list) < 3:
            self.list.append(diagram)
            self.vertical_layout.addWidget(diagram)

    def delete_diagram(self, diagram: DiagramView) -> NoReturn:
        self.list.remove(diagram)
        self.vertical_layout.removeWidget(diagram)

    def test_diag(self, diag: DiagramView):
        for i in range(40):
            diag.update_diagram(random.random())
