from copy import copy
from typing import NoReturn, List

from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget

from ..Workspace.WorkspaceView import WorkspaceView
from ..Workspace.WireView import WireView
from .InOutView import InOutView


class OutputView(InOutView):
    """Class for displaying an item output"""
    def __init__(self, parent: QWidget, model_id: int):
        super().__init__(parent)

        self.__model_id: int = model_id

        self.__wires: List[WireView] = []

    def redraw_wires(self) -> NoReturn:
        p = self._get_connection_point()
        for wire in self.__wires:
            wire.redraw(output=p)

    def _remove_wire(self, wire: WireView) -> NoReturn:
        self.__wires.remove(wire)

    def delete_all_wires(self) -> NoReturn:
        for wire in copy(self.__wires):
            wire.delete()
        self.__wires = []

    def mousePressEvent(self, event: QMouseEvent) -> NoReturn:
        if WorkspaceView.wire_in_hand is None:
            p = self._get_connection_point()
            wire = WireView(p, p, self.__model_id)
            wire.deletion_signal.connect(self._remove_wire)
            self.__wires.append(wire)
            WorkspaceView.add_wire(wire)
            wire.redraw()

        super().mousePressEvent(event)
