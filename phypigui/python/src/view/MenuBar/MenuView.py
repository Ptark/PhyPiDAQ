from typing import NoReturn

from PyQt5.QtWidgets import QMenu, QWidget

from .LanguageAction import LanguageAction


class FileMenuView(QMenu):
    def __init__(self, parent: QWidget):
        super().__init__("Datei", parent)

        self.addAction("Arbeitsfläche leeren", self.__clear_workspace)

    def __clear_workspace(self) -> NoReturn:
        pass  # TODO


class SettingsMenuView(QMenu):
    def __init__(self, parent: QWidget):
        super().__init__("Optionen", parent)

        self.__language_menu = QMenu("Sprache", self)
        self.addMenu(self.__language_menu)

        # Add languages here
        self.__language_menu.addAction(LanguageAction(self, "Deutsch", "de"))
        self.__language_menu.addAction(LanguageAction(self, "Englisch", "en"))


class HelpMenuView(QMenu):
    def __init__(self, parent: QWidget):
        super().__init__("Hilfe", parent)

        self.addAction("Info", self.__show_info)

    def __show_info(self) -> NoReturn:
        pass  # TODO