from typing import Dict, NoReturn, List, Callable
from ..item.Input import Input
from ..item.Output import Output
from ..item.SensorItem import SensorItem


class WorkspaceModel:
    __next_id: int = 0
    __input_list: Dict[int, Input] = {}
    __output_list: Dict[int, Output] = {}

    @staticmethod
    def __update_input(input_id: int, output_id: int) -> NoReturn:
        WorkspaceModel.__input_list[input_id].connected_to = output_id

    @staticmethod
    def __update_output(output_id: int, input_id: int) -> NoReturn:
        if input_id == -1:
            WorkspaceModel.__output_list[output_id].delete_all_connections()
        else:
            WorkspaceModel.__output_list[output_id].add_connection(input_id)

    @staticmethod
    def add_input(input: Input) -> int:
        id: int = WorkspaceModel.__next_id
        WorkspaceModel.__next_id += 1
        WorkspaceModel.__input_list[id] = input
        return id

    @staticmethod
    def add_output(output: Output) -> int:
        id: int = WorkspaceModel.__next_id
        WorkspaceModel.__next_id += 1
        WorkspaceModel.__output_list[id] = output
        return id

    @staticmethod
    def delete_input(id: int) -> NoReturn:
        if WorkspaceModel.delete_input_connection(id):
            WorkspaceModel.__input_list.pop(id)

    @staticmethod
    def delete_output(id: int) -> NoReturn:
        if WorkspaceModel.delete_output_connections(id):
            WorkspaceModel.__output_list.pop(id)

    @staticmethod
    def delete_input_connection(input_id: int) -> bool:
        connected_id: int = WorkspaceModel.__input_list[input_id].connected_to
        if connected_id in WorkspaceModel.__output_list.keys():
            WorkspaceModel.__output_list[connected_id].delete_connection(input_id)
            WorkspaceModel.__update_input(input_id, -1)
            return True
        else:
            return False


    @staticmethod
    def delete_output_connections(output_id: int) -> bool:
        connected_ids: List[int] = WorkspaceModel.__output_list[output_id].get_connections()
        for id in connected_ids:
            if id in WorkspaceModel.__input_list.keys():
                WorkspaceModel.__update_input(id, -1)
            else:
                return False
        WorkspaceModel.__update_output(output_id, -1)
        return True

    @staticmethod
    def connect(input_id: int, output_id: int) -> NoReturn:
        WorkspaceModel.__update_input(input_id, output_id)
        WorkspaceModel.__update_output(output_id, input_id)

    @staticmethod
    def calculate_function(output_id: int) -> Callable[[Dict[SensorItem, List[float]]], float]:
        if output_id in WorkspaceModel.__output_list.keys():
            return WorkspaceModel.__output_list[output_id].calculate_function()
        else:
            return None

    @staticmethod
    def calculate_unit(output_id: int) -> str:
        if output_id in WorkspaceModel.__output_list.keys():
            return WorkspaceModel.__output_list[output_id].calculate_unit()
        else:
            return None

