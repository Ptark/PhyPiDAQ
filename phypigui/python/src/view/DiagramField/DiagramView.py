from abc import ABC, abstractmethod
from typing import NoReturn, List

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5.QtWidgets import QSizePolicy

from ..View import View
from ...model.item.DiagramItem import DiagramItem, TimeDiagramItem, BarDiagramItem, DualDiagramItem


class DiagramViewMeta(type(FigureCanvas), type(View)):
    pass


class DiagramView(FigureCanvas, View, ABC, metaclass=DiagramViewMeta):
    """the super class of Time diagram, bar diagram and Dual diagram"""
    def __init__(self, item: DiagramItem):
        fig = Figure(figsize=(4, 5), dpi=70)

        super().__init__(fig)

        self._item: DiagramItem = item
        self._item.attach(self)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    @abstractmethod
    def _update_diagram(self, data: List[float]) -> NoReturn:
        pass

    def update_view(self) -> NoReturn:
        self._update_diagram(self._item.data)


class TimeDiagram(DiagramView):
    """this class represents time diagram"""
    def __init__(self, item: TimeDiagramItem):
        """Initialising an DualDiagram object

         Args:
             item (DualDiagramItem): time plot diagram item
        """
        super().__init__(item)

        self.__data = []

        self.__ax = self.figure.add_subplot(111)

        self.__ax.set_title(self._item.name)

    def _update_diagram(self, data: List[float]) -> NoReturn:
        if len(self.__data) > 20:
            self.__data.pop(0)
        self.__data.append(data[0])

        self.__ax.clear()
        self.__ax.plot(self.__data)
        self.draw()


class DualDiagram(DiagramView):
    """this class represents the dual diagram"""
    def __init__(self, item: DualDiagramItem):
        """Initialising an DualDiagram object

        Args:
            item (DualDiagramItem): plot diagram item
        """
        super().__init__(item)

        self.__data_x = []
        self.__data_y = []

        self.__ax = self.figure.add_subplot(111)

        self.__ax.set_title(self._item.name)

    def _update_diagram(self, data: List[float]) -> NoReturn:
        if len(self.__data_x) > 10:
            self.__data_x.pop(0)
            self.__data_y.pop(0)
        self.__data_x.append(data[0])
        self.__data_y.append(data[1])

        self.__ax.clear()
        self.__ax.plot(self.__data_x, self.__data_y)
        self.draw()


class BarDiagram(DiagramView):
    """this class represents a bar diagram """
    def __init__(self, item: BarDiagramItem):
        """Initialising an DualDiagram object

        Args:
                   item (DualDiagramItem): dual plot diagram item
        """
        super().__init__(item)

        self.__data = [0.0, 0.0, 0.0]
        self.__labels = ["first input", "second input", "third input"]

        self.__ax = self.figure.add_subplot(111)

        self.__ax.set_title(self._item.name)

        self.__ax.bar(self.__labels, self.__data)
        self.draw()

    def _update_diagram(self, data: List[float]) -> NoReturn:
        for i in range(0, 3):
            self.__data[i] = data[i]

        self.__ax.clear()
        self.__ax.bar(self.__labels, self.__data)
        self.draw()

