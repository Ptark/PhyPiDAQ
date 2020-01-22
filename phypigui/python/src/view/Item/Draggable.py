from abc import ABC
from typing import NoReturn

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget

from .ItemView import ItemView


class Draggable(ItemView, ABC):
    def __init__(self, main: QWidget, icon_path: str):
        super().__init__(main, icon_path)

        self.__mousePressPos: QPoint = None
        self.__mouseMovePos: QPoint = None

    def _save_position(self, event: QMouseEvent) -> NoReturn:
        self.__mousePressPos = event.globalPos()
        self.__mouseMovePos = event.globalPos()

    def _move_item(self, event: QMouseEvent) -> NoReturn:
        if self.__mouseMovePos is not None:
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)
            self.__mouseMovePos = globalPos

    def _on_click(self):
        pass

    def mouseReleaseEvent(self, event: QMouseEvent) -> NoReturn:
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return

        if event.button() == Qt.LeftButton:
            self._on_click()

        super(Draggable, self).mouseReleaseEvent(event)
