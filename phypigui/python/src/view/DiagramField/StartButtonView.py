from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton

# from ...model.manager import ManagerModel


class StartButtonView(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)

        self.__is_started = False
        self.__start_icon = QIcon("../resources/images/buttons/start.svg")
        self.__stop_icon = QIcon("../resources/images/buttons/stop.svg")

        self.setFixedSize(31, 31)
        self.setIcon(self.__start_icon)
        self.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        if self.__is_started:
            # ManagerModel.stop()
            self.setIcon(self.__start_icon)
        else:
            # ManagerModel.start()
            self.setIcon(self.__stop_icon)

        self.__is_started = not self.__is_started
