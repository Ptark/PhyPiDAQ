from typing import Callable, Dict, List

from ...config.ConfigModel import ConfigModel
from ..operators.OperatorItem import OperatorItem
from ..sensors.SensorItem import SensorItem
from ...workspace.WorkspaceModel import WorkspaceModel


class DivisionOperatorItem(OperatorItem):
    """This class models a operator, which divides the first by the second data-stream

    A DivisionOperatorItem has two inputs and one output.
    """

    def __init__(self):
        """Initialising a DivisionOperatorItem object"""
        name: str = "Divisionsoperator"
        description: str = "Dieser Operator dividiert zwei Werte"
        config: ConfigModel = ConfigModel()

        super().__init__(name, description, config, 2, 1)

    def get_rule(self, output_number: int = 0) -> Callable[[Dict[SensorItem, List[float]]], float]:
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[0].id)(data)
        second_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[1].id)(data)
        return lambda data: first_function(data) / second_function(data) if second_function(data) != 0 else None

    def get_unit(self, output_number: int = 0) -> str:
        left_unit = WorkspaceModel.calculate_unit(self._inputs[0].id)
        right_unit = WorkspaceModel.calculate_unit(self._inputs[1].id)
        if left_unit == right_unit:
            return ""
        if right_unit == "":
            return left_unit
        if left_unit == "":
            return "(1 / " + right_unit + ")"
        return "(" + left_unit + " / " + right_unit + ")"

    @staticmethod
    def get_name() -> str:
        return "Divisionsoperator"
