from .. import Identifiable
from ..workspace import WorkspaceModel


class Input(Identifiable):
    def __init__(self, parent_id: int):
        self.__parent_item_id: int = parent_id
        super().__init__(WorkspaceModel.WorkspaceModel.add_input(self))

    @property
    def parent_item_id(self) -> int:
        return self.__parent_item_id
