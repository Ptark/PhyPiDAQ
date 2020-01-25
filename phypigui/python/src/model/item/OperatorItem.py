from abc import ABC, abstractmethod
from ..item import InputItem, Output, Input, OutputItem, SensorItem
from ..config import ConfigModel
from ..workspace import WorkspaceModel
from typing import List, Callable, Dict


class OperatorItem(ABC, InputItem, OutputItem):
    def __init__(self, name: str, description: str, config: ConfigModel, inputs: int, outputs: int):
        InputItem.InputItem.__init__(self.super(), name, description, config, inputs)
        self._outputs: List[Output] = []
        for i in range(1, outputs):
            self._outputs.append(Output.Output(self._id, i))

    def get_number_of_outputs(self) -> int:
        return 1


class DivisionOperatorItem(OperatorItem):
    def __init__(self):
        name: str = "Divisionsoperator"
        description: str = "Dieser Operator dividiert zwei Werte"
        config: ConfigModel = ConfigModel.ConfigModel()
        super().__init__(name, description, config, 2, 1)

    def get_rule(self, output_number: int = 0) -> Callable[[Dict[SensorItem, List[float]]], float]:
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.WorkspaceModel.calculate_function(self._inputs[0].id())(data)
        second_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.WorkspaceModel.calculate_function(self._inputs[1].id())(data)
        return lambda data: first_function(data) / second_function(data)

    def get_unit(self, output_number: int) -> str:
        return "(" + WorkspaceModel.WorkspaceModel.calculate_unit(self._inputs[0].id()) + ") / (" +\
                WorkspaceModel.WorkspaceModel.calculate_unit(self._inputs[1].id()) + ")"

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
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.WorkspaceModel.calculate_function(self._inputs[0].id())(data)
        return lambda data: abs(first_function(data))

    def get_unit(self, output_number: int) -> str:
        return "(" + WorkspaceModel.WorkspaceModel.calculate_unit(self._inputs[0].id()) + ")"


class MultiplicationOperatorItem(OperatorItem):
    def __init__(self):
        name: str = "Multiplikationsoperator"
        description: str = "Dieser Operator multipliziert zwei Werte"
        config: ConfigModel = ConfigModel.ConfigModel()
        super().__init__(name, description, config, 2, 1)

    def get_rule(self, output_number: int = 0):
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.WorkspaceModel.calculate_function(self._inputs[0].id())(data)
        second_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.WorkspaceModel.calculate_function(self._inputs[1].id())(data)
        return lambda data: first_function(data) * second_function(data)

    def get_unit(self, output_number: int) -> str:
        return "(" + WorkspaceModel.WorkspaceModel.calculate_unit(self._inputs[0].id()) + ") * (" +\
                WorkspaceModel.WorkspaceModel.calculate_unit(self._inputs[1].id()) + ")"

    def get_number_of_inputs(self) -> int:
        return 2