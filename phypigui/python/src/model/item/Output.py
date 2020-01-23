from ..workspace import WorkspaceModel
from typing import List, Dict, Callable, NoReturn
from . import SensorItem
from .. import Identifiable


class Output(Identifiable.Identifiable):
    def __init__(self, parent_id: int, output_number: int):
        super().__init__(WorkspaceModel.WorkspaceModel.add_output(self))
        self.__parent_item: int = parent_id
        self.__connected_to: List[int] = []
        self.__number_of_output: int = output_number
        self.__function: Callable[[Dict[SensorItem.SensorItem, List[float]]], float] = lambda data: 0
        self.__is_function_valid: bool = False
        self.__data: float = 0
        self.__unit: str = ''

    @property
    def connected_to(self) -> List[int]:
        return self.__connected_to.copy()

    @property
    def number_of_output(self) -> int:
        return self.__number_of_output

    @property
    def unit(self) -> str:
        return self.__unit

    @property
    def data(self) -> float:
        return self.__data

    def add_connection(self, input_id: int) -> NoReturn:
        """Adds an input-ID to the list of connected inputs to this output

        Args:
            input_id (int): ID of the input
        """
        if WorkspaceModel.WorkspaceModel.check_input_id(input_id):
            self.__connected_to.append(input_id)

    def delete_connection(self, input_id) -> bool:
        """Deletes an input-ID of the list of connected inputs to this output

        Args:
            input_id (int): ID of the input

        Returns:
            bool: False, if input_id doesn't exist or are in the list
        """
        if WorkspaceModel.WorkspaceModel.check_input_id(input_id) and input_id in self.__connected_to:
            self.__connected_to.pop(input_id)
            return True
        return False

    def delete_all_connections(self) -> NoReturn:
        """Deletes all input-IDs of the list of connected inputs of this output
        """
        self.__connected_to.clear()

    def calculate_function(self) -> Callable[[Dict[SensorItem.SensorItem, List[float]]], float]:
        """Calculates lambda-function for this output and returns it

        Calculates lambda-function for this output recursively

        Returns:
            Callable[[Dict[SensorItem.SensorItem, List[float]]], float]: calculated lambda-function for this output
        """
        if not self.__is_function_valid:
            self.__function = WorkspaceModel.WorkspaceModel.calculate_function(self.__id)
            self.__is_function_valid = True
        return self.__function

    def calculate_unit(self) -> str:
        """Calculates unit for this output and returns it

        Calculates lambda-function for this output recursively and stores it

        Returns:
            str: calculated unit for this output
        """
        self.__unit = WorkspaceModel.WorkspaceModel.calculate_unit(self.__id)
        return self.__unit

    def calculate(self, data: Dict[SensorItem.SensorItem, List[float]]) -> NoReturn:
        """Plugs data in lambda-function und stores result

        Args:
            data (Dict[SensorItem.SensorItem, List[float]]): Data, which will plug in lambda-function
        """
        self.__data = self.__function(data)
