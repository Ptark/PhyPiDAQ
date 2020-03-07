from abc import ABC, abstractmethod
from typing import NoReturn, List, Dict, Callable

from ..item.Output import Output
from ..item.ItemModel import ItemModel
from ..config.ConfigModel import ConfigModel
from ..workspace.WorkspaceModel import WorkspaceModel


class OutputItem(ItemModel, ABC):
    """This class represents a Drag and Drop item, which has outputs"""

    def __init__(self, name: str, description: str, config: ConfigModel, outputs: int):
        """Initialising an OutputItem object

        Args:
            name (str): Name of this OutputItem
            description (str): Description of this OutputItem
            config (ConfigModel): A configuration of adjustable options for this OutputItem
            outputs (int): Count of outputs this OutputItem has
        """
        super().__init__(name, description, config, WorkspaceModel.add_output_item(self))

        self._outputs: List[Output] = []
        for i in range(0, outputs):
            self._outputs.append(Output(self._id, i))

    @abstractmethod
    def get_rule(self, output_number: int = 0) -> Callable[[Dict['SensorItem', List[float]]], float]:
        """Construct for an output on a specific index its lambda-function and returns it

        This method calls all previous items to construct their lambda-functions and constructs with these a new
        lambda-function for the specified output.
        Returns a constant zero lambda-function, if this item has no valid connections to enough sensors.
        The standard output_number is zero.

        Args:
            output_number (int): Index of the output in this item

        Returns:
            Callable[[Dict[SensorItem, List[float]]], float]: Lambda-function for the output.
                Constant zero lambda-function, if this item has no valid connections to enough sensors.
        """
        pass

    @abstractmethod
    def get_unit(self, output_number: int = 0) -> str:
        """Construct for an output on a specific index its unit and returns it

        This method calls all previous items to construct their units and constructs with these a new
        unit for the specified output.
        Returns a empty string, if this item has no valid connections to enough sensors.
        The standard output_number is zero.

        Args:
            output_number (int): Index of the output in this item

        Returns:
            str: unit of the output.
                Empty string, if this item has no valid connections to enough sensors.
        """
        pass

    def set_config(self, config: ConfigModel) -> NoReturn:
        """Sets all values of the config of this item to values of a given configuration

        This method also invalidates all stored lambda-functions in the outputs of this item and sequel items, too

        Args:
            config (ConfigModel): The Configuration, which contains the new values for every option of this item
        """
        super().set_config(config)
        self.invalidate_functions()

    def get_data(self) -> List[float]:
        """Returns a list of the last values all the outputs of this item had at the last calculation-cycle

        The list is in the same order as the outputs of this item.

        Returns:
             List[float]: List of data
        """
        data: List[float] = []
        for output in self._outputs:
            data.append(output.data)
        return data

    def get_units(self) -> List[str]:
        """Returns a list of the last constructed units for each output this item has

        The list is in the same order as the outputs of this item.

        Returns:
             List[str]: List of units. A unit is an empty string, if this item has no valid connections to enough
                sensors.
        """
        units: List[str] = []
        for output in self._outputs:
            units.append(output.unit)
        return units

    def get_count_of_outputs(self) -> int:
        """Returns maximum count of outputs for this item

        Returns:
            int: Maximum count of outputs
        """
        return len(self._outputs)

    def connect_output(self, output_index: int, input_id: int) -> NoReturn:
        """Connects an output with an input

        Connects the output on a specific index in this item to an input identified by its ID

        Args:
            output_index (int): Index of the output in this item, which will be connected
            input_id (int): ID of input, which is part of the connection
        """
        if 0 <= output_index < self.get_count_of_outputs():
            if self._outputs[output_index] is not None:
                output_id = self._outputs[output_index].id
                if WorkspaceModel.check_output_id(output_id) and WorkspaceModel.check_input_id(input_id):
                    WorkspaceModel.connect(input_id, output_id)

    def get_output_id(self, output_number: int) -> int:
        """Returns the ID of the output on a specific index

        Args:
            output_number (int): Index of output in this item

        Returns:
            int: ID of output.
                -1, if index is out of range
        """
        if 0 <= output_number < self.get_count_of_outputs():
            return self._outputs[output_number].id
        return -1

    def invalidate_functions(self) -> NoReturn:
        """Invalidates all stored lambda-functions in the outputs of this item and sequel items, too"""
        for output in self._outputs:
            output.invalidate_function()

    def calculate(self, data: Dict['SensorItem', List[float]]) -> NoReturn:
        """Plugs data in the lambda-function of every output of this item und stores the result in it

        Args:
            data (Dict[SensorItem.SensorItem, List[float]]): Data, which will be plugged in the lambda-functions
        """
        for output in self._outputs:
            output.calculate(data)

    def get_output_ids(self) -> List[int]:
        ids: List[int] = []
        for output in self._outputs:
            ids.append(output.id)
        return ids
