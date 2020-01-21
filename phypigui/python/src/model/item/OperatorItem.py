from abc import ABC, abstractmethod
from ..item import InputItem, Output, Input, OutputItem, SensorItem
from ..config import ConfigModel
from ..workspace import WorkspaceModel
from typing import List, Callable, Dict


class OperatorItem(ABC, InputItem, OutputItem):
    def __init__(self, name: str, description: str, config: ConfigModel, inputs: int, outputs: int):
        self._first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.WorkspaceModel.calculate_function(self._inputs[0].get_id())(data)
        super().__init__(name, description, config, inputs, outputs)

    def get_unit(self, output_number: int) -> str:
        return "(" + WorkspaceModel.WorkspaceModel.calculate_unit(self._inputs[0].get_id()) + ") + (" +\
                WorkspaceModel.WorkspaceModel.calculate_unit(self._inputs[1].get_id()) + ")"

    def get_number_of_outputs(self) -> int:
        return 1


class DivisionOperatorItem(OperatorItem):
    def __init__(self):
        self._second_function = Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.WorkspaceModel.calculate_function(self._inputs[1].get_id())(data)
        name: str = "Divisionsoperator"
        description: str = "Dieser Operator dividiert zwei Werte"
        config: ConfigModel = ConfigModel.ConfigModel()
        super().__init__(name, description, config, 2, 1)

    def get_rule(self, output_number: int = 0) -> Callable[[Dict[SensorItem, List[float]]], float]:
        return lambda data: self._first_function(data) / self._second_function(data)

    def get_number_of_inputs(self) -> int:
        return 2


class AbsoluteOperatorItem(OperatorItem):
    def __init__(self):
        name: str = "Absolutoperator"
        description: str = "Dieser Operator berechnet den Absolutbetrag"
        config: ConfigModel = ConfigModel.ConfigModel()
        super().__init__(name, description, config, 1, 1)
    
    def get_number_of_inputs(self) -> int:
        return 1

    def get_rule(self, output_number: int = 0):
        return lambda data: abs(self._first_function(data))

    def get_unit(self, output_number: int) -> str:
        return "(" + WorkspaceModel.WorkspaceModel.calculate_unit(self._inputs[0].get_id()) + ")"


class MultiplicationOperatorItem(OperatorItem):
    def __init__(self):
        self._second_function = Callable[[Dict[SensorItem, List[float]]], float] = lambda data: + \
            WorkspaceModel.WorkspaceModel.calculate_function(self._inputs[1].get_id())(data)
        name: str = "Multiplikationsoperator"
        description: str = "Dieser Operator multipliziert zwei Werte"
        config: ConfigModel = ConfigModel.ConfigModel()
        super().__init__(name, description, config, 2, 1)

    def get_rule(self, output_number: int = 0):
        return lambda data: self._first_function(data) * self._second_function(data)

    def get_number_of_inputs(self) -> int:
        return 2