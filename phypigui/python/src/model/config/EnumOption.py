from ..NameableRO import NameableRO
from typing import NoReturn
import enum


class NumOption(NameableRO):

    def __init__(self, name: str, samples: enum, start_selection: int = 0):
        self.__samples: enum = samples
        self.__selection: int = start_selection
        self._name = name

    def get_selection(self) -> int:
        return self.__selection

    def get_samples(self) -> enum:
        return self.__samples

    def set_selection(self, index: int) -> NoReturn:
        self.__selection = index

    selection: int = property(get_selection(), set_selection())
