from typing import NoReturn, List

from PyQt5.QtWidgets import QWidget

from ...model.manager.ManagerModel import ManagerModel
from ..Workspace.WorkspaceView import WorkspaceView
from ...model.item.OperatorItems.OperatorItem import OperatorItem
from .WorkspaceItemView import WorkspaceItemView


class OperatorItemView(WorkspaceItemView):
    """Abstract class for displaying an item of an operator on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    def __init__(self, parent: QWidget, operator: 'OperatorEnum'):
        self._model: OperatorItem = operator.model()

        super().__init__(parent, operator.path, self._model.get_input_ids(), self._model.get_output_ids())

    def _on_click(self) -> NoReturn:
        if WorkspaceView.wire_in_hand is None:
            ManagerModel.set_selected_item(self._model if not self.selected else None)
        super()._on_click()

    def get_data(self) -> List[float]:
        return self._model.get_data()

    def get_units(self) -> List[str]:
        return self._model.get_units()
