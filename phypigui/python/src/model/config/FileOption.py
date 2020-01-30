from .OptionModel import OptionModel
from typing import NoReturn
from pathlib import Path
from typing import List


class FileOption(OptionModel):
    ANYFILE: int = 0
    EXISTINGFILE: int = 1
    DIR: int = 2

    def __init__(self, name: str, description: str = '', file_opening_mode: int = 0
                 , file_type: str = '', file_endings: List[str] = None):
        super().__init__(name, description)
        self.__file_mode: int = file_opening_mode
        self.__file_type: str = file_type
        self.__file_endings: List[str] = file_endings

        self.__path: str = ''

    @property
    def file_mode(self) -> int:
        return self.__file_mode

    @property
    def file_type(self) -> str:
        return self.__file_type

    @property
    def file_endings(self) -> List[str]:
        return self.__file_endings

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, new_path: str) -> NoReturn:
        if Path(new_path).is_file():
            self.__path = new_path
