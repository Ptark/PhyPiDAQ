from typing import NoReturn

from PyQt5.QtGui import QMouseEvent

# from ..Workspace.WorkspaceView import WorkspaceView
from .InOutView import InOutView


class InputView(InOutView):
    """Class for displaying an item input"""
    def __init__(self):
        super().__init__()

        self.__connected: bool = False

    @property
    def connected(self) -> bool:
        return self.__connected

    def remove_connection(self) -> NoReturn:
        self.__connected = False

    def mousePressEvent(self, event: QMouseEvent) -> NoReturn:
        """
        if WorkspaceView.wire_in_hand is not None:
            WorkspaceView.wire_in_hand.input = self
            self.__connected = True
            WorkspaceView.wire_in_hand = None
        """
        super(InputView, self).mouseReleaseEvent(event)
