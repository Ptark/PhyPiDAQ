from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget


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
        self.setGeometry(int(window_width / 2), int(window_height / 2), int(window_width), int(window_height))

        # TODO: Abschnitte hinzufügen

        self.showMaximized()
