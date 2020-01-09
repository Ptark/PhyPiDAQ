from PyQt5.QtWidgets import QWidget, QPushButton


class InfoBarView(QWidget):
    widget: QWidget

    def refresh_infobar(self):
        pass


class DeleteButtonView(QPushButton):

    def on_click(self):
        pass


class SettingsButtonView(QPushButton):
    item_config: WorkspaceitemView

    def on_click(self):
        pass
