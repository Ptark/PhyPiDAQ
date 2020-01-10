from abc import ABC
from typing import List

from PyQt5.QtWidgets import QWidget

from python.src.model.item import ItemModel
from python.src.view.Selectable import Selectable
from python.src.view.WorkSpace import WorkspaceView
from python.src.view.item.InputView import InputView
from python.src.view.item.ItemView import ItemView
from python.src.view.item.OutputView import OutputView


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

    def delete(self) -> None:
        WorkspaceView.delete_item(self)