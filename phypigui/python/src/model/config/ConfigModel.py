from typing import List, NoReturn
from .BoolOption import BoolOption
from .FileOption import FileOption
from .EnumOption import EnumOption
from .NumOption import NumOption


class ConfigModel:

    def __init__(self):
        self.__bool_options: List[BoolOption] = []
        self.__file_options: List[FileOption] = []
        self.__enum_options: List[EnumOption] = []
        self.__num_options: List[NumOption] = []

    @property
    def bool_options(self) -> List[BoolOption]:
        return self.__bool_options.copy()

    @property
    def file_options(self) -> List[FileOption]:
        return self.__file_options.copy()

    @property
    def enum_options(self) -> List[EnumOption]:
        return self.__enum_options.copy()

    @property
    def num_options(self) -> List[NumOption]:
        return self.__num_options.copy()

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
        self.__file_options.append(option)
        return self.__file_options.index(option)

    def add_enum_option(self, option: EnumOption) -> int:
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
        if 0 <= index < len(self.__bool_options):
            self.__bool_options[index].enabled = value

    def set_file_option(self, index: int, path: str) -> NoReturn:
        if 0 <= index < len(self.__file_options):
            self.__file_options[index].path = path

    def set_enum_option(self, index: int, selection: int) -> NoReturn:
        if 0 <= index < len(self.__bool_options):
            if 0 <= selection < len(self.__enum_options[index].samples()):
                self.__enum_options[index].selection = selection

    def set_num_option(self, index: int, number: float) -> NoReturn:
        if 0 <= index < len(self.__num_options):
            self.__num_options[index].number = number
