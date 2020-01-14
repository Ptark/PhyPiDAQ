from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget

from python.src.view.InfoBar.DeleteButtonView import DeleteButtonView
from python.src.view.InfoBar.SettingsButtonView import SettingsButtonView
from python.src.view.Workspace.WorkspaceView import WorkspaceView


class InfoBarView(QWidget):
    widget: QWidget

    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(190, 450, 401, 131))
        self.setObjectName("Infobar")

        """self.Infobar = QtWidgets.QTextBrowser(self.InfobarView)
        self.Infobar.setGeometry(QtCore.QRect(0, 0, 401, 131))
        self.Infobar.setObjectName("Infobar")"""

        db = DeleteButtonView(self)

        sb = SettingsButtonView(self)

    def refresh_infobar(self):
        self.widget = WorkspaceView.selection.get_info_widget()
        self.Infobar(self.widget)
