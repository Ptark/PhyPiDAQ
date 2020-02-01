import enum
import copy

from typing import NoReturn

from .OptionModel import OptionModel


class EnumOption(OptionModel):
    """This class represents an enumerable option from an Drag and Drop item

    This option has an enum, which contains multiple values.
    Only the values of the enum will be excepted from this option.
    """

    def __init__(self, name: str, samples: enum, description: str = '', start_selection: int = 0):
        """Initialising an BoolOption object

        Args:
            name (str): Name of this option
            samples (enum): An enum of all possible values this option except
            description (str): Description of this option
            start_selection (int): Index, which should be selected in samples by default
        """
        super().__init__(name, description)

        self.__samples: enum = samples
        self.__selection: int = start_selection

    @property
    def selection(self) -> int:
        """Index of selected value in the enum"""
        return self.__selection

    @selection.setter
    def selection(self, selection_index: int) -> NoReturn:
        if selection_index >= 0:
            self.__selection = selection_index

    @property
    def samples(self) -> enum:
        """Enum of all possible values for this option"""
        return copy.deepcopy(self.__samples)
