import time
from typing import NoReturn

from PyQt5.QtCore import pyqtSignal, QThread, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton

from ..DialogView import DialogView
from ...model.ModelExceptions import PathDoesntExist
from ...SystemInfo import SystemInfo
from ...GlobalSignals import GlobalSignals
from ..Translator import Translator
from ...model.manager.ManagerModel import ManagerModel


error_boxes = {'info': DialogView.show_info, 'warn': DialogView.show_warning, 'error': DialogView.show_error}


class StartButtonView(QPushButton):
    """This class represents the start button"""

    class Start(QThread):
        error_occurred: pyqtSignal = pyqtSignal(str, str, str)

        def run(self) -> NoReturn:
            try:
                ManagerModel.start()
            except PathDoesntExist as e:
                self.error_occurred.emit(Translator.tr("Dateipfad nicht gefunden"), str(e), 'warn')
            except Exception as e:
                print("ManagerModel Error: %s" % str(e))

    __button: 'StartButtonView'
    start_signal = pyqtSignal()
    start_time: float = 0.0

    def __init__(self):
        super().__init__()

        StartButtonView.__button = self

        button_path = SystemInfo.RESOURCES + 'images/buttons/'

        self.__is_started = False
        self.__start_icon = QIcon(button_path + 'start.svg')
        self.__stop_icon = QIcon(button_path + 'stop.svg')
        self.__thread: StartButtonView.Start = StartButtonView.Start()

        self.setFixedSize(31, 31)
        self.setIcon(self.__start_icon)

        self.clicked.connect(self.__on_click)
        self.__thread.error_occurred.connect(self.__show_error)
        GlobalSignals.about_to_quit.signal.connect(ManagerModel.stop)
        Translator.language_changed.signal.connect(self.__update_text)

        self.__update_text()
        print(DialogView.show_warning)

    def __update_text(self):
        tooltip = "Stop" if self.__is_started else "Start"
        self.setToolTip(Translator.tr(tooltip))

    def __on_click(self) -> NoReturn:
        if self.__is_started:
            self.stop()
        else:
            self.start()

        self.clearFocus()

    def start(self) -> NoReturn:
        if not self.__is_started:
            if not self.__thread.isRunning():
                StartButtonView.start_time = time.time()
                self.__thread.start()
                self.start_signal.emit()
            self.setIcon(self.__stop_icon)
            self.__is_started = True
            self.__update_text()

    def stop(self) -> NoReturn:
        if self.__is_started:
            ManagerModel.stop()
            self.__thread.wait()
            self.setIcon(self.__start_icon)
            self.__is_started = False
            self.__update_text()

    @pyqtSlot(str, str, str)
    def __show_error(self, title: str, description: str, message_type: str = 'error') -> NoReturn:
        error_boxes[message_type](title, description + '.')
        self.stop()

    @staticmethod
    def click() -> NoReturn:
        """a static method of on_click that executes the running of the program on the Managermodel"""
        StartButtonView.__button.__on_click()

    @staticmethod
    def interrupt_mp() -> bool:
        """Interrupt a measurement process in the model and set StartButtonView on 'stop-state'

        Returns:
            bool: True, if there was a measurement process running
        """
        was_running: bool = StartButtonView.__button.__is_started
        StartButtonView.__button.stop()
        return was_running

    @staticmethod
    def start_mp() -> NoReturn:
        """Starts a measurement process in the model and set StartButtonView on 'start-state'"""
        StartButtonView.__button.start()

    @staticmethod
    def restart() -> NoReturn:
        """Restarts a measurement process in the model"""
        StartButtonView.__button.stop()
        StartButtonView.__button.start()
