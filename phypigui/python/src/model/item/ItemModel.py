from abc import ABC
from ..NameableRO import NameableRO
from ..Describable import Describable
from ..Identifiable import Identifiable
from ..Model import Model
from ..config.ConfigModel import ConfigModel
from typing import NoReturn
import copy


class ItemModel(NameableRO, Describable, Identifiable, Model, ABC):
    """Abstract class models an item (Sensor, Operator, Diagram).

   Attributes:
        _config (ConfigModel): Holds the configuration of the ItemModel
    """
    def __init__(self, name: str, description: str, config: ConfigModel, item_id: int):
        NameableRO.__init__(self, name)
        Describable.__init__(self, description)
        Identifiable.__init__(self, item_id)
        self._config: ConfigModel = config

    @property
    def config(self) -> ConfigModel:
        return self._config

    def set_bool_option(self, index: int, value: bool) -> NoReturn:
        """Sets the value of the Bool-Option on a specific index

        Args:
            index (int): Index of the Bool-Option in the List of all Bool-Options for this item
            value (bool): Value, on which the value of the Bool-Option will be set
        Raises:
            AssertionError: If the specified index doesnt exist
        """
        assert(self._config.bool_options[index] is not None)
        self._config.set_bool_option(index, value)

    def set_file_option(self, index: int, path: str) -> NoReturn:
        """Sets the path of the File-Option on a specific index

        Args:
            index (int): Index of the File-Option in the List of all File-Options for this item
            path (str): Path, on which the path of the File-Option will be set
        Raises:
            AssertionError: If the specified index doesnt exist
        """
        assert(self._config.file_options[index] is not None)
        self._config.set_file_option(index, path)

    def set_enum_option(self, index: int, selection: int) -> NoReturn:
        """Sets the selection of the Bool-Option on a specific index

        Args:
            index (int): Index of the Enum-Option in the List of all Enum-Options for this item
            selection (int): Selection-index, on which the selection of the Enum-Option will be set
        Raises:
            AssertionError: If the specified index doesnt exist
        """
        assert(self._config.enum_options[index] is not None)
        self._config.set_enum_option(index, selection)

    def set_num_option(self, index: int, number: float) -> NoReturn:
        """Sets the number of the Num-Option on a specific index

        Args:
            index (int): Index of the Num-Option in the List of all Num-Options for this item
            number (float): Number, on which the number of the Num-Option will be set
        Raises:
            AssertionError: If the specified index doesnt exist
        """
        assert(self._config.num_options[index] is not None)
        self._config.set_num_option(index, number)
