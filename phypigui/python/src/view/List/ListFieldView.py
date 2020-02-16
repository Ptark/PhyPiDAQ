from typing import NoReturn, List

from PyQt5.QtCore import Qt, QSize, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QWidget, QLineEdit, QGroupBox

from ...SystemInfo import SystemInfo
from ..Item.ItemEnum import SensorEnum, OperatorEnum, DiagramEnum
from ..Translator import Translator
from .ItemListView import ItemListView
from ..View import View


icon_path = SystemInfo.RESOURCES + 'images/items/'


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
        self.__search: QLineEdit = QLineEdit()
        self.__group: QGroupBox = QGroupBox()
        self.__layout: QVBoxLayout = QVBoxLayout(self)
        self.__group_layout: QVBoxLayout = QVBoxLayout(self.__group)

        self.__lists: List[ItemListView] = [
            ItemListView(main, list(SensorEnum)),
            ItemListView(main, list(OperatorEnum)),
            ItemListView(main, list(DiagramEnum))]
        self.__icons: List[QIcon] = [
            QIcon(icon_path + "sensor/distance.svg"),
            QIcon(icon_path + "operator/addition.svg"),
            QIcon(icon_path + "diagram/time.svg")]

        self.__new_search: bool = True
        self.__last_list: ItemListView = self.__lists[0]

        Translator.language_changed.signal.connect(self.__update_text)
        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        self.__group.setStyleSheet("QGroupBox { border: 1px solid gray }")
        self.__layout.addWidget(self.__group)
        self.__group_layout.addWidget(self.__tab)
        self.__group_layout.addWidget(self.__search)
        self.setLayout(self.__layout)

        self.__tab.setElideMode(Qt.ElideRight)
        self.__tab.setIconSize(QSize(35, 35))
        self.__tab.setStyleSheet("QTabBar::tab { height: 45px; width: 68px; }")

        for i in range(0, 3):
            self.__tab.addTab(self.__lists[i], self.__icons[i], "")

        self.__search.setClearButtonEnabled(True)
        self.__search.textChanged.connect(self.__update_search)

        self.__update_text()

    def __update_text(self):
        self.__tab.setTabToolTip(0, Translator.tr("Sensoren"))
        self.__tab.setTabToolTip(1, Translator.tr("Operatoren"))
        self.__tab.setTabToolTip(2, Translator.tr("Diagramme"))
        self.__search.setPlaceholderText(Translator.tr("Suchen"))

    @pyqtSlot(str)
    def __update_search(self, search: str):
        index = self.__tab.currentIndex()
        if search == "":
            self.__new_search = True
            self.__tab.removeTab(index)
            self.__tab.insertTab(index, self.__lists[index], self.__icons[index], "")
            self.__tab.setCurrentIndex(index)

            for i in range(0, 3):
                self.__tab.setTabEnabled(i, True)
        else:
            if self.__new_search is True:
                self.__new_search = False
                self.__last_list = self.__tab.currentWidget()

                for i in range(0, 3):
                    self.__tab.setTabEnabled(i, False)

            all_items = list(SensorEnum) + list(OperatorEnum) + list(DiagramEnum)
            result = [x for x in all_items if search.lower() in Translator.tr(x.model.get_name()).lower()]
            widget = ItemListView(self.__main, result)

            self.__tab.removeTab(index)
            self.__tab.insertTab(index, widget, self.__icons[index], "")
            self.__tab.setCurrentIndex(index)
