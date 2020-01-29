from typing import NoReturn, List

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget

from ..Workspace.WorkspaceView import WorkspaceView
from ..Workspace.WireView import WireView
from .InOutView import InOutView


class OutputView(InOutView):
    """Class for displaying an item output"""
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.__wires: List[QPoint] = []

    def redraw_wire(self) -> NoReturn:
        p = self._get_connection_point()
        for wire in self.__wires:
            wire.redraw(output=p)

    def mousePressEvent(self, event: QMouseEvent) -> NoReturn:
        if WorkspaceView.wire_in_hand is None:
            p = self._get_connection_point()
            wire = WireView(p, p)
            self.__wires.append(wire)
            WorkspaceView.add_wire(wire)
            wire.redraw()

        super().mousePressEvent(event)
