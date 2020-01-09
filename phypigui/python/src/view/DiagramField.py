from PyQt5.QtWidgets import QWidget, QPushButton
from matplotlib.backends.backend_template import FigureCanvas

from PhyPiDAQ.phypigui.python.src.model.item import DiagramItem


class DiagramView(FigureCanvas):
    diagram: DiagramItem

    def update_diagram(self, data):
        pass


class DiagramFieldView(QWidget):
    list = []  # List of DiagramView

    def add_diagram(self, diagram: DiagramView) -> None:
        list.append(diagram)

    def delete_diagram(self, diagram: DiagramView) -> None:
        list.remove(diagram)


class MaximizeButtonView(QPushButton):
    def on_click(self):
        pass
