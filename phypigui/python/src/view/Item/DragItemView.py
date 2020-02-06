from abc import ABC
from typing import NoReturn, Type

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget

from .ItemEnum import ItemEnum
from ..Translator import Translator
from ..DialogView import DialogView
from ...Exceptions import DuplicateWorkspaceItemException, DiagramMaximumReachedException
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
    def __init__(self, main: QWidget, pos: QPoint, item: ItemEnum):
        super().__init__(main, item.path)

        self.__main = main
        self.__item: ItemEnum = item

        self._save_position(pos)

    def mouseMoveEvent(self, event: QMouseEvent) -> NoReturn:
        self._move_item(event.globalPos())

        super(DragItemView, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> NoReturn:
        self.releaseMouse()
        event.ignore()
        self.close()

        if WorkspaceView.is_on_workspace(self):
            try:
                item = self.__item.create_workspace_item(WorkspaceView.widget)
            except DuplicateWorkspaceItemException:
                DialogView.show_warning(Translator.tr("Element schon auf Arbeitsfläche"),
                                        Translator.tr("Dieses Element kann nur einmal auf der Arbeitsfläche existieren."))
            except DiagramMaximumReachedException:
                DialogView.show_warning(Translator.tr("Maximum an Diagrammen erreicht"),
                                        Translator.tr("Es können nur drei Diagramme gleichzeitig verwendet werden.\n"
                                                      "Lösche ein anderes Diagramm um ein neues zu verwenden."))
            else:
                item.move(item.mapFrom(self.parent(), self.pos()))
                item.show()
