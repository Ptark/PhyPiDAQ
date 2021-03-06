from typing import Callable, Dict, List

from ...config.ConfigModel import ConfigModel
from ..operators.OperatorItem import OperatorItem
from ..sensors.SensorItem import SensorItem
from ...workspace.WorkspaceModel import WorkspaceModel


class AbsoluteOperatorItem(OperatorItem):
    """This class models an operator, which makes a data-stream only positive

    A AbsoluteOperatorItem has one inputs and one output.
    """

    def __init__(self):
        """Initialising a AbsoluteOperatorItem object"""
        name: str = "Absolutoperator"
        description: str = "Dieser Operator berechnet den Absolutbetrag"
        config: ConfigModel = ConfigModel()

        super().__init__(name, description, config, 1, 1)

    def get_rule(self, output_number: int = 0):
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[0].id)(data)
        return lambda data: abs(first_function(data))

    def get_unit(self, output_number: int = 0) -> str:
        return WorkspaceModel.calculate_unit(self._inputs[0].id)

    @staticmethod
    def get_name() -> str:
        return "Absolutoperator"
