from abc import ABC, abstractmethod
from ..item import Input
from ..config import ConfigModel


class DiagramItem(ABC):
    pass


class BarDiagramItem(DiagramItem):
    def __int__(self):
        super().__init__([None] * 3, [None] * 3, [None] * 3)
        self._name: str = "Balkendiagramm"
        self._config = ConfigModel.ConfigModel()
        self._description: str = "stellt die gemessenen Daten als Balkendiagramm dar"
        self._inputs: [Input] = [Input.Input()] * 3

    def get_number_of_inputs(self) -> int:
        return 3


class TimeDiagramItem(DiagramItem):
    def __init__(self):
        super().__init__([None], [None], [None])
        self._name: str = "Zeitdiagramm"
        self._description = "stellt die gemessenen Daten als Zeitdiagramm dar"
        self._config = ConfigModel.ConfigModel()
        self._inputs: [Input] = [Input.Input] * 2

    def get_number_of_inputs(self) -> int:
        return 1
