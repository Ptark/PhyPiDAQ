from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton

from python.src.view.Workspace.WorkspaceView import WorkspaceView


# from python.src.view.item.WorkspaceItemView import WorkspaceItemView


class DeleteButtonView(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(360, 20, 31, 31))
        self.setText("del")
        self.setObjectName("DeleteButtonView")

    def on_click(self):
        selectable = WorkspaceView.get_selectable()  # todo: WorspaceItemView raises an error

        ''' if selectable.type() == WorkspaceItemView:          
            WorkspaceItemView.delete(selectable)
           elif selectable.type() == WireView:
             WorkspaceItemView.delete(selectable)'''
