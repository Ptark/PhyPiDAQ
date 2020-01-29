from .OptionModel import OptionModel
from typing import NoReturn
from pathlib import Path


class FileOption(OptionModel):

    def __init__(self, name: str, description: str = ''):
        super().__init__(name, description)
        self.__path: str = ''

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, new_path: str) -> NoReturn:
        if Path(new_path).is_file():
            self.__path = new_path
