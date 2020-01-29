from abc import ABC
from typing import NoReturn

from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QFrame

from ..View import View


class InOutViewMeta(type(QFrame), type(View)):
    pass


class InOutView(QFrame, View, ABC, metaclass=InOutViewMeta):
    """Abstract class for displaying an item input or output"""
    def __init__(self):
        super().__init__(None)

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

    # Catches and stops all mouse events so other widgets under
    # the in-/outputs (items and workspace) don't get mouse events

    def mousePressEvent(self, event: QMouseEvent) -> NoReturn:
        pass

    def mouseMoveEvent(self, event: QMouseEvent) -> NoReturn:
        pass

    def mouseReleaseEvent(self, event: QMouseEvent) -> NoReturn:
        pass
