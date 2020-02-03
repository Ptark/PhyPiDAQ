from PyQt5.QtWidgets import QMenuBar

from .MenuView import FileMenuView, SettingsMenuView, HelpMenuView
from ..View import View


class MenuBarViewMeta(type(QMenuBar), type(View)):
    pass


class MenuBarView(QMenuBar, View, metaclass=MenuBarViewMeta):
    """This class represents the menu bar of the main window"""
    def __init__(self):
        super().__init__(None)

        self.addMenu(FileMenuView(self))
        self.addMenu(SettingsMenuView(self))
        self.addMenu(HelpMenuView(self))
