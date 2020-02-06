from typing import NoReturn

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QKeyEvent
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QMainWindow

from ..SystemInfo import SystemInfo
from .KeyboardHandler import KeyboardHandler
from .MenuBar.MenuBarView import MenuBarView
from .List.ListFieldView import ListFieldView
from .DiagramField.DiagramFieldView import DiagramFieldView
from .InfoBar.InfoBarView import InfoBarView
from .Workspace.WorkspaceView import WorkspaceView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__main_widget = QWidget(self)

        self.__list_field = ListFieldView(self.__main_widget)
        self.__workspace_field = WorkspaceView(self.__main_widget)
        self.__infobar_field = InfoBarView(None)
        self.__diagram_field = DiagramFieldView(None)

        self.__infobar_group: QtWidgets.QGroupBox = QtWidgets.QGroupBox(self)
        self.__infobar_layout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout(self.__infobar_group)
        self.__infobar_layout.addWidget(self.__infobar_field)

        self.__diagram_group: QtWidgets.QGroupBox = QtWidgets.QGroupBox(self)
        self.__diagram_layout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout(self.__diagram_group)
        self.__diagram_layout.addWidget(self.__diagram_field)

        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        self.setWindowTitle('PhyPiDAQ')
        self.setWindowIcon(QIcon(SystemInfo.RESOURCES + 'images/PhiPi_icon.png'))

        self.setMenuBar(MenuBarView())
        self.setCentralWidget(self.__main_widget)

        screen = QtWidgets.QDesktopWidget().screenGeometry(-1)
        window_width = screen.width() / 2
        window_height = screen.height() / 2
        self.resize(window_width, window_height)
        self.setMinimumSize(800, 600)

        layout_middle = QVBoxLayout()
        layout_middle.addWidget(self.__workspace_field, 7)
        self.__workspace_field.setStyleSheet("QWidget { margin: 0px; }")
        layout_middle.addWidget(self.__infobar_group, 2)

        self.__infobar_group.setStyleSheet("QGroupBox { margin: 9px; border: 1px solid gray; }")

        layout = QHBoxLayout()
        layout.addWidget(self.__list_field, 2)
        layout.addLayout(layout_middle, 7)
        layout.addWidget(self.__diagram_group, 3)
        self.__diagram_group.setStyleSheet("QGroupBox { margin-bottom: 9px; margin-top: 9px; margin-right: 4px;"
                                           " border: 1px solid grey; }")

        self.__main_widget.setLayout(layout)

        self.show()

    def keyPressEvent(self, event: QKeyEvent) -> NoReturn:
        KeyboardHandler.key_pressed(event)
