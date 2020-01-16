from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QMainWindow

from .MenuBar.MenuBarView import MenuBarView
from .List.ListFieldView import ListFieldView
from .DiagramField.DiagramFieldView import DiagramFieldView
from .InfoBar.InfoBarView import InfoBarView
from .Workspace.WorkspaceView import WorkspaceView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__main_widget = QWidget()

        self.__list_field = ListFieldView(self.__main_widget)
        self.__workspace_field = WorkspaceView(None)
        self.__infobar_field = InfoBarView(None)
        self.__diagram_field = DiagramFieldView(None)

        self.__init_ui()

    def __init_ui(self):
        self.setWindowTitle('PhyPiDAQ')
        self.setWindowIcon(QIcon('../../../images/PhiPi_icon.png'))

        self.setMenuBar(MenuBarView())
        self.setCentralWidget(self.__main_widget)

        screen = QtWidgets.QDesktopWidget().screenGeometry(-1)
        window_width = screen.width() / 2
        window_height = screen.height() / 2
        self.resize(window_width, window_height)
        self.setMinimumSize(800, 600)

        layout_middle = QVBoxLayout()
        layout_middle.addWidget(self.__workspace_field, 7)
        layout_middle.addWidget(self.__infobar_field, 2)

        layout = QHBoxLayout()
        layout.addWidget(self.__list_field, 2)
        layout.addLayout(layout_middle, 7)
        layout.addWidget(self.__diagram_field, 3)

        self.__main_widget.setLayout(layout)

        self.show()
