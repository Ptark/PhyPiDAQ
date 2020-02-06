import sys

from PyQt5.QtCore import QLocale
from PyQt5.QtWidgets import QApplication

from .SystemInfo import SystemInfo
from .GlobalSignals import GlobalSignals
from .view.MainWindow import MainWindow
from .view.Translator import Translator


def run():
    app = QApplication(sys.argv)

    SystemInfo.init()

    locale = QLocale.system().language()
    Translator.install_translator(locale)

    window = MainWindow()
    app.aboutToQuit.connect(GlobalSignals.about_to_quit.signal.emit)
    sys.exit(app.exec_())
