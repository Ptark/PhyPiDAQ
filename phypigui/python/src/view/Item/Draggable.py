from typing import NoReturn

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget

from .ItemView import ItemView


class Draggable(ItemView):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.__mousePressPos: QPoint = None
        self.__mouseMovePos: QPoint = None

    def _save_position(self, event: QMouseEvent) -> NoReturn:
        self.__mousePressPos = event.globalPos()
        self.__mouseMovePos = event.globalPos()

    def _move_item(self, event: QMouseEvent) -> NoReturn:
        currPos = self.mapToGlobal(self.pos())
        globalPos = event.globalPos()
        diff = globalPos - self.__mouseMovePos
        newPos = self.mapFromGlobal(currPos + diff)
        self.move(newPos)
        self.__mouseMovePos = globalPos

    def mouseReleaseEvent(self, event: QMouseEvent) -> NoReturn:
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return

        super(Draggable, self).mouseReleaseEvent(event)
