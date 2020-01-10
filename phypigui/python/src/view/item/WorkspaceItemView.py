from abc import ABC

from PyQt5.QtWidgets import QWidget

from python.src.view.Selectable import Selectable
from python.src.view.WorkSpace import WorkspaceView
from python.src.view.item.ItemView import ItemView


class WorkspaceItemView(ABC, ItemView, Selectable):
    def __init__(self, parent: QWidget, id: int, icon_path: str):
        super().__init__(parent, id, icon_path)
        # TODO: Klassenvariablen

    def get_info_widget(self) -> QWidget:
        return self.__info_widget

    def delete(self) -> None:
        WorkspaceView.delete_item(self)