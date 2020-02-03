from typing import NoReturn

from PyQt5.QtCore import pyqtSlot, QRunnable, QThreadPool
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton

from ...GlobalSignals import GlobalSignals
from ..Translator import Translator
from ...model.manager.ManagerModel import ManagerModel


class StartButtonView(QPushButton):

    class Start(QRunnable):
        def run(self) -> NoReturn:
            ManagerModel.start()

    __button: 'StartButtonView'

    def __init__(self, parent):
        super().__init__(parent)

        StartButtonView.__button = self

        self.__is_started = False
        self.__start_icon = QIcon("../resources/images/buttons/start.svg")
        self.__stop_icon = QIcon("../resources/images/buttons/stop.svg")

        self.setFixedSize(31, 31)
        self.setIcon(self.__start_icon)

        self.clicked.connect(self.__on_click)
        GlobalSignals.about_to_quit.signal.connect(ManagerModel.stop)
        Translator.language_changed.signal.connect(self.__update_text)

        self.__update_text()

    def __update_text(self):
        tooltip = "Stop" if self.__is_started else "Start"
        self.setToolTip(Translator.tr(tooltip))

    @pyqtSlot()
    def __on_click(self) -> NoReturn:
        if self.__is_started:
            ManagerModel.stop()
            self.setIcon(self.__start_icon)
        else:
            QThreadPool.globalInstance().start(self.Start())
            self.setIcon(self.__stop_icon)

        self.__is_started = not self.__is_started

        self.__update_text()
        self.clearFocus()

    @staticmethod
    def click() -> NoReturn:
        StartButtonView.__button.__on_click()
