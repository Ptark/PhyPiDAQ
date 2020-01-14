from ..NameableRO import NameableRO
from typing import NoReturn


class BoolOption(NameableRO):

    def __init__(self, name: str, start_value: bool = False):
        super().__init__(name)
        self.__enabled: bool = start_value

    @property
    def enabled(self) -> bool:
        return self.__enabled

    @enabled.setter
    def enabled(self, value: bool) -> NoReturn:
        self.__enabled = value
