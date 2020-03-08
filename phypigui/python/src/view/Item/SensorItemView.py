from typing import NoReturn, List

from PyQt5.QtWidgets import QWidget, QLabel

from ...Exceptions import SensorDAQError
from ..Translator import Translator
from ...model.manager.ManagerModel import ManagerModel
from ...model.item.sensors.SensorItem import SensorItem
from .WorkspaceItemView import WorkspaceItemView


class SensorItemView(WorkspaceItemView):
    """Abstract class for displaying an item of a sensor on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    def __init__(self, parent: QWidget, sensor: 'SensorEnum'):
        try:
            self._model: SensorItem = sensor.model()
        except Exception:
            raise SensorDAQError

        super().__init__(parent, sensor, [], self._model.get_output_ids(), False)

        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        pins = self._model.pins
        if pins is not None and len(pins) != 0:
            text = Translator.tr("Steckplätze auf dem Raspberry Pi") + ": "
            for pin in pins:
                text += str(pin) + ", "
            pin_label: QLabel = QLabel(text[:-2])
            self._info_layout.insertWidget(3, pin_label)

    def delete(self) -> NoReturn:
        ManagerModel.delete_sensor(self._model)
        super().delete()

    def _select(self) -> NoReturn:
        ManagerModel.set_selected_item(self._model if self.selected else None)
        super()._select()

    def get_data(self) -> List[float]:
        return self._model.get_data()

    def get_units(self) -> List[str]:
        return self._model.get_units()
