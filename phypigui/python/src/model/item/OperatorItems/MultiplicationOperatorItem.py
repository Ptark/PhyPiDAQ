from typing import Callable, Dict, List

from phypigui.python.src.model.config.ConfigModel import ConfigModel
from phypigui.python.src.model.item.OperatorItems.OperatorItem import OperatorItem
from phypigui.python.src.model.item.SensorItems.SensorItem import SensorItem
from phypigui.python.src.model.workspace.WorkspaceModel import WorkspaceModel


class MultiplicationOperatorItem(OperatorItem):
    """This class models an operator, which multiply two data-streams

    A MultiplicationOperatorItem has two inputs and one output.
    """

    def __init__(self):
        """Initialising a MultiplicationOperatorItem object"""
        name: str = "Multiplikationsoperator"
        description: str = "Dieser Operator multipliziert zwei Werte"
        config: ConfigModel = ConfigModel()

        super().__init__(name, description, config, 2, 1)

    def get_rule(self, output_number: int = 0):
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[0].id)(data)
        second_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[1].id)(data)
        return lambda data: first_function(data) * second_function(data)

    def get_unit(self, output_number: int = 0) -> str:
        return "(" + WorkspaceModel.calculate_unit(self._inputs[0].id) + ") * (" +\
            WorkspaceModel.calculate_unit(self._inputs[1].id) + ")"
