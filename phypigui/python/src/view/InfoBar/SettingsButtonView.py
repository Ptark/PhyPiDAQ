from typing import NoReturn

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton

from ...SystemInfo import SystemInfo
from ..Translator import Translator
from ..Workspace.WorkspaceView import WorkspaceView


class SettingsButtonView(QPushButton):
    """This class represents the Settings button in the info bar"""
    __button: 'SettingsButtonView'

    def __init__(self, parent):
        super().__init__(parent)

        SettingsButtonView.__button = self

        self.setFixedSize(31, 31)
        self.setIcon(QIcon(SystemInfo.RESOURCES + 'images/buttons/settings.svg'))
        self.setEnabled(False)
        self.clicked.connect(self.__on_click)
        Translator.language_changed.signal.connect(self.__update_text)
        self.__update_text()

    def __update_text(self) -> NoReturn:
        self.setToolTip(Translator.tr("Einstellungen"))

    @pyqtSlot()
    def __on_click(self) -> NoReturn:
        if WorkspaceView.selection is not None:
            WorkspaceView.selection.open_config()

        self.clearFocus()

    @staticmethod
    def click() -> NoReturn:
        """a static method of the on click method that opens a window with the settings of the selected WorkspaceItemView"""
        SettingsButtonView.__button.__on_click()

    @staticmethod
    def set_enabled(enabled: bool) -> NoReturn:
        SettingsButtonView.__button.setEnabled(enabled)
