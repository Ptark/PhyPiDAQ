from typing import NoReturn, List

from PyQt5.QtWidgets import QWidget

from ...model.manager.ManagerModel import ManagerModel
from ..DiagramField.DiagramFieldView import DiagramFieldView
from ..DiagramField.DiagramView import DiagramView
from ...model.item.diagrams.DiagramItem import DiagramItem
from ..Item.WorkspaceItemView import WorkspaceItemView


class DiagramItemView(WorkspaceItemView):
    """Abstract class for displaying an item of an diagram on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    def __init__(self, parent: QWidget, diagram: 'DiagramEnum'):
        self._model: DiagramItem = diagram.model()
        if diagram.diagram is not None:
            self._diagram: DiagramView = diagram.diagram(self._model)
            DiagramFieldView.add_diagram(self._diagram)
        else:
            self._diagram: DiagramView = None

        super().__init__(parent, diagram, self._model.get_input_ids(), [])

    def delete(self) -> NoReturn:
        if self._diagram is not None:
            DiagramFieldView.delete_diagram(self._diagram)
        ManagerModel.delete_diagram(self._model)
        super().delete()

    def _select(self) -> NoReturn:
        if self._diagram is not None:
            self._diagram.update_selected_view(self.selected)

        super()._select()

    def get_data(self) -> List[float]:
        return self._model.data

    def get_units(self) -> List[str]:
        return self._model.unit
