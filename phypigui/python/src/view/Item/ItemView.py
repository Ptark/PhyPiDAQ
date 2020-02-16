from abc import ABC
from typing import NoReturn

from PyQt5.QtCore import Qt
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QWidget, QFrame, QHBoxLayout

from ..View import View


class ItemViewMeta(type(QFrame), type(View)):
    pass


class ItemView(QFrame, View, ABC, metaclass=ItemViewMeta):
    """Abstract class for displaying an item

        Attributes:
            parent (QWidget): A parent widget.
            icon_path (str): A file path of the icon displayed on the item.
    """
    def __init__(self, parent: QWidget, item: 'ItemEnum'):
        super().__init__(parent)

        self._enum: 'ItemEnum' = item

        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        self.setFixedSize(120, 60)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setObjectName("item")

        self.setStyleSheet("""
            QFrame#item {
                border: 2px solid black;
                border-radius: 5px;
                background-color: """ + self._enum.background_color + """;
                }
            """)

        icon = QSvgWidget(self)
        icon.load(self._enum.path)
        icon.setFixedSize(40, 40)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(icon)
        self.setLayout(layout)
