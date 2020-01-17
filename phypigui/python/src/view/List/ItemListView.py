from typing import NoReturn, List

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from ..Item.ListItemView import ListItemView
from ..View import View


class ItemListViewMeta(type(QWidget), type(View)):
    pass


class ItemListView(QWidget, View, metaclass=ItemListViewMeta):
    def __init__(self):
        super().__init__()

        self.__items: List[ListItemView] = []
        self.__layout = QVBoxLayout()
        self.__layout.addSpacing(10)
        self.__layout.addStretch(1)

        centering = QHBoxLayout()
        centering.addLayout(self.__layout)
        self.setLayout(centering)

    def add_item(self, item: ListItemView) -> NoReturn:
        self.__items.append(item)
        self.__layout.insertWidget(1, item)
        self.__layout.insertSpacing(2, 20)
