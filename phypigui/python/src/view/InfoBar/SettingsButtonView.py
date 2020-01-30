from typing import NoReturn

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton

from ..Workspace.WorkspaceView import WorkspaceView


class SettingsButtonView(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)

        self.setFixedSize(31, 31)
        self.setIcon(QIcon("../resources/images/buttons/settings.svg"))
        self.clicked.connect(self.__on_click)

    @pyqtSlot()
    def __on_click(self) -> NoReturn:
        if WorkspaceView.selection is not None:
            WorkspaceView.selection.open_config()
