from typing import NoReturn

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton

from ..Translator import Translator
from ..Workspace.WorkspaceView import WorkspaceView


class DeleteButtonView(QPushButton):
    """This class represents the delete button in info bar"""
    __button: 'DeleteButtonView'

    def __init__(self, parent: QPushButton):
        super().__init__(parent)

        DeleteButtonView.__button = self

        self.setFixedSize(31, 31)
        self.setIcon(QIcon("../resources/images/buttons/delete.svg"))
        self.clicked.connect(self.__on_click)
        Translator.language_changed.signal.connect(self.__update_text)
        self.__update_text()

    def __update_text(self) -> NoReturn:
        self.setToolTip(Translator.tr("Entfernen"))

    @pyqtSlot()
    def __on_click(self) -> NoReturn:
        if WorkspaceView.selection is not None:
            WorkspaceView.selection.delete()

        self.clearFocus()

    @staticmethod
    def click() -> NoReturn:
        """a static method to execute the deletion of the selected workspaceItemView"""
        DeleteButtonView.__button.__on_click()
