import time
from abc import ABC, abstractmethod
from typing import NoReturn, List

from matplotlib.axes import Subplot
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5.QtWidgets import QSizePolicy, QFrame, QGridLayout

from ..Translator import Translator
from ..View import View
from ...model.item.DiagramItems.DiagramItem import DiagramItem
from ...model.item.DiagramItems.TimeDiagramItem import TimeDiagramItem
from ...model.item.DiagramItems.BarDiagramItem import BarDiagramItem
from ...model.item.DiagramItems.DualDiagramItem import DualDiagramItem
from .StartButtonView import StartButtonView


class DiagramViewMeta(type(QFrame), type(View)):
    pass


class DiagramView(QFrame, View, ABC, metaclass=DiagramViewMeta):
    """the super class of Time diagram, bar diagram and Dual diagram"""
    def __init__(self, item: DiagramItem, projection: str = 'rectilinear'):
        super().__init__()

        self._canvas = FigureCanvas(Figure(figsize=(4, 5), dpi=70))
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self._canvas)
        self.setLayout(layout)

        self._ax: Subplot = self._canvas.figure.add_subplot(111, projection=projection)
        self._item: DiagramItem = item
        self._item.attach(self)

        self.setStyleSheet("QFrame { border: 2px solid white; border-radius: 4px }")
        Translator.language_changed.signal.connect(self._draw_diagram)
        self._draw_diagram()

    @abstractmethod
    def _draw_diagram(self) -> NoReturn:
        pass

    @abstractmethod
    def _update_diagram(self, data: List[float]) -> NoReturn:
        pass

    @abstractmethod
    def clear_diagram(self) -> NoReturn:
        pass

    def update_view(self) -> NoReturn:
        self._update_diagram(self._item.data)

    def update_selected_view(self, selected: bool):
        border = "blue" if selected else "white"
        self.setStyleSheet("QFrame { border: 2px solid %s; border-radius: 4px }" % border)


class TimeDiagram(DiagramView):
    """this class represents a time diagram"""
    def __init__(self, item: TimeDiagramItem):
        """Initialising an TimeDiagram object

         Args:
             item (TimeDiagramItem): time plot diagram item
        """
        self.__time: List[float] = [i / 5.0 for i in range(-50, 0)]
        self.__data: List[float] = [0.0] * 50

        super().__init__(item)

    def _draw_diagram(self) -> NoReturn:
        self._ax.clear()

        self._ax.set_title(Translator.tr(self._item.name))
        self._ax.set_xlabel("s")
        self._ax.set_ylabel(self._item.unit[0])

        self._ax.plot(self.__time, self.__data)

        self._canvas.draw()

    def _update_diagram(self, data: List[float]) -> NoReturn:
        t = time.time() - StartButtonView.start_time
        while t - self.__time[0] > 10:
            self.__time.pop(0)
            self.__data.pop(0)

        self.__time.append(t)
        self.__data.append(data[0])

        self._draw_diagram()

    def clear_diagram(self) -> NoReturn:
        self.__time = [i / 5.0 for i in range(-50, 0)]
        self.__data = [0.0] * 50

        self._draw_diagram()


class DualDiagram(DiagramView):
    """this class represents a dual diagram"""
    def __init__(self, item: DualDiagramItem):
        """Initialising an DualDiagram object

        Args:
            item (DualDiagramItem): plot diagram item
        """
        self.__data_x: List[float] = []
        self.__data_y: List[float] = []

        super().__init__(item)

    def _draw_diagram(self) -> NoReturn:
        self._ax.clear()

        self._ax.set_title(Translator.tr(self._item.name))
        self._ax.set_xlabel(self._item.unit[0])
        self._ax.set_ylabel(self._item.unit[1])

        self._ax.plot(self.__data_x, self.__data_y)

        self._canvas.draw()

    def _update_diagram(self, data: List[float]) -> NoReturn:
        if len(self.__data_x) > 10:
            self.__data_x.pop(0)
            self.__data_y.pop(0)
        self.__data_x.append(data[0])
        self.__data_y.append(data[1])

        self._draw_diagram()

    def clear_diagram(self) -> NoReturn:
        self.__data_x.clear()
        self.__data_y.clear()

        self._draw_diagram()


class BarDiagram(DiagramView):
    """this class represents a bar diagram """
    def __init__(self, item: BarDiagramItem):
        """Initialising an BarDiagram object

        Args:
            item (BarDiagramItem): bar chart diagram item
        """
        self.__data: List[float] = [0.0, 0.0, 0.0]
        self.__labels: List[str] = ["first input", "second input", "third input"]

        super().__init__(item)

    def _draw_diagram(self):
        self._ax.clear()

        self._ax.set_title(Translator.tr(self._item.name))

        self._ax.bar(self.__labels, self.__data)

        self._canvas.draw()

    def _update_diagram(self, data: List[float]) -> NoReturn:
        for i in range(0, 3):
            self.__data[i] = data[i]

        self._draw_diagram()

    def clear_diagram(self) -> NoReturn:
        self.__data = [0.0, 0.0, 0.0]

        self._draw_diagram()
