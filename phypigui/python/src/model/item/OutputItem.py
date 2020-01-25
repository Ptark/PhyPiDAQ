from abc import ABC, abstractmethod
from ..item import ItemModel, Output, SensorItem
from ..workspace import WorkspaceModel
from typing import NoReturn, List, Dict
from ..config import ConfigModel


class OutputItem(ItemModel, ABC):
    def __init__(self, name: str, description: str, config: ConfigModel.ConfigModel, outputs: int):
        super().__init__(name, description, config, WorkspaceModel.WorkspaceModel.add_output_item(self))
        self._outputs: List[Output.Output] = []
        for i in range(1, outputs):
            self._outputs.append(Output.Output(self.__id, i))

    @abstractmethod
    def get_rule(self, output_number: int) -> NoReturn:
        pass

    @abstractmethod
    def get_unit(self, output_number: int) -> str:
        pass

    def get_data(self) -> List[float]:
        """Returns a list of stored data/results from the outputs of this item

        The list is in the same order as the outputs.

        Returns:
             List[float]: List of data
        """
        data: List[float] = []
        for output in self._outputs:
            data.append(output.data)
        return data

    def get_units(self) -> List[str]:
        """Returns a list of the stored units of the outputs

        The list is in the same order as the outputs.

        Returns:
             List[str]: List of units
        """
        units: List[str] = []
        for output in self._outputs:
            units.append(output.unit)
        return units

    def get_number_of_outputs(self) -> int:
        """Returns maximum number of outputs for this item

        Returns:
            int: Maximum number of outputs
        """
        if len(self._outputs) is not None:
            return len(self._outputs)
        return 0

    def connect_output(self, output_index: int, input_id: int) -> NoReturn:
        if self._outputs[output_index] is not None:
            output_id = self._outputs[output_index].id
            WorkspaceModel.WorkspaceModel.connect(input_id, output_id)
        return

    def get_output_id(self, number_of_output: int) -> int:
        """Returns the ID of the output on index number_of_output

        Args:
            number_of_output (int): Index of output

        Returns:
            int: ID of output. -1, if index is out of range
        """
        if 0 <= number_of_output <= self.get_number_of_outputs():
            return self._outputs[number_of_output].id
        return -1

    def invalidate_functions(self) -> NoReturn:
        """Invalidates all lambda-functions in the outputs of this item

        Invalidates all lambda-functions in the outputs of this item and invalidates all lambda-functions from
        sequel items.
        """
        for output in self._outputs:
            output.invalidate_function()

    def calculate(self, data: Dict[SensorItem.SensorItem, List[float]]) -> NoReturn:
        """Plugs data in every lambda-function of its outputs und stores result

        Args:
            data (Dict[SensorItem.SensorItem, List[float]]): Data, which will plug in lambda-function
        """
        for output in self._outputs:
            output.calculate(data)
