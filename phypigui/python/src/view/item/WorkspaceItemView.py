from abc import ABC
from typing import List, NoReturn

from PyQt5.QtWidgets import QWidget

from ...model.item.ItemModel import ItemModel
from ..Selectable import Selectable
from ..Workspace.WorkspaceView import WorkspaceView
from .ItemView import ItemView
from .OutputView import OutputView
from .InputView import InputView


class WorkspaceItemView(ABC, ItemView, Selectable):
    def __init__(self, parent: QWidget, id: int, icon_path: str):
        super().__init__(parent, id, icon_path)

        self.__model: ItemModel = None
        self.__selected: bool = False
        self.__inputs: List[InputView] = []
        self.__outputs: List[OutputView] = []
        self.__info_widget: QWidget = QWidget(None, None)  # TODO: parent sollte infobarview sein, wie bekommt man das??

    def get_info_widget(self) -> QWidget:
        return self.__info_widget

    def delete(self) -> NoReturn:
        WorkspaceView.delete_item(self)
