from typing import NoReturn

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout

from python.src.view.Item.ListItemView import ListItemView
from .ItemListView import ItemListView


class ListFieldView(QWidget):
    def __init__(self, main: QWidget):
        super().__init__()

        self.__main = main
        self.__tab: QTabWidget = QTabWidget()
        self.__sensor_list: ItemListView = ItemListView()
        self.__operator_list: ItemListView = ItemListView()
        self.__diagram_list: ItemListView = ItemListView()

        self.__init_items()
        self.__init_ui()

    def __init_items(self) -> NoReturn:
        self.__sensor_list.add_item(ListItemView(self.__main, None))

        self.__operator_list.add_item(ListItemView(self.__main, None))

        self.__diagram_list.add_item(ListItemView(self.__main, None))

    def __init_ui(self) -> NoReturn:
        self.__tab.setElideMode(Qt.ElideRight)

        self.__tab.addTab(self.__sensor_list, "&Sensoren")
        self.__tab.addTab(self.__operator_list, "&Operatoren")
        self.__tab.addTab(self.__diagram_list, "&Diagramme")

        layout = QVBoxLayout()
        layout.addWidget(self.__tab)
        self.setLayout(layout)
