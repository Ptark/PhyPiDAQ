from typing import NoReturn

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QWidget

from ...SystemInfo import SystemInfo
from ..Item.ItemEnum import SensorEnum, OperatorEnum, DiagramEnum
from ..Translator import Translator
from .ItemListView import ItemListView
from ..View import View


class ListFieldViewMeta(type(QWidget), type(View)):
    pass


class ListFieldView(QWidget, View, metaclass=ListFieldViewMeta):
    """Class for displaying the three lists of items

        Attributes:
            main (QWidget): The main widget.
    """
    def __init__(self, main: QWidget):
        super().__init__()

        self.__main = main
        self.__tab: QTabWidget = QTabWidget()
        self.__sensor_list: ItemListView = ItemListView(main, SensorEnum)
        self.__operator_list: ItemListView = ItemListView(main, OperatorEnum)
        self.__diagram_list: ItemListView = ItemListView(main, DiagramEnum)

        Translator.language_changed.signal.connect(self.__update_text)

        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        self.__tab.setElideMode(Qt.ElideRight)
        self.__tab.setIconSize(QSize(35, 35))

        icon_path = SystemInfo.RESOURCES + 'images/items/'

        self.__tab.setStyleSheet("QTabBar::tab { height: 45px; width: 62px; }"
                                 "QTabWidget { border: 1px solid gray}")

        self.__tab.addTab(self.__sensor_list, QIcon(icon_path + "sensor/distance.svg"), "")
        self.__tab.addTab(self.__operator_list, QIcon(icon_path + "operator/addition.svg"), "")
        self.__tab.addTab(self.__diagram_list, QIcon(icon_path + "diagram/time.svg"), "")

        layout = QVBoxLayout()
        layout.addWidget(self.__tab)
        self.setLayout(layout)
        self.setFixedWidth(206)

        self.__update_text()

    def __update_text(self):
        self.__tab.setTabToolTip(0, Translator.tr("Sensoren"))
        self.__tab.setTabToolTip(1, Translator.tr("Operatoren"))
        self.__tab.setTabToolTip(2, Translator.tr("Diagramme"))
