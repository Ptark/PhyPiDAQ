from abc import ABC, abstractmethod
from ..config import ConfigModel
from . import ItemModel, Input
from ..workspace import WorkspaceModel
from typing import List, NoReturn


class InputItem(ItemModel, ABC):
    def __init__(self, name: str, description: str, config: ConfigModel.ConfigModel, inputs: int):
        super().__init__(name, description, config, WorkspaceModel.WorkspaceModel.add_input_item(self))
        self.__inputs: List[Input.Input] = []
        for i in range(1, inputs):
            self.__inputs.append(Input.Input(self._id))

    @abstractmethod
    def get_number_of_inputs(self) -> int:
        """Returns maximum number of inputs for this item

        Returns:
            int: Maximum number of inputs
        """
        pass

    def connect_input(self, input_index: int, output_id: int) -> NoReturn:
        """Connects an input with an output

        Connects one input of this item to an output identified by its ID

        Args:
            input_index (int): Number of the input, which will be connected
            output_id (int): ID of output, which is part of the connection
        """
        if 0 <= input_index <= self.get_number_of_inputs():
            input_id: int = self.__inputs[input_index].id
            if WorkspaceModel.WorkspaceModel.check_output_id(output_id) \
                    and WorkspaceModel.WorkspaceModel.check_input_id(input_id):
                WorkspaceModel.WorkspaceModel.connect(input_id, output_id)

    def get_output_id(self, number_of_input: int) -> int:
        """Returns the ID of the input on index number_of_input

        Args:
            number_of_input (int): Index of input

        Returns:
            int: ID of input. -1, if index is out of range
        """
        if 0 <= number_of_input <= self.get_number_of_inputs():
            return self._inputs[number_of_input].id
        return -1
