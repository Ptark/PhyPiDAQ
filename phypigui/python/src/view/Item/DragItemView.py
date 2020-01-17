from abc import ABC
from typing import NoReturn, Type

from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget

from .Draggable import Draggable
from .WorkspaceItemView import WorkspaceItemView
from ..Workspace.WorkspaceView import WorkspaceView


class DragItemView(Draggable, ABC):
    def __init__(self, main: QWidget, event: QMouseEvent, item: Type[WorkspaceItemView]):
        super().__init__(main, item.icon_path)

        self.__main = main
        self.__item: Type[WorkspaceItemView] = item

        self._save_position(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> NoReturn:
        self._move_item(event)

        super(DragItemView, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> NoReturn:
        if WorkspaceView.widget.geometry().contains(self.geometry()):
            item = self.__item(self.__main)
            item.move(self.pos())
            item.show()

        self.releaseMouse()
        event.ignore()
        self.close()
