from typing import NoReturn

from PyQt5.QtWidgets import QMenu, QWidget

from .LanguageAction import LanguageAction


class FileMenuView(QMenu):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.setTitle(self.tr("&Datei"))
        self.addAction(self.tr("Arbeitsflaeche leeren"), self.__clear_workspace)

    def __clear_workspace(self) -> NoReturn:
        pass  # TODO


class SettingsMenuView(QMenu):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.setTitle(self.tr("&Optionen"))
        self.__language_menu = QMenu(self.tr("Sprache"), self)
        self.addMenu(self.__language_menu)

        # Add languages here
        self.__language_menu.addAction(LanguageAction(self, self.tr("Deutsch"), "de"))
        self.__language_menu.addAction(LanguageAction(self, self.tr("Englisch"), "en"))


class HelpMenuView(QMenu):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.setTitle(self.tr("&Hilfe"))
        self.addAction(self.tr("Info"), self.__show_info)

    def __show_info(self) -> NoReturn:
        pass  # TODO