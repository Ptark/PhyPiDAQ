from typing import NoReturn

from PyQt5.QtWidgets import QWidget

from ..View import View


class ItemView(QWidget, View):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        # TODO
        # self.__id: int = 0
        # self.__icon_path: str = ""

        self.__init_view()

    def __init_view(self) -> NoReturn:
        self.setFixedSize(150, 50)
        self.setAutoFillBackground(True)

        # TODO: Shape
        # TODO: Icons
