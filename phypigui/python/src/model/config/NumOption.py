from ..NameableRO import NameableRO
from typing import NoReturn
import sys
import math


class NumOption(NameableRO):

    def __init__(self, name: str, num: float = 0, min: float = -sys.float_info.max, max: float = sys.float_info.max
                 , decimals: int = 20):
        super().__init__(name)
        self.__number: float = num
        self.__min: float = min
        self.__max: float = max
        self.__decimals: int = decimals

    @property
    def number(self) -> float:
        return self.__number

    @number.setter
    def number(self, value: float) -> NoReturn:
        self.__number = value

    @property
    def min(self) -> float:
        return self.__min

    @property
    def max(self) -> float:
        return self.__max

    @property
    def decimals(self) -> int:
        return self.__decimals
