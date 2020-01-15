from PyQt5 import QtCore
from PyQt5.QtWidgets import QPushButton

#from python.src.view.item.WorkspaceItemView import WorkspaceItemView


class SettingsButtonView(QPushButton):
    #item_config: WorkspaceItemView  #Todo was macht das eigentlich?

    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(360, 80, 31, 31))
        self.setText("sett")
        self.setObjectName("SettingsButtonView")
        #self.clicked.connect(self.on_click())

    def on_click(self):
        ConfigView.init_window()
