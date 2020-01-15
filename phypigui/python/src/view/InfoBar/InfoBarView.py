from PyQt5.QtWidgets import QWidget

from python.src.view.InfoBar.DeleteButtonView import DeleteButtonView
from python.src.view.InfoBar.SettingsButtonView import SettingsButtonView
from python.src.view.Workspace.WorkspaceView import WorkspaceView


class InfoBarView(QWidget):
    widget: QWidget

    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("Infobar")

        """self.Infobar = QtWidgets.QTextBrowser(self.InfobarView)
        self.Infobar.setGeometry(QtCore.QRect(0, 0, 401, 131))
        self.Infobar.setObjectName("Infobar")"""

        db = DeleteButtonView(self)

        sb = SettingsButtonView(self)

    def refresh_infobar(self):
        if not WorkspaceView.selection is None:
            self.widget = WorkspaceView.selection.get_info_widget()
            self.Infobar = self.widget  # Todo: Rückgabe in die InfoBarView einbinden.
            self.Infobar.setGeometry(QtCore.QRect(0, 0, InfoBarView.width(self), InfoBarView.height(self)))
