from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

from ..SystemInfo import SystemInfo
from .Translator import Translator


class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.__init_ui()

    def __init_ui(self):
        self.setFixedSize(300, 350)
        self.setWindowTitle(Translator.tr("Über"))
        self.setWindowIcon(QIcon(SystemInfo.RESOURCES + 'images/PhiPi_icon.png'))
        self.setWindowModality(Qt.ApplicationModal)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        font = SystemInfo.FONT

        font.setPointSize(15)
        title = QLabel("PhyPiGUI", self)
        title.setFont(font)

        font.setPointSize(10)
        desc = QLabel(self)
        desc.setText(Translator.tr("Beschreibung\n"
                                   "Beschreibung\n"
                                   "Beschreibung"))
        desc.setFont(font)

        layout.addWidget(title)
        layout.addWidget(desc)
        layout.addStretch(1)

        self.setLayout(layout)