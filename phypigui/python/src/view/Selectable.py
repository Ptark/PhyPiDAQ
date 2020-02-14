from abc import ABC, abstractmethod
from typing import NoReturn

from PyQt5.QtWidgets import QWidget

from .InfoBar.DeleteButtonView import DeleteButtonView
from ..model.manager.ManagerModel import ManagerModel
from .InfoBar.InfoBarView import InfoBarView
from .Workspace.WorkspaceView import WorkspaceView


class Selectable(ABC):
    """Abstract class for a selectable workspace component

        Selectable workspace components are for example items and connections.
    """
    def __init__(self):
        self.__selected: bool = False

    @property
    def selected(self) -> bool:
        """Returns if the selectable is selected

            Return:
                bool: If the selectable is selected.
        """
        return self.__selected

    @selected.setter
    def selected(self, new_selected: bool) -> NoReturn:
        """Sets the selected status

            This also updates the Workspace and the old selection
            because only one selection at the same time is allowed.

            Args:
                new_selected (bool): New selected state
        """
        if self.__selected == new_selected:
            return

        self.__selected = new_selected

        if self.selected:
            if WorkspaceView.selection is not None:
                WorkspaceView.selection.selected = False
            WorkspaceView.selection = self
        else:
            WorkspaceView.selection = None

        self._select()
        self._update_selected_view()
        InfoBarView.refresh_infobar()

    @abstractmethod
    def _update_selected_view(self) -> NoReturn:
        """Checks if the component is selected and updates the its appearance accordingly"""
        pass

    @abstractmethod
    def get_info_widget(self) -> QWidget:
        """Returns an widget which hold information about the component

            The widget is usually used for the info bar.

            Returns:
                QWidget: Widget with components information.
        """
        pass

    @abstractmethod
    def open_config(self) -> NoReturn:
        """Opens the components configuration window"""
        pass

    @abstractmethod
    def delete(self) -> NoReturn:
        """Deletes the component from the workspace"""
        if WorkspaceView.selection is self:
            ManagerModel.set_selected_item(None)
            WorkspaceView.selection = None
            InfoBarView.refresh_infobar()

    def _select(self) -> NoReturn:
        pass
