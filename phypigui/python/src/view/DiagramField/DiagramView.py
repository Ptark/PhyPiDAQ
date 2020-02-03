from typing import NoReturn

from PyQt5.QtWidgets import QSizePolicy
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from ..View import View
from ...model.item import DiagramItem


class DiagramViewMeta(type(FigureCanvas), type(View)):
    pass


class DiagramView(FigureCanvas, View, metaclass=DiagramViewMeta):
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
        pass
        # self.__update_diagram(self.__item.data[0])


class TimeDiagram(DiagramView):
    def __update_diagram(self, data: float) -> NoReturn:
        self.data.append(data)
        self.ax.plot(self.data, "r")
        self.draw()
