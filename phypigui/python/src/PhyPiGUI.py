import sys

from PyQt5.QtCore import QTranslator, QLocale
from PyQt5.QtWidgets import QApplication

from python.src.view.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    locale = QLocale.system().name()
    #locale = "en"

    translator = QTranslator()
    if translator.load("phypigui_" + locale, "../resources/languages"):
        app.installTranslator(translator)

    window = MainWindow()
    sys.exit(app.exec_())
