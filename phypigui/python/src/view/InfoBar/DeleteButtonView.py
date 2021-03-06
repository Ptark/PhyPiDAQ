from typing import NoReturn
import time

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton

from ..DiagramField.StartButtonView import StartButtonView
from ...SystemInfo import SystemInfo
from ..Translator import Translator
from ..Workspace.WorkspaceView import WorkspaceView


class DeleteButtonView(QPushButton):
    """This class represents the delete button in info bar"""
    __button: 'DeleteButtonView'

    def __init__(self, parent: QPushButton):
        """
        Initializes the delete button
        Args:
             parent (QPushButton)
        """
        super().__init__(parent)

        DeleteButtonView.__button = self

        self.setFixedSize(31, 31)
        self.setIcon(QIcon(SystemInfo.RESOURCES + 'images/buttons/delete.svg'))
        self.setEnabled(False)
        self.clicked.connect(self.__on_click)
        Translator.language_changed.signal.connect(self.__update_text)
        self.__update_text()

    def __update_text(self) -> NoReturn:
        """updates the tooltip text"""
        self.setToolTip(Translator.tr("Entfernen"))

    def __on_click(self) -> NoReturn:
        """on click method when delete button is clicked deletes the selected item in workspaceview"""
        if WorkspaceView.selection is not None:
            StartButtonView.interrupt_mp()
            WorkspaceView.selection.delete()

        self.clearFocus()

    @staticmethod
    def click() -> NoReturn:
        """a static method to execute the deletion of the selected workspaceItemView"""
        DeleteButtonView.__button.__on_click()

    @staticmethod
    def set_enabled(enabled: bool) -> NoReturn:
        """enables the delete button"""
        DeleteButtonView.__button.setEnabled(enabled)
