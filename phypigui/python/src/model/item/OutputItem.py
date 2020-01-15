from abc import ABC, abstractmethod
from ..item import ItemModel
from ..item import Output
from ..workspace import WorkspaceModel
from typing import NoReturn


class OutputItem(ItemModel, ABC):
    def __init__(self):
        self._outputs: [Output] = []

    @abstractmethod
    def get_rule(self, output_number: int) -> NoReturn:
        #TODO
        pass

    @abstractmethod
    def get_unit(self, output_number: int) -> str:
        pass

    @abstractmethod
    def get_number_of_outputs(self) -> int:
        if len(self._outputs) is not None:
            return len(self._outputs)
        return 0

    def connect_output(self, output_index: int, input_id: int) -> NoReturn:
        if self._outputs[output_index] is not None:
            output_id = self._outputs[output_index].getid()
            WorkspaceModel.WorkspaceModel.connect(input_id, output_id)
        return
