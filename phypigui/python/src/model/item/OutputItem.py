from abc import ABC, abstractmethod
from ..item import ItemModel
from ..item import Output
from ..workspace import WorkspaceModel
from typing import NoReturn, List
from ..config import ConfigModel


class OutputItem(ItemModel, ABC):
    def __init__(self, name: str, description: str, config: ConfigModel, outputs: int):
        self._outputs: [Output] = []
        for i in range(1, outputs):
            self._outputs.append(Output.Output(self.__id, i))
        super().__init__(name, description, config)

    @abstractmethod
    def get_rule(self, output_number: int) -> NoReturn:
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
            output_id = self._outputs[output_index].id
            WorkspaceModel.WorkspaceModel.connect(input_id, output_id)
        return
