import time
from abc import ABC, abstractmethod
from typing import NoReturn, List

from matplotlib.axes import Subplot
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5.QtWidgets import QSizePolicy

from ..Translator import Translator
from ..View import View
from ...model.item.DiagramItems.DiagramItem import DiagramItem
from ...model.item.DiagramItems.TimeDiagramItem import TimeDiagramItem
from ...model.item.DiagramItems.BarDiagramItem import BarDiagramItem
from ...model.item.DiagramItems.DualDiagramItem import DualDiagramItem
from .StartButtonView import StartButtonView


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

    @abstractmethod
    def clear_diagram(self) -> NoReturn:
        pass

    def update_view(self) -> NoReturn:
        self._update_diagram(self._item.data)


class TimeDiagram(DiagramView):
    """this class represents a time diagram"""
    def __init__(self, item: TimeDiagramItem):
        """Initialising an TimeDiagram object

         Args:
             item (TimeDiagramItem): time plot diagram item
        """
        super().__init__(item)

        self.__time: List[float] = [i / 5.0 for i in range(-50, 0)]
        self.__data: List[float] = [0.0] * 50

        self.__ax: Subplot = self.figure.add_subplot(111)

        self.__ax.set_title(Translator.tr(self._item.name))

    def _update_diagram(self, data: List[float]) -> NoReturn:
        t = time.time() - StartButtonView.start_time
        while t - self.__time[0] > 10:
            self.__time.pop(0)
            self.__data.pop(0)

        self.__time.append(t)
        self.__data.append(data[0])

        self.__ax.clear()
        self.__ax.plot(self.__time, self.__data)
        self.draw()

    def clear_diagram(self) -> NoReturn:
        self.__time = [i / 5.0 for i in range(-50, 0)]
        self.__data = [0.0] * 50

        self.__ax.clear()
        self.__ax.plot(self.__time, self.__data)
        self.draw()


class DualDiagram(DiagramView):
    """this class represents a dual diagram"""
    def __init__(self, item: DualDiagramItem):
        """Initialising an DualDiagram object

        Args:
            item (DualDiagramItem): plot diagram item
        """
        super().__init__(item)

        self.__data_x: List[float] = []
        self.__data_y: List[float] = []

        self.__ax: Subplot = self.figure.add_subplot(111)

        self.__ax.set_title(Translator.tr(self._item.name))

    def _update_diagram(self, data: List[float]) -> NoReturn:
        if len(self.__data_x) > 10:
            self.__data_x.pop(0)
            self.__data_y.pop(0)
        self.__data_x.append(data[0])
        self.__data_y.append(data[1])

        self.__ax.clear()
        self.__ax.plot(self.__data_x, self.__data_y)
        self.draw()

    def clear_diagram(self) -> NoReturn:
        self.__data_x.clear()
        self.__data_y.clear()

        self.__ax.clear()
        self.__ax.plot(self.__data_x, self.__data_y)
        self.draw()


class BarDiagram(DiagramView):
    """this class represents a bar diagram """
    def __init__(self, item: BarDiagramItem):
        """Initialising an BarDiagram object

        Args:
            item (BarDiagramItem): bar chart diagram item
        """
        super().__init__(item)

        self.__data: List[float] = [0.0, 0.0, 0.0]
        self.__labels: List[str] = ["first input", "second input", "third input"]

        self.__ax: Subplot = self.figure.add_subplot(111)

        self.__ax.set_title(Translator.tr(self._item.name))

        self.__ax.bar(self.__labels, self.__data)
        self.draw()

    def _update_diagram(self, data: List[float]) -> NoReturn:
        for i in range(0, 3):
            self.__data[i] = data[i]

        self.__ax.clear()
        self.__ax.bar(self.__labels, self.__data)
        self.draw()

    def clear_diagram(self) -> NoReturn:
        self.__data.clear()

        self.__ax.clear()
        self.__ax.bar(self.__labels, self.__data)
        self.draw()
