from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QAction


class LanguageAction(QAction):
    def __init__(self, parent, text: str, locale: str):
        super().__init__(text, parent)

        self.__locale = locale

        self.triggered.connect(self.__on_click)

    @pyqtSlot()
    def __on_click(self):
        pass  # TODO
