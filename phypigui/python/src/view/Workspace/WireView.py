from typing import NoReturn, Final

from PyQt5.QtCore import pyqtSignal, QObject, QPoint
from PyQt5.QtWidgets import QWidget

from ..Selectable import Selectable
from .WorkspaceView import WorkspaceView


class WireViewMeta(type(Selectable), type(QObject)):
    pass


class WireView(Selectable, QObject, metaclass=WireViewMeta):
    __CLICKABLE_MARGIN: Final[int] = 1400
    redraw_signal = pyqtSignal()

    def __init__(self, output: QPoint, input: QPoint):
        Selectable.__init__(self)
        QObject.__init__(self)

        self.__output: QPoint = output
        self.__input: QPoint = input

    @property
    def output(self) -> QPoint:
        return self.__output

    @property
    def input(self) -> QPoint:
        return self.__input

    def redraw(self, output: QPoint = None, input: QPoint = None) -> NoReturn:
        if output is not None:
            self.__output = output
        if input is not None:
            self.__input = input

        self.redraw_signal.emit()

    def point_on_line(self, point: QPoint) -> bool:
        p1_x = self.__output.x()
        p1_y = self.__output.y()
        p2_x = self.__input.x()
        p2_y = self.__input.y()
        p_x = point.x()
        p_y = point.y()

        cross_product = (p_y - p1_y) * (p2_x - p1_x) - (p_x - p1_x) * (p2_y - p1_y)
        if abs(cross_product) > WireView.__CLICKABLE_MARGIN:
            return False

        dot_product = (p_x - p1_x) * (p2_x - p1_x) + (p_y - p1_y)*(p2_y - p1_y)
        if dot_product < 0:
            return False

        squared_length = (p2_x - p1_x)*(p2_x - p1_x) + (p2_y - p1_y)*(p2_y - p1_y)
        if dot_product > squared_length:
            return False

        return True

    def _update_selected_view(self) -> NoReturn:
        self.redraw()

    def get_info_widget(self) -> QWidget:
        pass

    def open_config(self) -> NoReturn:
        pass

    def delete(self) -> NoReturn:
        WorkspaceView.delete_wire(self)
        super().delete()
        self.redraw()
