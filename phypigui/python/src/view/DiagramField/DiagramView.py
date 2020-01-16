import random

from PyQt5.QtWidgets import QSizePolicy
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from python.src.model.item import DiagramItem


class DiagramView(FigureCanvas):

    def __init__(self, parent, diagram: DiagramItem):
        self.diagram = diagram
        fig = Figure(figsize=(4, 5), dpi=70)
        super().__init__(fig)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.plot()

    def plot(self):
        time = []
        data = []
        for i in range(-1, -21, -1):
            time.append(i)
        for i in range(1, 8, 1):
            data.append(i)
        ax = self.figure.add_subplot(111)
        ax.plot(data, "b")
        ax.set_title("example")  # self.diagram._name
        self.draw()

    def update_diagram(self, data: float):
        pass
