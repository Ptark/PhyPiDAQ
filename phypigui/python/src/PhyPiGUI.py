import sys

from PyQt5.QtCore import QLocale
from PyQt5.QtWidgets import QApplication

from phypigui.python.src.GlobalSignals import GlobalSignals
from phypigui.python.src.view.MainWindow import MainWindow
from phypigui.python.src.view.Translator import Translator

if __name__ == '__main__':
    app = QApplication(sys.argv)

    locale = QLocale.system().language()
    Translator.install_translator(locale)

    window = MainWindow()
    app.aboutToQuit.connect(GlobalSignals.about_to_quit.signal.emit)
    sys.exit(app.exec_())
