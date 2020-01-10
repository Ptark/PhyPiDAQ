from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget

from python.src.view.item.InOutView import InOutView
from python.src.view.item.WorkspaceItemView import WorkspaceItemView


class InputView(InOutView):
    def __init__(self, parent: QWidget, item: WorkspaceItemView):
        super().__init__(parent, item)

        self.__connected: bool = False

    def is_connected(self) -> bool:
        return self.__connected

    def remove_connection(self) -> None:
        self.__connected = False

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        # TODO
        pass
