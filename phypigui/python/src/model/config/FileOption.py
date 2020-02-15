import copy

from typing import NoReturn, List
from pathlib import Path, PurePath

from .OptionModel import OptionModel
from ..ModelExceptions import PathDoesntExist


class FileOption(OptionModel):
    """This class represents a path-selecting option"""

    ANYFILE: int = 0
    EXISTINGFILE: int = 1
    DIR: int = 2

    def __init__(self, name: str, description: str = '', file_opening_mode: int = 0
                 , file_type: str = '', file_endings: List[str] = ["ppg"]):
        """Initialising a FileOption object

        Args:
            name (str): Name of this option
            description (str): Description of this option
            file_opening_mode (int): Indicates, what should be selectable. If it is out of range it will be 0.
                0: Every file (existing or not)
                1: Only existing files
                2: Only directories
            file_type (str): Name of the allowed file-type
            file_endings (List[str]): List of all allowed file-endings (without the dot)
        """
        super().__init__(name, description)
        self.__file_mode: int = 0
        if 0 < file_opening_mode < 3:
            self.__file_mode = file_opening_mode
        self.__file_type: str = file_type
        self.__file_endings: List[str] = file_endings

        self.__path: PurePath = PurePath()

    @property
    def file_mode(self) -> int:
        """Mode, which files/directories should be selectable
            0: Every file (existing or not)
            1: Only existing files
            2: Only directories
        """
        return self.__file_mode

    @property
    def file_type(self) -> str:
        """Name of the allowed file-type (See also file_endings)"""
        return self.__file_type

    @property
    def file_endings(self) -> List[str]:
        """List of endings, which specify the file-type to be selected

        The Endings are only the letters and contain no dots
        """
        return self.__file_endings

    @property
    def path(self) -> PurePath:
        """Path of an file/directory, which is part of this option

        Raises:
            PathDoesntExist: If the path doesn't exist
        """
        return copy.deepcopy(self.__path)

    @path.setter
    def path(self, new_path: PurePath) -> NoReturn:
        if self.__file_mode != 0 and not Path(str(new_path)).exists():
            raise PathDoesntExist("The selected path %s from the option %s doesn't exist" % (str(new_path), self._name, ))
        self.__path = new_path
