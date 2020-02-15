import copy

from typing import List, NoReturn
from pathlib import PurePath

from .BoolOption import BoolOption
from .FileOption import FileOption
from .EnumOption import EnumOption
from .NumOption import NumOption


class ConfigModel:
    """This class represents an configuration of options of a Drag and Drop item

    A configuration contains one list per option type
    """

    def __init__(self):
        """Initialising an ConfigModel object"""
        self.__bool_options: List[BoolOption] = []
        self.__file_options: List[FileOption] = []
        self.__enum_options: List[EnumOption] = []
        self.__num_options: List[NumOption] = []

    @property
    def bool_options(self) -> List[BoolOption]:
        """Copy of List of all boolean options in this config"""
        return copy.deepcopy(self.__bool_options)

    @property
    def file_options(self) -> List[FileOption]:
        """Copy of List of all path-selecting options in this config"""
        return copy.deepcopy(self.__file_options)

    @property
    def enum_options(self) -> List[EnumOption]:
        """Copy of List of all enumerable options in this config"""
        return copy.deepcopy(self.__enum_options)

    @property
    def num_options(self) -> List[NumOption]:
        """Copy of List of all numerical options in this config"""
        return copy.deepcopy(self.__num_options)

    @property
    def empty(self) -> bool:
        bool, file, enum, num = [len(options) == 0 for options in
                      [self.__bool_options, self.__file_options, self.__enum_options, self.__num_options]]
        return bool and file and enum and num

    def add_bool_option(self, option: BoolOption) -> int:
        """Adds an boolean option to this config

        Adds an boolean option to this config.
        The user can modify this option in generic generated settings-window.
        Maximum size for the name of this option should be 50 Symbols.
        Maximum size for the description of this option should be two lines with 50 Symbols each.

        Args:
            option (BoolOption): Boolean option, which will be added to this config

        Return:
            int: Returns index from the added option in the list of BoolOptions
        """
        self.__bool_options.append(option)
        return self.__bool_options.index(option)

    def add_file_option(self, option: FileOption) -> int:
        """Adds an file-option to this config

        Adds an file-option to this config.
        The user can modify this option in generic generated settings-window.
        Maximum size for the name of this option should be 22 Symbols.
        Maximum size for the description of this option should be two lines with 22 Symbols each.

        Args:
            option (FileOption): File-option, which will be added to this config

        Return:
            int: Returns index from the added option in the list of FileOptions
        """
        self.__file_options.append(option)
        return self.__file_options.index(option)

    def add_enum_option(self, option: EnumOption) -> int:
        """Adds an enum-option to this config

        Adds an enum-option to this config.
        The user can modify this option in generic generated settings-window.
        Maximum size for the name of this option should be 28 Symbols.
        Maximum size for the description of this option should be two lines with 28 Symbols each.
        Maximum size for each element is 21 Symbols.

        Args:
            option (EnumOption): Enum-option, which will be added to this config

        Return:
            int: Returns index from the added option in the list of EnumOptions
        """
        self.__enum_options.append(option)
        return self.__enum_options.index(option)

    def add_num_option(self, option: NumOption) -> int:
        """Adds an numerical option to this config

        Adds an numerical option to this config.
        The user can modify this option in generic generated settings-window.
        Maximum size for the name of this option should be 30 Symbols.
        Maximum size for the description of this option should be two lines with 30 Symbols each.

        Args:
            option (NumOption): Numerical option, which will be added to this config

        Return:
            int: Returns index from the added option in the list of NumOptions
        """
        self.__num_options.append(option)
        return self.__num_options.index(option)

    def set_bool_option(self, index: int, value: bool) -> NoReturn:
        """Sets the value of a BoolOption

        Sets the value of a BoolOption on a specific index in the list of this config, if index is valid.

        Args:
            index (int): Index of option, which will be set
            value (bool): Value on which the option will be set

        Raises:
            IndexError: If the index of the option is out of range
        """
        if index < 0 or index >= len(self.bool_options):
            raise IndexError("The index %d for this boolean option is out of range." % (index,))
        self.__bool_options[index].enabled = value

    def set_file_option(self, index: int, path: PurePath) -> NoReturn:
        """Sets the path of a FileOption

        Sets the path of a FileOption on a specific index in the list of this config, if index is valid.

        Args:
            index (int): Index of option, which will be set
            path (PurePath): Path on which the option will be set

        Raises:
            IndexError: If the index of the option is out of range
            PathDoesntExist: If the path doesn't exist
        """
        if index < 0 or index >= len(self.__file_options):
            raise IndexError("The index %d for this path-selecting option is out of range." % (index,))
        self.__file_options[index].path = path

    def set_enum_option(self, index: int, selection: int) -> NoReturn:
        """Sets the selection of an EnumOption

        Sets the selection of an EnumOption on a specific index in the list of this config, if index is valid.

        Args:
            index (int): Index of option, which will be set
            selection (int): Selection on which the option will be set

        Raises:
            IndexError: If the index of the option is out of range
            OutOfRange: If the index of the selection in the enum is out of range
        """
        if index < 0 or index >= len(self.__enum_options):
            raise IndexError("The index %d for this enumerable option is out of range." % (index,))
        self.__enum_options[index].selection = selection

    def set_num_option(self, index: int, number: float) -> NoReturn:
        """Sets the number of a NumOption

        Sets the number of a NumOption on a specific index in the list of this config, if index is valid.

        Args:
            index (int): Index of option, which will be set
            number (float): Number on which the option will be set

        Raises:
            IndexError: If the index of the option is out of range
            NumberTooLarge: If the number is greater than the maximum allowed number for this option
            NumberTooSmall: If the number is smaller than the minimum allowed number for this option
        """
        if index < 0 or index >= len(self.__num_options):
            raise IndexError("The index %d for this numerical option is out of range." % (index,))
        self.__num_options[index].number = number
