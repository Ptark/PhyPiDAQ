from abc import ABC, abstractmethod
from typing import NoReturn

from PyQt5.QtWidgets import QWidget, QFrame

from ..View import View


class ItemViewMeta(type(QFrame), type(View)):
    pass


class ItemView(QFrame, View, metaclass=ItemViewMeta):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        # TODO: id

        self.__init_view()

    def __init_view(self) -> NoReturn:
        self.setFixedSize(150, 60)
        self.setStyleSheet("""
            QFrame {
                border: 2px solid black;
                border-radius: 5px;
                background-color: #CCCCCC;
                }
            """)

        # TODO: Size
        # TODO: Shape
        # TODO: Icons
