from typing import NoReturn

from .OptionModel import OptionModel


class BoolOption(OptionModel):
    """This class represents an boolean option from an Drag and Drop item

    A boolean option can only be True or False.
    """

    def __init__(self, name: str, description: str = '', start_value: bool = False):
        """Initialising an FileOption object

        Args:
            name (str): Name of this option
            description (str): Description of this option
            start_value (bool): Start value of this option
        """
        super().__init__(name, description)

        self.__enabled: bool = start_value

    @property
    def enabled(self) -> bool:
        """State of this option"""
        return self.__enabled

    @enabled.setter
    def enabled(self, value: bool) -> NoReturn:
        self.__enabled = value
