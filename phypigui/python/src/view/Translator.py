from typing import Dict
from xml.dom import minidom

from PyQt5.QtCore import QLocale, pyqtSignal, QObject

path = '../resources/languages/'


class Signal(QObject):
    signal = pyqtSignal()


class Translator:
    __translator: Dict[str, str] = None
    language_changed: Signal = Signal()

    @staticmethod
    def install_translator(language: int) -> bool:
        if language == QLocale.German:
            Translator.__translator = None
        else:
            try:
                items = minidom.parse(path + QLocale(language).name() + '.xml').getElementsByTagName('item')
            except FileNotFoundError:
                return False

            Translator.__translator = {}
            for item in items:
                Translator.__translator[item.childNodes[1].firstChild.data] = item.childNodes[3].firstChild.data

        Translator.language_changed.signal.emit()
        return True

    @staticmethod
    def tr(original: str) -> str:
        if Translator.__translator is None:
            return original

        translated = Translator.__translator.get(original)
        if translated is None:
            print("No existing translation for " + original)
            return original

        return translated
