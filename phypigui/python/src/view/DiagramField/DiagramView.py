import random

from PyQt5.QtWidgets import QSizePolicy
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from python.src.model.item import DiagramItem


class DiagramView(FigureCanvas):
    diagram: DiagramItem

    def __init__(self, parent):
        fig = Figure(figsize=(4, 5), dpi=70)
        super().__init__(fig)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.plot()

    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'b')
        ax.set_title("example")
        self.draw()

    def update_diagram(self, data):
        pass