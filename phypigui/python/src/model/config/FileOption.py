from ..NameableRO import NameableRO
from typing import NoReturn


class FileOption(NameableRO):

    def __init__(self, name: str):
        self.__path: str = ''
        self._name = name

    def get_path(self) -> str:
        return self.__path

    def set_path(self, path: str) -> NoReturn:
        self.__path = path

    path: str = property(get_path(), set_path())
