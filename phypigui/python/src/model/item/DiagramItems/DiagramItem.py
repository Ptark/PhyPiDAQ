from abc import ABC
from typing import List, Callable, Dict

from ...manager.ManagerModel import ManagerModel
from ..InputItem import InputItem
from ..SensorItems.SensorItem import SensorItem
from ...config.ConfigModel import ConfigModel
from ...workspace.WorkspaceModel import WorkspaceModel


class DiagramItem(InputItem, ABC):
    """This class is a superclass for all kind of DiagramItems"""

    def __init__(self, name: str, description: str, config: ConfigModel, inputs: int):
        """Initialising a DiagramItem object

        Args:
            name (str): Name of this DiagramItem
            description (str): Description of this DiagramItem
            config (ConfigModel): A configuration of adjustable options for this DiagramItem
            inputs (int): Count of inputs for this DiagramItem
        """
        super().__init__(name, description, config, inputs)

        self._functions: List[Callable[[Dict[SensorItem, List[float]]], float]] = []
        self._data: List[float] = []
        self._unit: List[str] = []

        for i in range(0, inputs):
            self._functions.append(lambda data: 0)
            self._data.append(0)
            self._unit.append('')

        ManagerModel.add_diagram(self)

    @property
    def data(self) -> List[float]:
        """List of the last values all the inputs of this item had at the last calculation-cycle

        The list is in the same order as the inputs of this item.
        """
        return self._data

    @property
    def unit(self) -> List[str]:
        return self._unit

    def calculate_functions(self) -> bool:
        """Constructs recursively all lambda-functions and units from previous item starting at this DiagramItem

        This method is typically called every time the ManagerModel is starting a measuring process.

        Returns:
            bool: #TODO ....
        """
        for i in range(0, self.get_count_of_inputs()):
            self._functions[i] = WorkspaceModel.calculate_function(self._inputs[i].id)
            self._unit[i] = WorkspaceModel.calculate_unit(self._inputs[i].id)
        return True

    def calculate(self, sensor_data: Dict[SensorItem, List[float]]) -> bool:
        """Plugs data in all lambda-functions of this DiagramItem und stores the result

        Args:
            sensor_data (Dict[SensorItem.SensorItem, List[float]]): Data, which will be plugged in the lambda-functions

        Returns:
            bool: #TODO ....
        """
        for i in range(0, self.get_count_of_inputs()):
            self._data[i] = self._functions[i](sensor_data)
        return True

    def stop(self):
        """Allows WriteToFileItem to write json to file"""
        pass
