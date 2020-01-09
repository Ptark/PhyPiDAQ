from typing import TypeVar

from python.src.view.WorkSpace import WorkspaceView
from python.src.view.item.DiagramItemView import DiagramItemView
from python.src.view.item.ItemView import ItemView
from python.src.view.item.OperatorItemView import OperatorItemView
from python.src.view.item.SensorItemView import SensorItemView

T = TypeVar('T', SensorItemView, OperatorItemView, DiagramItemView)


class ListItemView(ItemView):
    def __init__(self, parent, id: int, icon_path: str, item: T):
        super().__init__(parent, id, icon_path)

        self.__visible = True
        self.__item = item

    def is_visible(self) -> bool:
        return self.__visible

    def set_visible(self, visible: bool):
        self.__visible = visible

    def mousePressEvent(self, event):
        item = ListItemView(self.parent(), self.__id, self.__icon_path, self.__item)
        item.move(self.pos())
        item.show()
        self.raise_()

        super(ListItemView, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if WorkspaceView.get_rectangle().contains(self.geometry()):
            item = self.__item.__class__(self.parent())  # TODO: richtiger Konstruktor
            item.move(self.pos())
            item.show()
        self.close()
