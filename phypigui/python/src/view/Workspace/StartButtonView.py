from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QEvent, pyqtSlot
from PyQt5.QtWidgets import QPushButton

#from python.src.model.manager.ManagerModel import ManagerModel


class StartButtonView(QPushButton):
    __start_image = "../resources/images/buttons/startknopf.png"
    __stop_image = "../resources/images/buttons/stoppknopf.png"
    is_started = False

    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(31,31)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(StartButtonView.__start_image))
        self.setIcon(self.icon)
        self.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        if not self.is_started:
            #ManagerModel.start()
            self.change_icon()
            self.is_started = True
        else:
            #ManagerModel.stop()
            self.change_icon()
            self.is_started = False

    def change_icon(self):
        if self.is_started:
            self.icon.addPixmap(QtGui.QPixmap(self.__start_image))
            self.setIcon(self.icon)
        else:
            self.icon.addPixmap(QtGui.QPixmap(self.__stop_image))
            self.setIcon(self.icon)
