from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QAction

from ..Translator import Translator


class LanguageAction(QAction):
    """This class represents a language change action in the main menu bar"""
    def __init__(self, parent, locale: int):
        super().__init__(parent)

        self.__locale: int = locale

        self.triggered.connect(self.__on_click)

    @pyqtSlot()
    def __on_click(self):
        Translator.install_translator(self.__locale)
