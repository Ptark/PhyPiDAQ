from PyQt5.QtCore import QObject, pyqtSignal


class GlobalSignals:

    class Signal(QObject):
        signal = pyqtSignal()

    about_to_quit: Signal = Signal()
