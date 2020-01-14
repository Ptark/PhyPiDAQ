from ..NameableRO import NameableRO
from typing import NoReturn


class FileOption(NameableRO):

    def __init__(self, name: str):
        super().__init__(name)
        self.__path: str = ''

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, new_path: str) -> NoReturn:
        self.__path = new_path
