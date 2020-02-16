from typing import Callable, Dict, List

from ...config.ConfigModel import ConfigModel
from ..OperatorItems.OperatorItem import OperatorItem
from ..SensorItems.SensorItem import SensorItem
from ...config.NumOption import NumOption
from ...workspace.WorkspaceModel import WorkspaceModel


class PowerOperatorItem(OperatorItem):
    """This class models an operator, which exponentiates a data-stream with an adjustable number

    A PowerOperatorItem has one input and one output.
    """

    def __init__(self):
        """Initialising a PowerOperatorItem object"""
        name: str = "Exponentialsoperator"
        description: str = "Dieser Operator potenziert einen Datenstrom mit einer einstellbaren Zahl"
        config: ConfigModel = ConfigModel()
        config.add_num_option(NumOption("Exponent", "Mit dieser Zahl wird der\nDaten-Strom potenziert", 0, -20, 20, 0))

        super().__init__(name, description, config, 1, 1)

    def get_rule(self, output_number: int = 0):
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: + \
            WorkspaceModel.calculate_function(self._inputs[0].id)(data)
        return lambda data: pow(first_function(data), self.config.num_options[0].number)

    def get_unit(self, output_number: int = 0) -> str:
        unit = WorkspaceModel.calculate_unit(self._inputs[0].id)
        number = str(self.config.num_options[0].number)
        return unit + "^" + number


    @staticmethod
    def get_name() -> str:
        return "Exponentialsoperator"
