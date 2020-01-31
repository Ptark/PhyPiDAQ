import sys

from PyQt5.QtCore import QLocale
from PyQt5.QtWidgets import QApplication

from python.src.view.MainWindow import MainWindow
from python.src.view.Translator import Translator

if __name__ == '__main__':
    app = QApplication(sys.argv)

    locale = QLocale.system().language()
    Translator.install_translator(locale)

    """
    translator = QTranslator()
    if translator.load("phypigui_" + locale, "../resources/languages"):
        app.installTranslator(translator)
    """

    window = MainWindow()
    sys.exit(app.exec_())
