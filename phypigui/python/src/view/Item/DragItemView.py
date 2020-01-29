from abc import ABC
from typing import NoReturn, Type

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget

from .Draggable import Draggable
from .WorkspaceItemView import WorkspaceItemView
from ..Workspace.WorkspaceView import WorkspaceView


class DragItemView(Draggable, ABC):
    """Abstract class for displaying an temporary item for dragging from the list to the workspace

        Attributes:
            main (QWidget): The main widget of the window.
            pos (QPoint): The position at which the item is created.
            item (Type[WorkspaceItemView]): A subclass of WorkspaceItemView to define which item type to represent.
                  It holds the actual class and not an instance of it.
    """
    def __init__(self, main: QWidget, pos: QPoint, item: Type[WorkspaceItemView]):
        super().__init__(main, item.icon_path)

        self.__main = main
        self.__item: Type[WorkspaceItemView] = item

        self._save_position(pos)

    def mouseMoveEvent(self, event: QMouseEvent) -> NoReturn:
        self._move_item(event.globalPos())

        super(DragItemView, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> NoReturn:
        if WorkspaceView.is_on_workspace(self):
            item = self.__item(WorkspaceView.widget)
            item.move(item.mapFrom(self.parent(), self.pos()))
            item.show()

        self.releaseMouse()
        event.ignore()
        self.close()
