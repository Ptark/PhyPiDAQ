from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget
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
        self.resize(800, 600)
        screen = QtWidgets.QDesktopWidget().screenGeometry(-1)
        window_width = screen.width() / 2
        window_height = screen.height() / 2

        # TODO: Abschnitte hinzufügen
        InfoBarView(self)
        DiagramFieldView(self)
        WorkspaceView(self)

        self.show()


