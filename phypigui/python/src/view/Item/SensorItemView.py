from abc import ABC
from typing import NoReturn

from PyQt5.QtWidgets import QWidget

from ...model.manager.ManagerModel import ManagerModel
from phypigui.python.src.model.item.SensorItems.SensorItem import SensorItem
from .WorkspaceItemView import WorkspaceItemView


class SensorItemView(WorkspaceItemView, ABC):
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
