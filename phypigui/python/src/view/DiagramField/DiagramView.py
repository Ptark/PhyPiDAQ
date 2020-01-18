from PyQt5.QtWidgets import QSizePolicy
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import random

from python.src.model.item import DiagramItem


class DiagramView(FigureCanvas):

    def __init__(self, parent, diagram: DiagramItem):
        self.diagram = diagram
        self.data = []
        fig = Figure(figsize=(4, 5), dpi=70)
        super().__init__(fig)
        FigureCanvas.__init__(self, fig)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("self.diagram.name")  # self.diagram._name
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def update_diagram(self, data: float):
        self.data.append(data)
        self.ax.plot(self.data, "r")
        self.draw()


