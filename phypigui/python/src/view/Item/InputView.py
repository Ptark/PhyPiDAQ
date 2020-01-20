from typing import NoReturn

from PyQt5.QtGui import QMouseEvent

from .InOutView import InOutView


class InputView(InOutView):
    def __init__(self):
        super().__init__()

        self.__connected: bool = False

    @property
    def connected(self) -> bool:
        return self.__connected

    def remove_connection(self) -> NoReturn:
        self.__connected = False

    def mouseReleaseEvent(self, event: QMouseEvent) -> NoReturn:
        # TODO
        pass
