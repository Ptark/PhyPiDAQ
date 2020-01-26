from ..NameableRO import NameableRO
from typing import NoReturn


class NumOption(NameableRO):

    def __init__(self, name: str, num: float = 0):
        super().__init__(name)
        self.__number: float = num

    @property
    def number(self) -> float:
        return self.__number

    @number.setter
    def number(self, value: float) -> NoReturn:
        self.__number = value
