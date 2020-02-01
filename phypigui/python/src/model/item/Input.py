from ..Identifiable import Identifiable
from ..workspace.WorkspaceModel import WorkspaceModel


class Input(Identifiable):
    """This class represents an input of a InputItem

    Objects from this class are typically created in the constructor of an InputItem.
    """

    def __init__(self, parent_id: int, input_number: int):
        """Initialising an Input object

        Args:
            parent_id (int): ID of the InputItem, which this input belongs to
            input_number (int): Number this input has in its parent item
        """
        self.__parent_item_id: int = parent_id
        self.__number_of_input = input_number
        super().__init__(WorkspaceModel.add_input(self))

    @property
    def parent_item_id(self) -> int:
        """ID of the InputItem, which this input belongs to"""
        return self.__parent_item_id

    @property
    def number_of_input(self) -> int:
        """Number this input has in its parent item"""
        return self.__number_of_input
