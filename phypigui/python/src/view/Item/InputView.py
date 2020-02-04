from typing import NoReturn

from PyQt5.QtGui import QMouseEvent

from ..Workspace.WireView import WireView
from ..Workspace.WorkspaceView import WorkspaceView
from PyQt5.QtWidgets import QWidget

from .InOutView import InOutView


class InputView(InOutView):
    """Class for displaying an item input"""
    def __init__(self, parent: QWidget, model_id: int):
        super().__init__(parent)

        self.__model_id: int = model_id

        self.__wire: WireView = None

    def redraw_wires(self) -> NoReturn:
        if self.__wire is not None:
            p = self._get_connection_point()
            self.__wire.redraw(input=p)

    def _remove_wire(self, wire: WireView) -> NoReturn:
        if self.__wire is wire:
            self.__wire = None

    def delete_all_wires(self) -> NoReturn:
        if self.__wire is not None:
            self.__wire.delete()
            self.__wire = None

    def mousePressEvent(self, event: QMouseEvent) -> NoReturn:
        if WorkspaceView.wire_in_hand is not None and self.__wire is None:
            self.__wire = WorkspaceView.wire_in_hand
            self.__wire.connect(self.__model_id)
            self.__wire.deletion_signal.connect(self._remove_wire)
            WorkspaceView.wire_in_hand = None
            self.redraw_wires()

        super().mousePressEvent(event)
