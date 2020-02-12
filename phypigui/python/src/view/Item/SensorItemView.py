from typing import NoReturn, List

from PyQt5.QtWidgets import QWidget

from ..Workspace.WorkspaceView import WorkspaceView
from ...model.manager.ManagerModel import ManagerModel
from ...model.item.SensorItems.SensorItem import SensorItem
from .WorkspaceItemView import WorkspaceItemView


class SensorItemView(WorkspaceItemView):
    """Abstract class for displaying an item of a sensor on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    def __init__(self, parent: QWidget, sensor: 'SensorEnum'):
        self._model: SensorItem = sensor.model()

        super().__init__(parent, sensor.path, [], self._model.get_output_ids(), False)

    def delete(self) -> NoReturn:
        ManagerModel.delete_sensor(self._model)
        super().delete()

    def select(self) -> NoReturn:
        ManagerModel.set_selected_item(self._model if self.selected else None)

    def get_data(self) -> List[float]:
        return self._model.get_data()

    def get_units(self) -> List[str]:
        return self._model.get_units()
