from abc import ABC
from typing import NoReturn

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QFrame, QWidget

from ..View import View


class InOutViewMeta(type(QFrame), type(View)):
    pass


class InOutView(QFrame, View, ABC, metaclass=InOutViewMeta):
    """Abstract class for displaying an item input or output"""

    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        self.setFixedSize(20, 12)

        self.setStyleSheet("""
            QFrame {
                border: 2px solid black;
                border-radius: 5px;
                background-color: #FF4444;
                }
            """)

    def _get_connection_point(self) -> QPoint:
        p = self.parent().mapTo(self.parent().parent().parent(), self.pos())
        p.setX(p.x() + self.width() / 2)
        p.setY(p.y() + self.height() / 2)
        return p

    # Catches and stops all mouse events so other widgets under
    # the in-/outputs (items and workspace) don't get mouse events
    def mousePressEvent(self, event: QMouseEvent) -> NoReturn:
        pass

    def mouseMoveEvent(self, event: QMouseEvent) -> NoReturn:
        pass

    def mouseReleaseEvent(self, event: QMouseEvent) -> NoReturn:
        pass
