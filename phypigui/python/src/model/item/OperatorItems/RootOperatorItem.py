from typing import Callable, Dict, List

from ...config.ConfigModel import ConfigModel
from ..OperatorItems.OperatorItem import OperatorItem
from ..SensorItems.SensorItem import SensorItem
from ...config.NumOption import NumOption
from ...workspace.WorkspaceModel import WorkspaceModel


class RootOperatorItem(OperatorItem):
    """This class models an operator, which exponentiates a data-stream with 1 divided through an adjustable number

    A OperatorItem has one input and one output.
    """

    def __init__(self):
        """Initialising a RootOperatorItem object"""
        name: str = "Wurzeloperator"
        description: str = "Dieser Operator potenziert einen Datenstrom mit 1 geteilt durch eine einstellbare Zahl"
        config: ConfigModel = ConfigModel()
        config.add_num_option(NumOption("n-te Wurzel", "Hier kann man die Zahl n\neinstellen", 0, -20, 20, 0))

        super().__init__(name, description, config, 1, 1)

    def get_rule(self, output_number: int = 0):
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: + \
            WorkspaceModel.calculate_function(self._inputs[0].id)(data)
        return lambda data: pow(first_function(data), 1 / self.config.num_options[0].number)

    def get_unit(self, output_number: int = 0) -> str:
        return "(" + WorkspaceModel.calculate_unit(self._inputs[0].id) + "^ 1/" \
                + str(self.config.num_options[0].number) + ")"
