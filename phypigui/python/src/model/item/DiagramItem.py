from abc import ABC, abstractmethod
from ..item.SensorItem import SensorItem
from ..config.ConfigModel import ConfigModel
from typing import List, Callable, Dict
from ..item.InputItem import InputItem
from ..workspace import WorkspaceModel


class DiagramItem(InputItem):
    def __init__(self, name: str, description: str, config: ConfigModel, input_count: int):
        self._functions: List[Callable[[Dict[SensorItem, List[float]]], float]] = []
        self._data: List[float] = []
        self._unit: List[str] = []
        for i in range(0, input_count - 1):
            self._functions.append(lambda data: 0)
            self._data.append(0)
            self._unit.append('')
        super().__init__(name, description, config, input_count)

    def calculate_functions(self) -> bool:
        for i in range(0, self.get_number_of_inputs() - 1):
            self._functions[i] = WorkspaceModel.WorkspaceModel.calculate_function(self._inputs[i].id)
            self._unit[i] = WorkspaceModel.WorkspaceModel.calculate_unit(self._inputs[i].id)
        return True

    def calculate(self, sensor_data: Dict[SensorItem, List[float]]) -> bool:
        for i in range(0, self._get_number_of_inputs() - 1):
            self._data[i] = self._functions[i](sensor_data)
        return True


class BarDiagramItem(DiagramItem):
    def __int__(self):
        name: str = "Balkendiagramm"
        config: ConfigModel = ConfigModel()
        description: str = "Stellt die gemessenen Daten als Balkendiagramm dar"
        super().__init__(name, description, config, self.get_number_of_inputs())

    def get_number_of_inputs(self) -> int:
        return 3


class TimeDiagramItem(DiagramItem):
    def __init__(self):
        name: str = "Zeitdiagramm"
        description = "Stellt die gemessenen Daten als Zeitdiagramm dar"
        config = ConfigModel()
        super().__init__(name, description, config, self.get_number_of_inputs())

    def get_number_of_inputs(self) -> int:
        return 1
