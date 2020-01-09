from ..NameableRO import NameableRO
from typing import NoReturn


class BoolOption(NameableRO):

    def __init__(self, name: str, start_value: bool = False):
        self.__enabled: bool = start_value
        self._name = name

    def get_enabled(self) -> bool:
        return self.__enabled

    def set_enabled(self, value: bool) -> NoReturn:
        self.__enabled = value

    enabled: bool = property(get_enabled(), set_enabled())
