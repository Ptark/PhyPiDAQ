from PyQt5.QtCore import pyqtSlot, QLocale
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction

from ..Translator import Translator


class LanguageAction(QAction):
    """This class represents a language change action in the main menu bar"""
    def __init__(self, parent, locale: int):
        super().__init__(parent)

        self.__locale: int = locale
        self.setIcon(QIcon("../resources/images/flags/" + QLocale(self.__locale).name() + ".png"))

        self.triggered.connect(self.__on_click)

    @pyqtSlot()
    def __on_click(self):
        Translator.install_translator(self.__locale)
