from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

from python.src.view.InfoBar.DeleteButtonView import DeleteButtonView
from python.src.view.InfoBar.SettingsButtonView import SettingsButtonView
from python.src.view.Workspace.WorkspaceView import WorkspaceView


class InfoBarView(QWidget):
    widget: QWidget

    def __init__(self, parent):
        super().__init__(parent)

        self.delete_button = DeleteButtonView(self)
        self.settings_button = SettingsButtonView(self)

        self.horizontal_layout = QHBoxLayout()  # for the info widget
        self.vertical_layout = QVBoxLayout()  # for the buttons

        self.vertical_layout.addWidget(self.delete_button)
        self.vertical_layout.addWidget(self.settings_button)
        self.horizontal_layout.addStretch(1)
        self.horizontal_layout.addLayout(self.vertical_layout)
        self.setLayout(self.horizontal_layout)

    def refresh_infobar(self):
        if not WorkspaceView.selection is None:
            self.widget = WorkspaceView.selection.get_info_widget()
            self.horizontal_layout.addWidget(self.widget)
