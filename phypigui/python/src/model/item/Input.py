from .. import Identifiable
from ..workspace import WorkspaceModel


class Input(Identifiable):
    def __init__(self, parent_id: int, input_number: int):
        self.__parent_item_id: int = parent_id
        self.__number_of_input = input_number
        super().__init__(WorkspaceModel.WorkspaceModel.add_input(self))

    @property
    def parent_item_id(self) -> int:
        return self.__parent_item_id

    @property
    def number_of_input(self) -> int:
        return self.__number_of_input
