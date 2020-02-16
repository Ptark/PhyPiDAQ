import sys

from typing import NoReturn

from .OptionModel import OptionModel
from ...Exceptions import NumberTooLarge, NumberTooSmall


class NumOption(OptionModel):
    """This class represents an numerical option

    This option contains an adjustable numerical value.
    """

    def __init__(self, name: str, description: str = '', num: float = 0, min: float = -sys.float_info.max
                 , max: float = sys.float_info.max , decimals: int = 20):
        """Initialising an NumOption object

        Args:
            name (str): Name of this option
            description (str): Description of this option
            num (float): Number, which is value of this option by default
            min (float): Minimum number this option can be
            max (float): Maximum number this option can be
            decimals (int): Count of decimals
        """
        super().__init__(name, description)

        self.__number: float = num
        self.__min: float = min
        self.__max: float = max
        self.__decimals: int = decimals

    @property
    def number(self) -> float:
        """Number, which was adjusted for this option

        Raises:
            NumberTooLarge: If the number is greater than the maximum allowed number for this option
            NumberTooSmall: If the number is smaller than the minimum allowed number for this option
        """
        return self.__number

    @number.setter
    def number(self, value: float) -> NoReturn:
        if value > self.__max:
            raise NumberTooLarge(self._name, self.__max)
        elif value < self.__min:
            raise NumberTooSmall(self._name, self.__min)
        self.__number = round(value, self.decimals)

    @property
    def min(self) -> float:
        """Minimum number this option can be"""
        return self.__min

    @property
    def max(self) -> float:
        """Maximum number this option can be"""
        return self.__max

    @property
    def decimals(self) -> int:
        """Count of decimals for this option"""
        return self.__decimals
