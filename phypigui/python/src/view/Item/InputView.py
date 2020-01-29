from typing import NoReturn

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QMouseEvent

from ..Workspace.WorkspaceView import WorkspaceView
from PyQt5.QtWidgets import QWidget

from .InOutView import InOutView


class InputView(InOutView):
    """Class for displaying an item input"""
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.__wire: QPoint = None

    def redraw_wire(self) -> NoReturn:
        if self.__wire is not None:
            p = self._get_connection_point()
            self.__wire.redraw(input=p)

    def mousePressEvent(self, event: QMouseEvent) -> NoReturn:
        if WorkspaceView.wire_in_hand is not None and self.__wire is None:
            self.__wire = WorkspaceView.wire_in_hand
            WorkspaceView.wire_in_hand = None
            self.redraw_wire()

        super().mousePressEvent(event)
