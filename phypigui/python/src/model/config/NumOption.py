from ..NameableRO import NameableRO
from typing import NoReturn


class NumOption(NameableRO):

    def __init__(self, name: str):
        self.__number: float = 0
        self._name = name

    def get_number(self) -> float:
        return self.__number

    def set_number(self, number: float) -> NoReturn:
        self.__number = number

    number: float = property(get_number(), set_number())