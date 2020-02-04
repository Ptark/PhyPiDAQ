from typing import List, NoReturn

from .Input import Input
from .ItemModel import ItemModel
from ..config.ConfigModel import ConfigModel
from ..workspace.WorkspaceModel import WorkspaceModel


class InputItem(ItemModel):
    """This class represents a Drag and Drop item, which has inputs"""

    def __init__(self, name: str, description: str, config: ConfigModel, inputs: int):
        """Initialising an InputItem object

        Args:
            name (str): Name of the InputItem
            description (str): Description of the InputItem
            config (ConfigModel): A configuration of adjustable options for this InputItem
            inputs (int): Count of inputs this InputItem has
        """
        super().__init__(name, description, config, WorkspaceModel.add_input_item(self))

        self._inputs: List[Input] = []
        for i in range(0, inputs):
            self._inputs.append(Input(self._id, i))

    def get_count_of_inputs(self) -> int:
        """Returns maximum count of inputs for this item

        Returns:
            int: Maximum count of inputs
        """
        if len(self._inputs) is not None:
            return len(self._inputs)
        return 0

    def connect_input(self, input_index: int, output_id: int) -> NoReturn:
        """Connects an input with an output

        Connects the input on a specific index in this item to an output identified by its ID

        Args:
            input_index (int): Index of the input in this item, which will be connected
            output_id (int): ID of output, which is part of the connection
        """
        if 0 <= input_index < self.get_count_of_inputs():
            if self._inputs[input_index] is not None:
                input_id: int = self._inputs[input_index].id
                if WorkspaceModel.check_output_id(output_id) and WorkspaceModel.check_input_id(input_id):
                    WorkspaceModel.connect(input_id, output_id)

    def get_output_id(self, input_number: int) -> int:
        """Returns the ID of the input on a specific index

        Args:
            input_number (int): Index of the input in this item

        Returns:
            int: ID of input.
                -1, if index is out of range
        """
        if 0 <= input_number < self.get_count_of_inputs():
            return self._inputs[input_number].id
        return -1

    def get_input_ids(self) -> List[int]:
        ids: List[int] = []
        for input in self._inputs:
            ids.append(input.id)
        return ids
