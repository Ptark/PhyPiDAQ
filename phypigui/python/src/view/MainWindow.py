from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QMainWindow

from .MenuBar.MenuBarView import MenuBarView
from .List.ListFieldView import ListFieldView
from .DiagramField.DiagramFieldView import DiagramFieldView
from .InfoBar.InfoBarView import InfoBarView
from .Workspace.WorkspaceView import WorkspaceView

from ..model.config import ConfigModel, NumOption, EnumOption, FileOption, BoolOption
from ..view.config import ConfigView
from .EnumTest import EnumTest
import enum


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__main_widget = QWidget(self)

        self.__list_field = ListFieldView(self.__main_widget)
        self.__workspace_field = WorkspaceView(self.__main_widget)
        self.__infobar_field = InfoBarView(None)
        self.__diagram_field = DiagramFieldView(None)
        self.__config_window = None

        self.__init_ui()

    def __init_ui(self):
        self.setWindowTitle('PhyPiDAQ')
        self.setWindowIcon(QIcon('../resources/images/PhiPi_icon.png'))

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
        config = ConfigModel.ConfigModel()
        config.add_file_option(FileOption.FileOption("FileOption1", "1234567890123456789012", FileOption.FileOption.ANYFILE))
        config.add_file_option(FileOption.FileOption("1234567890123456789012", "Bescheibung\n tüdelü", FileOption.FileOption.EXISTINGFILE))
        config.add_file_option(FileOption.FileOption("", "", FileOption.FileOption.DIR))
        config.add_file_option(FileOption.FileOption("Mit Name", "", FileOption.FileOption.ANYFILE, 'Textdokumente', ['txt', 'tex', 'pdf']))
        config.add_file_option(FileOption.FileOption("Ohne Name", "", FileOption.FileOption.ANYFILE, '', ['png', 'ahmad']))
        #for i in range(0, 100):
        #    config.add_num_option(NumOption.NumOption(i.__str__(), 0))
        self.__config_window = ConfigView.ConfigView("Item", config)

        self.show()
