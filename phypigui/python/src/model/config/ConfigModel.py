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

    def get_bool_options(self) -> List[BoolOption]:
        return self.__bool_options.copy()

    def get_file_options(self) -> List[FileOption]:
        return self.__file_options.copy()

    def get_enum_options(self) -> List[EnumOption]:
        return self.__enum_options.copy()

    def get_num_options(self) -> List[NumOption]:
        return self.__num_options.copy()

    def set_bool_options(self, options_list: List[BoolOption]) -> NoReturn:
        self.__bool_options = options_list

    def set_file_options(self, options_list: List[FileOption]) -> NoReturn:
        self.__file_options = options_list

    def set_enum_options(self, options_list: List[EnumOption]) -> NoReturn:
        self.__enum_options = options_list

    def set_num_options(self, options_list: List[NumOption]) -> NoReturn:
        self.__num_options = options_list

    bool_options: List[BoolOption] = property(get_bool_options(), set_bool_options())
    file_options: List[FileOption] = property(get_file_options(), set_file_options())
    enum_options: List[EnumOption] = property(get_enum_options(), set_enum_options())
    num_option: List[NumOption] = property(get_num_options(), get_num_options())

    def add_bool_option(self, option: BoolOption) -> int:
        self.__bool_options.append(option)
        return self.__bool_options.index(option)

    def add_file_option(self, option: FileOption) -> int:
        self.__file_options.append(option)
        return self.__file_options.index(option)

    def add_enum_option(self, option: EnumOption) -> int:
        self.__enum_options.append(option)
        return self.__enum_options.index(option)

    def add_num_option(self, option: NumOption) -> int:
        self.__num_options.append(option)
        return self.__num_options.index(option)
