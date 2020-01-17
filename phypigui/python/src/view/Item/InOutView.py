from typing import NoReturn

from PyQt5.QtWidgets import QWidget, QFrame

from ..View import View


class InOutViewMeta(type(QWidget), type(View)):
    pass


class InOutView(QFrame, View, metaclass=InOutViewMeta):
    def __init__(self):
        super().__init__(None)

        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        self.setFixedSize(20, 12)

        self.setStyleSheet("""
            QFrame {
                border: 2px solid black;
                border-radius: 5px;
                background-color: #FF0000;
                }
            """)