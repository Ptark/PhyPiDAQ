from typing import Callable, Dict, List

from ...config.ConfigModel import ConfigModel
from ..operators.OperatorItem import OperatorItem
from ..sensors.SensorItem import SensorItem
from ...workspace.WorkspaceModel import WorkspaceModel


class NegativeOperatorItem(OperatorItem):
    """This class models an operator, which makes a data-stream only negative

    A NegativeOperatorItem has one input and one output.
    """

    def __init__(self):
        """Initialising a NegativeOperatorItem object"""
        name: str = "Negativer Betragsoperator"
        description: str = "Dieser Operator negiert alle einkommenden Werte"
        config: ConfigModel = ConfigModel()

        super().__init__(name, description, config, 1, 1)

    def get_rule(self, output_number: int = 0):
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[0].id)(data)
        return lambda data: (-1 * abs(first_function(data)))

    def get_unit(self, output_number: int = 0) -> str:
        return WorkspaceModel.calculate_unit(self._inputs[0].id)

    @staticmethod
    def get_name() -> str:
        return "Negativer Betragsoperator"
