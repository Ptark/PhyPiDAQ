from typing import NoReturn, Final

from PyQt5.QtCore import pyqtSignal, QObject, QPoint
from PyQt5.QtWidgets import QWidget, QMenu

from ..Selectable import Selectable
from .WorkspaceView import WorkspaceView


class WireViewMeta(type(Selectable), type(QObject)):
    pass


class WireView(Selectable, QObject, metaclass=WireViewMeta):
    __CLICKABLE_MARGIN: Final[int] = 1400
    redraw_signal = pyqtSignal()
    deletion_signal = pyqtSignal(QObject)

    def __init__(self, output: QPoint, input: QPoint):
        Selectable.__init__(self)
        QObject.__init__(self)

        self.__output: QPoint = output
        self.__input: QPoint = input

    @property
    def output(self) -> QPoint:
        """Position of the connected output"""
        return self.__output

    @property
    def input(self) -> QPoint:
        """Position of the connected input"""
        return self.__input

    def redraw(self, output: QPoint = None, input: QPoint = None) -> NoReturn:
        """Updates the position of the connected in- and/or output

            Args:
                output (QPoint): The new output position. If not given, output position does not change.
                input (QPoint): The new input position. If not given, input position does not change.
        """
        if output is not None:
            self.__output = output
        if input is not None:
            self.__input = input

        self.redraw_signal.emit()

    def point_on_line(self, point: QPoint) -> bool:
        """Checks if the given point is on the wire

            Args:
                point (QPoint): Thw point to check.

            Returns:
                bool: Returns true when the given point is on the wire.
        """
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

    def open_context_menu(self, pos: QPoint) -> NoReturn:
        """Creates a context menu at the given position

            Args:
                pos (QPoint): Position at which the menu should appear.
        """
        menu = QMenu()
        menu.addAction(self.tr("Entfernen"), self.delete)
        menu.exec(pos)

    def _update_selected_view(self) -> NoReturn:
        self.redraw()

    def get_info_widget(self) -> QWidget:
        pass

    def open_config(self) -> NoReturn:
        pass

    def delete(self) -> NoReturn:
        WorkspaceView.delete_wire(self)
        super().delete()
        self.deletion_signal.emit(self)
        self.redraw()
