from abc import ABC
from typing import Type, NoReturn

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget

from .ItemEnum import ItemEnum
from .DragItemView import DragItemView
from .ItemView import ItemView
from .WorkspaceItemView import WorkspaceItemView


class ListItemView(ItemView, ABC):
    """Abstract class for displaying an item in the list

        Attributes:
            main (QWidget): The main widget of the window.
            item (Type[WorkspaceItemView]): A subclass of WorkspaceItemView to define which item type to represent.
                  It holds the actual class and not an instance of it.
    """
    def __init__(self, main: QWidget, item: ItemEnum):
        super().__init__(main, item.path)

        self.__main = main
        self.__item: ItemEnum = item

    def mousePressEvent(self, event: QMouseEvent) -> NoReturn:
        if event.buttons() == Qt.LeftButton:
            item = DragItemView(self.__main, event.globalPos(), self.__item)
            item.move(self.mapTo(self.__main, QPoint(0, 0)))
            item.show()
            item.grabMouse()
        
        super(ListItemView, self).mousePressEvent(event)
