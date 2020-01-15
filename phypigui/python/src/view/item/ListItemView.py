from typing import Type, NoReturn

from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget

from ..Workspace.WorkspaceView import WorkspaceView
from .ItemView import ItemView
from .WorkspaceItemView import WorkspaceItemView


class ListItemView(ItemView):
    def __init__(self, parent: QWidget, id: int, icon_path: str, item: Type[WorkspaceItemView]):
        super().__init__(parent, id, icon_path)

        self.__visible: bool = True
        self.__item: Type[WorkspaceItemView] = item

    def is_visible(self) -> bool:
        return self.__visible

    def set_visible(self, visible: bool) -> NoReturn:
        self.__visible = visible

    def mousePressEvent(self, event: QMouseEvent) -> NoReturn:
        item = ListItemView(self.parent(), self.__id, self.__icon_path, self.__item)
        item.move(self.pos())
        item.show()
        self.raise_()

        super(ListItemView, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> NoReturn:
        if WorkspaceView.get_rectangle().contains(self.geometry()):
            item = self.__item(self.parent(), self.__id, self.__icon_path)
            item.move(self.pos())
            item.show()
        self.close()
