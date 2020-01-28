from abc import ABC, abstractmethod
from ..item.InputItem import InputItem
from ..item.Output import Output
from ..item.OutputItem import OutputItem
from ..item.SensorItem import SensorItem
from ..config.ConfigModel import ConfigModel
from ..workspace.WorkspaceModel import WorkspaceModel
from typing import List, Callable, Dict


class OperatorItem(ABC, InputItem, OutputItem):
    """Superclass for all kind of operators"""
    def __init__(self, name: str, description: str, config: ConfigModel, inputs: int, outputs: int):
        InputItem.__init__(self.super(), name, description, config, inputs)
        self._outputs: List[Output] = []
        for i in range(1, outputs):
            self._outputs.append(Output(self._id, i))


class DivisionOperatorItem(OperatorItem):
    """Class models a division operator"""
    def __init__(self):
        name: str = "Divisionsoperator"
        description: str = "Dieser Operator dividiert zwei Werte"
        config: ConfigModel = ConfigModel()
        super().__init__(name, description, config, 2, 1)

    def get_rule(self, output_number: int = 0) -> Callable[[Dict[SensorItem, List[float]]], float]:
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[0].id())(data)
        second_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[1].id())(data)
        return lambda data: first_function(data) / second_function(data)

    def get_unit(self, output_number: int) -> str:
        """Returns the units from inputs and concatenate with division operator"""

        return "(" + WorkspaceModel.WorkspaceModel.calculate_unit(self._inputs[0].id()) + ") / (" +\
            WorkspaceModel.WorkspaceModel.calculate_unit(self._inputs[1].id()) + ")"


class AbsoluteOperatorItem(OperatorItem):
    """Class models an absolute operator"""

    def __init__(self):
        name: str = "Absolutoperator"
        description: str = "Dieser Operator berechnet den Absolutbetrag"
        config: ConfigModel = ConfigModel()
        super().__init__(name, description, config, 1, 1)

    def get_rule(self, output_number: int = 0):
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[0].id())(data)
        return lambda data: abs(first_function(data))

    def get_unit(self, output_number: int) -> str:
        """Returns the unit from input"""

        return "(" + WorkspaceModel.WorkspaceModel.calculate_unit(self._inputs[0].id()) + ")"


class MultiplicationOperatorItem(OperatorItem):
    """Class models a multiplication operator"""

    def __init__(self):
        name: str = "Multiplikationsoperator"
        description: str = "Dieser Operator multipliziert zwei Werte"
        config: ConfigModel = ConfigModel()
        super().__init__(name, description, config, 2, 1)

    def get_rule(self, output_number: int = 0):
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[0].id())(data)
        second_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[1].id())(data)
        return lambda data: first_function(data) * second_function(data)

    def get_unit(self, output_number: int) -> str:
        """Returns the units from inputs and concatenate with multiplication operator"""

        return "(" + WorkspaceModel.WorkspaceModel.calculate_unit(self._inputs[0].id()) + ") * (" +\
            WorkspaceModel.WorkspaceModel.calculate_unit(self._inputs[1].id()) + ")"