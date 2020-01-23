from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton


from ..Workspace.WorkspaceView import WorkspaceView


class SettingsButtonView(QPushButton):
    __icon_source = "../resources/images/buttons/settingsbutton.png"

    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(31, 31)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(self.__icon_source))
        self.setIcon(self.icon)
        self.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        if WorkspaceView.selection is not None:
            WorkspaceView.selection.open_config()
