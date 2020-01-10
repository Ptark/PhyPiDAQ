from typing import Type

from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget

from python.src.view.WorkSpace import WorkspaceView
from python.src.view.item.ItemView import ItemView

from python.src.view.item.WorkspaceItemView import WorkspaceItemView


class ListItemView(ItemView):
    def __init__(self, parent: QWidget, id: int, icon_path: str, item: Type[WorkspaceItemView]):
        super().__init__(parent, id, icon_path)

        self.__visible: bool = True
        self.__item: Type[WorkspaceItemView] = item

    def is_visible(self) -> bool:
        return self.__visible

    def set_visible(self, visible: bool) -> None:
        self.__visible = visible

    def mousePressEvent(self, event: QMouseEvent) -> None:
        item = ListItemView(self.parent(), self.__id, self.__icon_path, self.__item)
        item.move(self.pos())
        item.show()
        self.raise_()

        super(ListItemView, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if WorkspaceView.get_rectangle().contains(self.geometry()):
            item = self.__item(self.parent(), self.__id, self.__icon_path)
            item.move(self.pos())
            item.show()
        self.close()
