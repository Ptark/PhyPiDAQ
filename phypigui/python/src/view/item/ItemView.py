from abc import ABC, abstractmethod

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QFrame


class ItemView(ABC, QWidget):
    def __init__(self, parent, id: int, icon_path: str):
        super.__init__(parent)

        self.__id: int = id
        self.__icon_path: str = icon_path
        
        self.__mousePressPos = None
        self.__mouseMovePos = None
        self.__lastPos = None

        self.__init_view()

    def __init_view(self):
        self.setFixedSize(150, 50)
        self.setFrameShape(QFrame.StyledPanel)
        self.setAutoFillBackground(True)

        # TODO: Shape
        # TODO: Icons

    @abstractmethod
    def delete(self):
        self.delete()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()
            self.__lastPos = self.pos()

        super(ItemView, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)
            self.__mouseMovePos = globalPos

        super(ItemView, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return

        super(ItemView, self).mouseReleaseEvent(event)
