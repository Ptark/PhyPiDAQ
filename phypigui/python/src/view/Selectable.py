from abc import ABC, abstractmethod
from typing import NoReturn

from PyQt5.QtWidgets import QWidget

from .Workspace.WorkspaceView import WorkspaceView


class Selectable(ABC):
    def __init__(self):
        self.__selected: bool = False

    @property
    def selected(self) -> bool:
        return self.__selected

    @selected.setter
    def selected(self, new_selected: bool) -> NoReturn:
        if self.__selected == new_selected:
            return

        self.__selected = new_selected

        if self.selected:
            if WorkspaceView.selection is not None:
                WorkspaceView.selection.selected = False
            WorkspaceView.selection = self
        else:
            WorkspaceView.selection = None

        self._change_selected_view()

    @abstractmethod
    def _change_selected_view(self) -> NoReturn:
        pass

    @abstractmethod
    def get_info_widget(self) -> QWidget:
        pass

    @abstractmethod
    def open_config(self) -> NoReturn:
        pass

    @abstractmethod
    def delete(self) -> NoReturn:
        pass
