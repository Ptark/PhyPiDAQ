from .OptionModel import OptionModel
from typing import NoReturn
import enum
import copy


class EnumOption(OptionModel):

    def __init__(self, name: str, samples: enum, description: str = '', start_selection: int = 0):
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
        return copy.deepcopy(self.__samples)
