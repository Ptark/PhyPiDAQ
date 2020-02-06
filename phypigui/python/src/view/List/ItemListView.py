from typing import List, Type

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from ..Item.ItemEnum import ItemEnum
from ..Item.ListItemView import ListItemView
from ..View import View


class ItemListViewMeta(type(QWidget), type(View)):
    pass


class ItemListView(QWidget, View, metaclass=ItemListViewMeta):
    """Class for displaying a list of items"""
    def __init__(self, main: QWidget, type: Type[ItemEnum]):
        super().__init__()

        self.__items: List[ListItemView] = []

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 20, 0, 0)
        layout.setSpacing(20)

        for item in list(type):
            new = ListItemView(main, item)
            self.__items.append(new)
            layout.addWidget(new)

        layout.addStretch(1)

        centering = QHBoxLayout()
        centering.setContentsMargins(0, 0, 0, 0)
        centering.addLayout(layout)
        self.setLayout(centering)