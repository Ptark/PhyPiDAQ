from abc import ABC
from .. import NameableRO, Identifiable
from ..config import ConfigModel
from ..workspace import WorkspaceModel
from typing import NoReturn
import copy


class ItemModel(NameableRO.NameableRO, Identifiable.Identifiable, ABC):
    """Abstract class models an item (Sensor, Operator, Diagram).

   Attributes:
        name: A str which names the ItemModel
        description: A str which describes the item model
        config: A ConfigModel which holds the configuration of the ItemModel
    """
    def __init__(self, name: str, description: str, config: ConfigModel.ConfigModel):
        NameableRO.NameableRO.__init__(self, name)
        Identifiable.Identifiable.__init__(self, WorkspaceModel.WorkspaceModel.add_item(self))
        self.__config: ConfigModel.ConfigModel = config
        self.__description: str = description

    @property
    def config(self) -> ConfigModel.ConfigModel:
        return copy.deepcopy(self.__config)

    @property
    def description(self) -> str:
        return self.__description

    def set_bool_option(self, index: int, value: bool) -> NoReturn:
        """Sets the value of the Bool-Option on a specific index

        Args:
            index (int): Index of the Bool-Option in the List of all Bool-Options for this item
            value (bool): Value, on which the value of the Bool-Option will be set
        Raises:
            AssertionError: If the specified index doesnt exist
        """
        assert(self.__config.bool_options[index] is not None)
        self.__config.set_bool_option(index, value)

    def set_file_option(self, index: int, path: str) -> NoReturn:
        """Sets the path of the File-Option on a specific index

        Args:
            index (int): Index of the File-Option in the List of all File-Options for this item
            path (str): Path, on which the path of the File-Option will be set
        Raises:
            AssertionError: If the specified index doesnt exist
        """
        assert(self.__config.file_options[index] is not None)
        self.__config.set_file_option(index, path)

    def set_enum_option(self, index: int, selection: int) -> NoReturn:
        """Sets the selection of the Bool-Option on a specific index

        Args:
            index (int): Index of the Enum-Option in the List of all Enum-Options for this item
            selection (int): Selection-index, on which the selection of the Enum-Option will be set
        Raises:
            AssertionError: If the specified index doesnt exist
        """
        assert(self.__config.enum_options[index] is not None)
        self.__config.set_enum_option(index, selection)

    def set_num_option(self, index: int, number: float) -> NoReturn:
        """Sets the number of the Num-Option on a specific index

        Args:
            index (int): Index of the Num-Option in the List of all Num-Options for this item
            number (float): Number, on which the number of the Num-Option will be set
        Raises:
            AssertionError: If the specified index doesnt exist
        """
        assert(self.__config.num_options[index] is not None)
        self.__config.set_num_option(index, number)
