from ..workspace import WorkspaceModel
from typing import List, Dict, Callable, NoReturn
from . import SensorItem
from .. import Identifiable


class Output(Identifiable.Identifiable):
    """Represents one output of an item.

    Items can have Output in a list to represent its outputs.

    Attributes:
        __parent_item_id (int): Id of the item the output belongs to
        __number_of_output (int): The number this output has in the parent item
        __function (Callable[[Dict[SensorItem.SensorItem, List[float]]], float]):
            the constructed delta function of all previous Items
        __is_function_valid (bool): Indicates if the function has been constructed and is valid
        __data (float): Saves the last calculated value for this Output
        __unit (str): Saves the last calculated unit for this Output
    """
    def __init__(self, parent_id: int, output_number: int):
        super().__init__(WorkspaceModel.WorkspaceModel.add_output(self))
        self.__parent_item_id: int = parent_id
        self.__number_of_output: int = output_number
        self.__function: Callable[[Dict[SensorItem.SensorItem, List[float]]], float] = lambda data: 0
        self.__is_function_valid: bool = False
        self.__data: float = 0
        self.__unit: str = ''

    @property
    def parent_item_id(self) -> int:
        return self.__parent_item_id

    @property
    def number_of_output(self) -> int:
        return self.__number_of_output

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, new_unit: str) -> NoReturn:
        self.__unit = new_unit

    @property
    def function(self) -> Callable[[Dict[SensorItem.SensorItem, List[float]]], float]:
        return self.__function

    @function.setter
    def function(self, new_function: Callable[[Dict[SensorItem.SensorItem, List[float]]], float]) -> NoReturn:
        self.__function = new_function
        self.__is_function_valid = True

    @property
    def is_function_valid(self) -> bool:
        return self.__is_function_valid

    @property
    def data(self) -> float:
        return self.__data

    def invalidate_function(self) -> NoReturn:
        """Invalidates the lambda-function of this output and all sequel items
        """
        self.__is_function_valid = False
        WorkspaceModel.WorkspaceModel.invalidate_functions(self._id)

    def calculate_function(self) -> Callable[[Dict[SensorItem.SensorItem, List[float]]], float]:
        """Calculates lambda-function for this output and returns it

        Calculates lambda-function for this output recursively

        Returns:
            Callable[[Dict[SensorItem.SensorItem, List[float]]], float]: calculated lambda-function for this output
        """
        if not self.__is_function_valid:
            self.__function = WorkspaceModel.WorkspaceModel.calculate_function(self._id)
            self.__is_function_valid = True
        return self.__function

    def calculate_unit(self) -> str:
        """Calculates unit for this output and returns it

        Calculates lambda-function for this output recursively and stores it

        Returns:
            str: calculated unit for this output
        """
        self.__unit = WorkspaceModel.WorkspaceModel.calculate_unit(self._id)
        return self.__unit

    def calculate(self, data: Dict[SensorItem.SensorItem, List[float]]) -> NoReturn:
        """Plugs data in lambda-function und stores result

        Args:
            data (Dict[SensorItem.SensorItem, List[float]]): Data, which will plug in lambda-function
        """
        self.__data = self.__function(data)
