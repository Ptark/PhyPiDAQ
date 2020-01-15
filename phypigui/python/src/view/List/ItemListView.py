from typing import NoReturn, List

from PyQt5.QtWidgets import QWidget, QVBoxLayout

from ..Item.ListItemView import ListItemView


class ItemListView(QWidget):
    def __init__(self):
        super().__init__()

        self.__items: List[ListItemView] = []
        self.__layout = QVBoxLayout()
        self.setLayout(self.__layout)

    def add_item(self, item: ListItemView) -> NoReturn:
        self.__items.append(item)
        self.__layout.addWidget(item)