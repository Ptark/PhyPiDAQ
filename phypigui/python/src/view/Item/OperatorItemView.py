from typing import NoReturn, List

from PyQt5.QtWidgets import QWidget

from ...model.manager.ManagerModel import ManagerModel
from ...model.item.operators.OperatorItem import OperatorItem
from .WorkspaceItemView import WorkspaceItemView


class OperatorItemView(WorkspaceItemView):
    """Abstract class for displaying an item of an operator on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    def __init__(self, parent: QWidget, operator: 'OperatorEnum'):
        self._model: OperatorItem = operator.model()

        super().__init__(parent, operator, self._model.get_input_ids(), self._model.get_output_ids())

    def _select(self) -> NoReturn:
        ManagerModel.set_selected_item(self._model if self.selected else None)
        super()._select()

    def get_data(self) -> List[float]:
        return self._model.get_data()

    def get_units(self) -> List[str]:
        return self._model.get_units()
