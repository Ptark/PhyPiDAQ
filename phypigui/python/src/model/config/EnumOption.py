from .OptionModel import OptionModel
from typing import NoReturn
import enum


class EnumOption(OptionModel):

    def __init__(self, name: str, samples: enum, description: str = '', start_selection: int = 1):
        super().__init__(name, description)
        self.__samples: enum = samples
        self.__selection: int = start_selection

    @property
    def selection(self) -> int:
        return self.__selection

    @selection.setter
    def selection(self, index: int) -> NoReturn:
        if index >= 0:
            self.__selection = index

    @property
    def samples(self) -> enum:
        return self.__samples.copy()
