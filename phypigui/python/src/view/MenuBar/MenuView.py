from typing import NoReturn

from PyQt5.QtCore import QLocale
from PyQt5.QtWidgets import QMenu, QWidget

from ...model.manager.ManagerModel import ManagerModel
from ..config.ConfigView import ConfigView
from ..MenuBar.AboutWindow import AboutWindow
from ..Translator import Translator
from ..Workspace.WorkspaceView import WorkspaceView
from .LanguageAction import LanguageAction


class FileMenuView(QMenu):
    """This class represents the file menu of the main menu bar"""
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.addAction("", self.__clear_workspace)

        Translator.language_changed.signal.connect(self.__update_text)
        self.__update_text()

    def __update_text(self):
        self.setTitle(Translator.tr("Datei"))
        self.actions()[0].setText(Translator.tr("Arbeitsfläche leeren"))

    def __clear_workspace(self) -> NoReturn:
        WorkspaceView.delete_all()


class SettingsMenuView(QMenu):
    """This class represents the settings menu of the main menu bar"""
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.addAction("", self.__open_global_options)
        self.__settings_window: ConfigView = None
        ManagerModel.init_config()

        self.__language_menu = QMenu("", self)
        self.addMenu(self.__language_menu)

        # Add languages here
        self.__language_menu.addAction(LanguageAction(self, QLocale.German))
        self.__language_menu.addAction(LanguageAction(self, QLocale.English))

        Translator.language_changed.signal.connect(self.__update_text)
        self.__update_text()

    def __update_text(self):
        self.setTitle(Translator.tr("Einstellungen"))
        self.actions()[0].setText(Translator.tr("Globale Einstellungen"))
        self.__language_menu.setTitle(Translator.tr("Sprache"))
        self.__language_menu.actions()[0].setText(Translator.tr("Deutsch"))
        self.__language_menu.actions()[1].setText(Translator.tr("Englisch"))

    def __open_global_options(self):
        self.__settings_window = ConfigView("Globales", ManagerModel.get_settings())


class HelpMenuView(QMenu):
    """This class represents the help menu of the main menu bar"""
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.addAction("", self.__show_about)
        self.__about_window: AboutWindow = None

        Translator.language_changed.signal.connect(self.__update_text)
        self.__update_text()

    def __update_text(self):
        self.setTitle(Translator.tr("Hilfe"))
        self.actions()[0].setText(Translator.tr("Über"))

    def __show_about(self) -> NoReturn:
        self.__about_window = AboutWindow()
        self.__about_window.show()
