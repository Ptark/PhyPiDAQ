from typing import Type, NoReturn

from PyQt5.QtWidgets import QWidget

from .ItemView import ItemView
from .WorkspaceItemView import WorkspaceItemView


class ListItemView(ItemView):
    def __init__(self, main: QWidget, item: Type[WorkspaceItemView]):
        super().__init__(None)

        self.__visible: bool = True
        self.__item: Type[WorkspaceItemView] = item

    def is_visible(self) -> bool:
        return self.__visible

    def set_visible(self, visible: bool) -> NoReturn:
        self.__visible = visible
