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
        super().__init__(parent)

        DeleteButtonView.__button = self

        self.setFixedSize(31, 31)
        self.setIcon(QIcon(SystemInfo.RESOURCES + 'images/buttons/delete.svg'))
        self.setEnabled(False)
        self.clicked.connect(self.__on_click)
        Translator.language_changed.signal.connect(self.__update_text)
        self.__update_text()

    def __update_text(self) -> NoReturn:
        self.setToolTip(Translator.tr("Entfernen"))

    def __on_click(self) -> NoReturn:
        if WorkspaceView.selection is not None:
            StartButtonView.interrupt_mp()
            time.sleep(0.2)     # TODO Thread Deadlock oder sowas
            WorkspaceView.selection.delete()

        self.clearFocus()

    @staticmethod
    def click() -> NoReturn:
        """a static method to execute the deletion of the selected workspaceItemView"""
        DeleteButtonView.__button.__on_click()

    @staticmethod
    def set_enabled(enabled: bool) -> NoReturn:
        DeleteButtonView.__button.setEnabled(enabled)
