from .. import Identifiable
from ..workspace import WorkspaceModel


class Input(Identifiable):
    def __init__(self, parent_id: int):
        self.__parent_item_id: int = parent_id
        super().__init__(WorkspaceModel.WorkspaceModel.add_input(self))
        self.__connected_to: int = -1

    @property
    def parent_item_id(self) -> int:
        return self.__parent_item_id

    @property
    def connected_to(self) -> int:
        return self.__connected_to

    @connected_to.setter
    def connected_to(self, output_id: int):
        if WorkspaceModel.WorkspaceModel.check_output_id():
            self.__connected_to = output_id

    def is_connected(self) -> bool:
        """Checks if this input is connected to an output

        Returns:
            bool: True, if input is connected to an output
        """
        return self.__connected_to == -1
