from typing import NoReturn

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton

from ..Workspace.WorkspaceView import WorkspaceView


class DeleteButtonView(QPushButton):
    __button: 'DeleteButtonView'

    def __init__(self, parent):
        super().__init__(parent)

        DeleteButtonView.__button = self

        self.setFixedSize(31, 31)
        self.setIcon(QIcon("../resources/images/buttons/delete.svg"))
        self.clicked.connect(self.__on_click)

    @pyqtSlot()
    def __on_click(self) -> NoReturn:
        if WorkspaceView.selection is not None:
            WorkspaceView.selection.delete()

        self.clearFocus()

    @staticmethod
    def click() -> NoReturn:
        DeleteButtonView.__button.__on_click()
