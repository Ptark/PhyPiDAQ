from typing import NoReturn

from PyQt5.QtWidgets import QWidget


class Selectable:
    def get_info_widget(self) -> QWidget:
        pass

    def delete(self) -> NoReturn:
        pass
