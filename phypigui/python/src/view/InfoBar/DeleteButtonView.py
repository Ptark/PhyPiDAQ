from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QPushButton

from python.src.view.Workspace.WorkspaceView import WorkspaceView


# from python.src.view.item.WorkspaceItemView import WorkspaceItemView


class DeleteButtonView(QPushButton):
    __icon_source = "../resources/images/buttons/deletebutton.png"

    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(31, 31)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(self.__icon_source))
        self.setIcon(self.icon)
        self.clicked.connect(self.on_click)

    def on_click(self):
        selectable = WorkspaceView.get_selectable()  # todo: WorspaceItemView raises an error

        ''' if selectable.type() == WorkspaceItemView:          
            WorkspaceItemView.delete(selectable)
           elif selectable.type() == WireView:
             WorkspaceItemView.delete(selectable)'''
