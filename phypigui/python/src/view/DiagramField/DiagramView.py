from typing import NoReturn, List

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5.QtWidgets import QSizePolicy

from ..View import View
from ...model.item import DiagramItem
from ...model.item.DiagramItem import BarDiagramItem, TimeDiagramItem, DualDiagramItem


class DiagramViewMeta(type(FigureCanvas), type(View)):
    pass


class DiagramView(FigureCanvas, View, metaclass=DiagramViewMeta):
    """the super class of Time diagram, bar diagram and Dual diagram"""
    def __init__(self, item: DiagramItem):
        fig = Figure(figsize=(4, 5), dpi=70)

        super().__init__(fig)

        self.__data = []
        self.__item: DiagramItem = item
        self.__item.attach(self)

        self.__ax = self.figure.add_subplot(111)
        self.__ax.set_title(self.__item.name)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def __update_diagram(self, data: float) -> NoReturn:
        self.__data.append(data)
        self.__ax.plot(self.__data, "r")
        self.draw()

    def update_view(self) -> NoReturn:
        self.__update_diagram(self.__item.data[0])


class TimeDiagram(DiagramView):
    """this class represents time diagram"""
    def __init__(self, item: TimeDiagramItem):
        """Initialising an DualDiagram object

         Args:
             item (DualDiagramItem): time plot diagram item
        """
        __fig = Figure(figsize=(4, 5), dpi=70)

        super().__init__(__fig)

        self.__data = []
        self.__item: DiagramItem = item
        self.__item.attach(self)

        self.__ax = self.figure.add_subplot(111)
        self.__ax.set_title(self.__item.name)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def __update_diagram(self, data: float) -> NoReturn:
        self.data.append(data)
        self.ax.plot(self.data, "r")
        self.draw()


class DualDiagram(DiagramView):
    """this class represents the dual diagram"""
    def __init__(self, item: DualDiagramItem):
        """Initialising an DualDiagram object

        Args:
            item (DualDiagramItem): plot diagram item
        """
        fig = Figure(figsize=(4, 5), dpi=70)
        super().__init__(fig)

        self.__data_1 = [1.1, 2.1]  # for testing purposes
        self.__data_2 = [2.1, 3.1]

        self.__item: DiagramItem = item
        self.__item.attach(self)

        self.__ax = self.figure.add_subplot(111)
        self.__ay = self.figure.add_subplot(111)

        self.__ax.set_title(self.__item.name)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.__ax.plot(self.data_1, "r")
        self.__ay.plot(self.data_2, "g")

        self.draw()

    def __update_diagram(self, data: List[float]) -> NoReturn:
        self.__data_1.append(data[0])
        self.__data_2.append(data[1])

        self.__ax.plot(self.data_1, "r")
        self.__ay.plot(self.data_2, "g")

        self.draw()


class BarDiagram(DiagramView):
    """this class represents a bar diagram """
    def __init__(self, item: BarDiagramItem):
        """Initialising an DualDiagram object

        Args:
                   item (DualDiagramItem): dual plot diagram item
        """
        fig = Figure(figsize=(4, 5), dpi=70)
        super().__init__(fig)

        self.__item: BarDiagramItem = item

        self.__item.attach(self)

        self.values = [1.1, 2.1, 3.1]  # for testing purposes
        self.labels = ["first input", "second input", "third input"]

        plt.bar(self.labels, self.values)
        plt.show()

    def __update_diagram(self, data: List[float]) -> NoReturn:
        self.values[0] = data[0]
        self.values[1] = data[1]
        self.values[2] = data[2]

        plt.show()
