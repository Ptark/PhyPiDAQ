import copy
from enum import Enum

from typing import NoReturn, Type

from .OptionModel import OptionModel
from ..ModelExceptions import OutOfRange


class EnumOption(OptionModel):
    """This class represents an enumerable option from an Drag and Drop item

    This option has an enum, which contains multiple values.
    Only the values of the enum will be excepted from this option.
    """

    def __init__(self, name: str, samples: Type[Enum], description: str = '', start_selection: int = 0):
        """Initialising an BoolOption object

        Args:
            name (str): Name of this option
            samples (enum): An enum of all possible values this option except
            description (str): Description of this option
            start_selection (int): Index, which should be selected in samples by default
        """
        super().__init__(name, description)

        self.__samples: Type[Enum] = samples
        self.__selection: int = start_selection

    @property
    def selection(self) -> int:
        """Index of selected value in the enum

        Raises:
            OutOfRange: If the selected index is smaller than zero or greater than the length of samples
        """
        return self.__selection

    @selection.setter
    def selection(self, selection_index: int) -> NoReturn:
        if 0 > selection_index or selection_index >= len(self.__samples):
            raise OutOfRange("The selected index %d of option %s is out of range" % (selection_index, self._name, ))
        self.__selection = selection_index

    @property
    def samples(self) -> Type[Enum]:
        """Enum of all possible values for this option"""
        return copy.deepcopy(self.__samples)
