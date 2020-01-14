from PyQt5 import QtCore
from PyQt5.QtWidgets import QPushButton

#from python.src.view.item.WorkspaceItemView import WorkspaceItemView


class SettingsButtonView(QPushButton):
    #item_config: WorkspaceItemView

    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(360, 80, 31, 31))
        self.setText("sett")
        self.setObjectName("SettingsButtonView")

    def on_click(self):
        pass
