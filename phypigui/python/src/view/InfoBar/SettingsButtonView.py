from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QPushButton


# from python.src.view.item.WorkspaceItemView import WorkspaceItemView


class SettingsButtonView(QPushButton):
    # item_config: WorkspaceItemView  #Todo was macht das eigentlich?
    __icon_source = "../resources/images/buttons/settingsbutton.png"

    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(31, 31)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(self.__icon_source))
        self.setIcon(self.icon)
        # self.clicked.connect(self.on_click())

    def on_click(self):
        ConfigView.init_window()
