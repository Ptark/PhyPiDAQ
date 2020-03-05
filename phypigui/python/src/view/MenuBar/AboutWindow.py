from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

from ...SystemInfo import SystemInfo
from ..Translator import Translator


class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.__init_ui()

    def __init_ui(self):
        self.setFixedSize(350, 350)
        self.setWindowTitle(Translator.tr("Über"))
        self.setWindowIcon(QIcon(SystemInfo.RESOURCES + 'images/PhiPi_icon.png'))
        self.setWindowModality(Qt.ApplicationModal)

        font = QFont(SystemInfo.FONT)

        icon = QLabel(self)
        img = QPixmap(SystemInfo.RESOURCES + 'images/PhiPi_icon.png')
        icon.setPixmap(img)

        title = QLabel("PhyPiGUI", self)
        font.setPointSize(15)
        title.setFont(font)

        version = QLabel('v' + SystemInfo.VERSION, self)
        font.setPointSize(10)
        version.setFont(font)

        description = QLabel(self)
        font.setPointSize(10)
        description.setFont(font)
        description.setWordWrap(True)
        description.setAlignment(Qt.AlignCenter)
        description.setText(Translator.tr("PhyPiGUI ist ein Softwareprojekt, dass im Rahmen von Praxis der "
                                          "Softwareentwicklung am Karlsruher Institut für Technologie entstanden ist")
                            + ".\n\n" +
                            Translator.tr("Es bietet eine für Schüler ausgelegte grafische Benutzeroberfläche "
                                          "zur vereinfachten Benutzung der Software PhyPiDAQ von Günter Quast")
                            + ".")

        authors = QLabel("Simon Essig | Christian Hauser | Fritz Hund\nAhmad Jayossi | Sandro Negri")
        font.setPointSize(8)
        authors.setFont(font)
        authors.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 10)
        layout.setSpacing(0)

        layout.addWidget(icon, alignment=Qt.AlignCenter)
        layout.addSpacing(5)
        layout.addWidget(title, alignment=Qt.AlignCenter)
        layout.addWidget(version, alignment=Qt.AlignCenter)
        layout.addSpacing(15)
        layout.addWidget(description, alignment=Qt.AlignCenter)
        layout.addStretch(1)
        layout.addWidget(authors, alignment=Qt.AlignCenter)
        layout.addSpacing(3)

        self.setLayout(layout)
