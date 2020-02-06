from typing import List, Type

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea

from ..Item.ItemEnum import ItemEnum
from ..Item.ListItemView import ListItemView
from ..View import View


class ItemListViewMeta(type(QWidget), type(View)):
    pass


class ItemListView(QScrollArea, View, metaclass=ItemListViewMeta):
    """Class for displaying a list of items"""
    def __init__(self, main: QWidget, type: Type[ItemEnum]):
        super().__init__()

        self.__items: List[ListItemView] = []

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 15, 0, 15)
        layout.setSpacing(20)

        for item in list(type):
            new = ListItemView(main, item)
            self.__items.append(new)
            layout.addWidget(new)

        widget = QWidget()
        widget.setObjectName("scroll")
        widget.setLayout(layout)
        self.setStyleSheet("""
            QScrollArea{
                background: white;
                border: 0px;
            }
            QWidget#scroll{
                background: white
            }""")
        self.setAlignment(Qt.AlignHCenter)
        self.setWidget(widget)
