from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

from .DiagramField.DiagramFieldView import DiagramFieldView
from .InfoBar.InfoBarView import InfoBarView
from .Workspace.WorkspaceView import WorkspaceView


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.__init_ui()

    def __init_ui(self):
        self.setWindowTitle('PhyPiDAQ')
        self.setWindowIcon(QIcon('../../../images/PhiPi_icon.png'))

        screen = QtWidgets.QDesktopWidget().screenGeometry(-1)
        window_width = screen.width() / 2
        window_height = screen.height() / 2
        self.resize(window_width, window_height)
        self.setMinimumSize(800, 600)

        list_field = QWidget()  # ListFieldView(None)
        workspace_field = WorkspaceView(None)
        infobar_field = InfoBarView(None)
        diagram_field = DiagramFieldView(None)

        layout_middle = QVBoxLayout()
        layout_middle.addWidget(workspace_field, 7)
        layout_middle.addWidget(infobar_field, 2)

        layout = QHBoxLayout()
        layout.addWidget(list_field, 2)
        layout.addLayout(layout_middle, 7)
        layout.addWidget(diagram_field, 3)

        self.setLayout(layout)

        self.show()


