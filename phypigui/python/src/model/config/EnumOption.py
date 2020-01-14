from ..NameableRO import NameableRO
from typing import NoReturn
import enum


class EnumOption(NameableRO):

    def __init__(self, name: str, samples: enum, start_selection: int = 0):
        super().__init__(name)
        self.__samples: enum = samples
        self.__selection: int = start_selection

    @property
    def selection(self) -> int:
        return self.__selection

    @selection.setter
    def selection(self, index: int) -> NoReturn:
        if index >= 0:
            self.__selection = index

    def get_samples(self) -> enum:
        return self.__samples
