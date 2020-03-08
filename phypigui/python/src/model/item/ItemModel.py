import copy

from abc import ABC, abstractmethod
from pathlib import Path
from typing import NoReturn, List

from ..Model import Model
from ..NameableRO import NameableRO
from ..Describable import Describable
from ..Identifiable import Identifiable
from ..config.NumOption import NumOption
from ..config.BoolOption import BoolOption
from ..config.FileOption import FileOption
from ..config.EnumOption import EnumOption
from ..config.ConfigModel import ConfigModel


class ItemModel(NameableRO, Describable, Identifiable, Model, ABC):
    """This class contains the basic structure for all Drag and Drop items"""

    def __init__(self, name: str, description: str, config: ConfigModel, item_id: int):
        """Initialising an ItemModel object

        Args:
            name (str): Name of this item
            description (str): Description of this item
            config (ConfigModel): A configuration of adjustable options for this item
            item_id (int): ID of this item
        """
        NameableRO.__init__(self, name)
        Describable.__init__(self, description)
        Identifiable.__init__(self, item_id)
        Model.__init__(self)

        self._config: ConfigModel = config

    @property
    def config(self) -> ConfigModel:
        """Configuration of options for this item"""
        return copy.deepcopy(self._config)

    def set_config(self, config: ConfigModel) -> NoReturn:
        """Sets all values of the config of this item to values of a given configuration

        Args:
            config (ConfigModel): The Configuration, which contains the new values for every option of this item
        """
        file_options: List[FileOption] = config.file_options
        enum_options: List[EnumOption] = config.enum_options
        num_options: List[NumOption] = config.num_options
        bool_options: List[BoolOption] = config.bool_options
        for option in file_options:
            self._config.set_file_option(file_options.index(option), option.path)
        for option in enum_options:
            self._config.set_enum_option(enum_options.index(option), option.selection)
        for option in num_options:
            self._config.set_num_option(num_options.index(option), option.number)
        for option in bool_options:
            self._config.set_bool_option(bool_options.index(option), option.enabled)

    def set_bool_option(self, index: int, value: bool) -> NoReturn:
        """Sets the value of a BoolOption on a specific index

        Args:
            index (int): Index of the BoolOption in the config of this item
            value (bool): Value, on which the value of the BoolOption will be set

        Raises:
            IndexError: If the specified index doesnt exist
        """
        if index >= len(self._config.bool_options) or index < 0:
            raise IndexError("Index %i for a boolean option is out of range" % (index,))
        self._config.set_bool_option(index, value)

    def set_file_option(self, index: int, path: Path) -> NoReturn:
        """Sets the path of a FileOption on a specific index

        Args:
            index (int): Index of the FileOption in the config of this item
            path (str): Path, on which the path of the FileOption will be set

        Raises:
            IndexError: If the specified index doesnt exist
        """
        if index >= len(self._config.file_options) or index < 0:
            raise IndexError("Index %i for a file option is out of range" % (index,))
        self._config.set_file_option(index, path)

    def set_enum_option(self, index: int, selection: int) -> NoReturn:
        """Sets the selection of a EnumOption on a specific index

        Args:
            index (int): Index of the EnumOption in the config of this item
            selection (int): Selection-index, on which the selection of the EnumOption will be set

        Raises:
            IndexError: If the specified index doesnt exist
        """
        if index >= len(self._config.enum_options) or index < 0:
            raise IndexError("Index %i for enumerable option is out of range" % (index,))
        self._config.set_enum_option(index, selection)

    def set_num_option(self, index: int, number: float) -> NoReturn:
        """Sets the number of a NumOption on a specific index

        Args:
            index (int): Index of the NumOption in the config of this item
            number (float): Number, on which the number of the NumOption will be set

        Raises:
            IndexError: If the specified index doesnt exist
        """
        if index >= len(self._config.num_options) or index < 0:
            raise IndexError("Index %i for a numerical option is out of range" % (index,))
        self._config.set_num_option(index, number)

    @staticmethod
    @abstractmethod
    def get_name() -> str:
        return ""
