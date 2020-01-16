from typing import NoReturn

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget

# from ...model.item.ItemModel import ItemModel
from .Draggable import Draggable
from ..Selectable import Selectable
from ..Workspace.WorkspaceView import WorkspaceView


class WorkspaceItemView(Draggable, Selectable):
    def __init__(self, main: QWidget):
        super().__init__(main)

        self.__lastPos: QPoint = None

        # self.__model: ItemModel = None
        # self.__selected: bool = False
        # self.__inputs: List[InputView] = []
        # self.__outputs: List[OutputView] = []

        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        # TODO
        pass

    def get_info_widget(self) -> QWidget:
        pass

    def delete(self) -> NoReturn:
        WorkspaceView.delete_item(self)

    def mousePressEvent(self, event: QMouseEvent) -> NoReturn:
        if event.buttons() == Qt.LeftButton:
            self.__lastPos = self.pos()
            self._save_position(event)

        super(WorkspaceItemView, self).mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> NoReturn:
        if event.buttons() == Qt.LeftButton:
            self._move_item(event)

        super(WorkspaceItemView, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> NoReturn:
        if not WorkspaceView.widget.geometry().contains(self.geometry()):
            self.move(self.__lastPos)
            return

        super(WorkspaceItemView, self).mouseReleaseEvent(event)
