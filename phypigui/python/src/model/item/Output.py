from typing import List, Dict, Callable, NoReturn

from ..Identifiable import Identifiable
from ..workspace.WorkspaceModel import WorkspaceModel


class Output(Identifiable):
    """This class represents a output of an OutputItem

     Objects from this class are typically created in the constructor of an OutputItem.
    """
    def __init__(self, parent_id: int, output_number: int):
        """Initialising an Output object

        Args:
            parent_id (int): ID of the OutputItem, which this output belongs to
            output_number (int): Number this output has in its parent item
        """
        super().__init__(WorkspaceModel.add_output(self))
        self.__parent_item_id: int = parent_id
        self.__number_of_output: int = output_number
        self.__function: Callable[[Dict['SensorItem', List[float]]], float] = lambda data: 0
        self.__is_function_valid: bool = False
        self.__data: float = 0
        self.__unit: str = ''

    @property
    def parent_item_id(self) -> int:
        """ID of the OutputItem, which this output belongs to"""
        return self.__parent_item_id

    @property
    def number_of_output(self) -> int:
        """Number this output has in its parent item"""
        return self.__number_of_output

    @property
    def unit(self) -> str:
        """Unit of the calculated data this output supplies"""
        return self.__unit

    @unit.setter
    def unit(self, new_unit: str) -> NoReturn:
        self.__unit = new_unit

    @property
    def function(self) -> Callable[[Dict['SensorItem', List[float]]], float]:
        """The constructed lambda-function for this output

        It is a constant zero function, if the stored function is not valid or the parent item has no valid connections
        to enough sensors.
        Next time the ManagerModel initialises the lambda-functions, this lambda-function will be updated.
        """
        if not self.__is_function_valid:
            self.__function = lambda data: 0
        return self.__function

    @function.setter
    def function(self, new_function: Callable[[Dict['SensorItem', List[float]]], float]) -> NoReturn:
        self.__function = new_function
        self.__is_function_valid = True

    @property
    def is_function_valid(self) -> bool:
        """Indicates, if the lambda-function for this output has been constructed and is valid"""
        return self.__is_function_valid

    @property
    def data(self) -> float:
        """Last calculated value for this output"""
        return self.__data

    def invalidate_function(self) -> NoReturn:
        """Invalidates the lambda-function of this output and all sequel items"""
        self.__is_function_valid = False
        WorkspaceModel.invalidate_functions(self._id)

    def calculate(self, data: Dict['SensorItem', List[float]]) -> NoReturn:
        """Plugs data in the lambda-function of this output und stores the result

        Args:
            data (Dict[SensorItem.SensorItem, List[float]]): Data, which will be plugged in lambda-function
        """
        self.__data = self.__function(data)
