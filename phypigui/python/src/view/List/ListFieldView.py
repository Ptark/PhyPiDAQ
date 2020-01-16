from typing import NoReturn

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout

from ..Item.DiagramItemView import *
from ..Item.ListItemView import ListItemView
from ..Item.OperatorItemView import *
from ..Item.SensorItemView import *
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
        self.__sensor_list.add_item(ListItemView(self.__main, AccelerationSensorItemView))
        self.__sensor_list.add_item(ListItemView(self.__main, DistanceSensorItemView))
        self.__sensor_list.add_item(ListItemView(self.__main, ForceSensorItemView))
        self.__sensor_list.add_item(ListItemView(self.__main, TemperatureSensorItemView))

        self.__operator_list.add_item(ListItemView(self.__main, AbsoluteOperatorItemView))
        self.__operator_list.add_item(ListItemView(self.__main, DivisionOperatorItemView))
        self.__operator_list.add_item(ListItemView(self.__main, MultiplicationOperatorItemView))
        self.__operator_list.add_item(ListItemView(self.__main, SubtractionOperatorItemView))
        self.__operator_list.add_item(ListItemView(self.__main, AdditionOperatorItemView))

        self.__diagram_list.add_item(ListItemView(self.__main, DualDiagramItemView))
        self.__diagram_list.add_item(ListItemView(self.__main, BarDiagramItemView))
        self.__diagram_list.add_item(ListItemView(self.__main, TimeDiagramItemView))

    def __init_ui(self) -> NoReturn:
        self.__tab.setElideMode(Qt.ElideRight)

        self.__tab.addTab(self.__sensor_list, "&Sensoren")
        self.__tab.addTab(self.__operator_list, "&Operatoren")
        self.__tab.addTab(self.__diagram_list, "&Diagramme")

        layout = QVBoxLayout()
        layout.addWidget(self.__tab)
        self.setLayout(layout)
