from abc import ABC

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget, QFrame

from python.src.view.View import View


class ItemView(ABC, QWidget, View):
    def __init__(self, parent: QWidget, id: int, icon_path: str):
        super().__init__(parent)

        self.__id: int = id
        self.__icon_path: str = icon_path

        self.__mousePressPos: QPoint = None
        self.__mouseMovePos: QPoint = None
        self.__lastPos: QPoint = None

        self.__init_view()

    def __init_view(self):
        self.setFixedSize(150, 50)
        self.setFrameShape(QFrame.StyledPanel)
        self.setAutoFillBackground(True)

        # TODO: Shape
        # TODO: Icons

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()
            self.__lastPos = self.pos()

        super(ItemView, self).mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if event.buttons() == Qt.LeftButton:
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)
            self.__mouseMovePos = globalPos

        super(ItemView, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return

        super(ItemView, self).mouseReleaseEvent(event)
