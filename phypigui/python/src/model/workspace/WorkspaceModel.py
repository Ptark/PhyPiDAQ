from typing import Dict, NoReturn, List, Callable
from ..item import Input, Output, SensorItem, ItemModel


class WorkspaceModel:
    __next_id: int = 0
    __input_list: Dict[int, Input.Input] = {}
    __output_list: Dict[int, Output.Output] = {}

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
    def check_input_id(input_id: int) -> bool:
        pass #TODO

    @staticmethod
    def check_output_id(output_id: int) -> bool:
        pass #TODO

    @staticmethod
    def add_input(input: Input.Input) -> int:
        """Adds an Input-Object to global list of inputs

            Adds an Input-Object to global list of inputs and returns next free ID.
            This method is called every time a Input-Object was created.
            The returned ID should set as id for input.

            Args:
                input (Input): Input, which will be added to the list

            Returns:
                int: Next free id
        """
        id: int = WorkspaceModel.__next_id
        WorkspaceModel.__next_id += 1
        WorkspaceModel.__input_list[id] = input
        return id

    @staticmethod
    def add_output(output: Output.Output) -> int:
        """Adds an Output-Object to global list of outputs

                Adds an Output-Object to global list of outputs and returns next free ID.
                This method is called every time a Output-Object was created.
                The returned ID should set as id for output.

                Args:
                    output (Output): Output, which will be added to the list

                Returns:
                    int: Next free id
        """
        id: int = WorkspaceModel.__next_id
        WorkspaceModel.__next_id += 1
        WorkspaceModel.__output_list[id] = output
        return id

    @staticmethod
    def add_item(item: ItemModel.ItemModel) -> int:
        pass #TODO

    @staticmethod
    def delete_input(id: int) -> NoReturn:
        """Deletes an input

        Deletes an input and refreshes all items, which are connected to this input

        Args:
            id (int): ID of input, which will be deleted
        """
        if WorkspaceModel.delete_connection(id):
            WorkspaceModel.__input_list.pop(id)

    @staticmethod
    def delete_output(id: int) -> NoReturn:
        """Deletes an output

        Deletes an output und refreshes all items, which are connected to this output

        Args:
            id (int): ID of output, which will be deleted
        """
        if WorkspaceModel.delete_all_output_connections(id):
            WorkspaceModel.__output_list.pop(id)

    @staticmethod
    def delete_connection(input_id: int) -> bool:
        """Deletes a connection between two items

        Deletes a connection identified by an input-ID and refreshes all items, which are part of the connection

        Args:
             input_id (int): ID of input, which are part of the connection to be deleted

        Returns:
            bool: False, if there is no connection from this input
                    or if connected output doesn't exist
        """
        connected_id: int = WorkspaceModel.__input_list[input_id].connected_to
        if connected_id in WorkspaceModel.__output_list.keys():
            WorkspaceModel.__output_list[connected_id].delete_connection(input_id)
            WorkspaceModel.__update_input(input_id, -1)
            return True
        else:
            return False

    @staticmethod
    def delete_all_output_connections(output_id: int) -> bool:
        """Deletes all connection from one output

        Deletes all connections identified by an output-ID and refreshes all items, which ire part of the connection

        Args:
            output_id (int): ID of output, which are part of all connections to be deleted

        Returns:
              bool: False, if one of the connected inputs doesn't exist
        """
        connected_ids: List[int] = WorkspaceModel.__output_list[output_id].connected_to
        for id in connected_ids:
            if id in WorkspaceModel.__input_list.keys():
                WorkspaceModel.__update_input(id, -1)
            else:
                return False
        WorkspaceModel.__update_output(output_id, -1)
        return True

    @staticmethod
    def connect(input_id: int, output_id: int) -> NoReturn:
        """Connects two items

            Connects two items and updates there attributes

            Args:
                input_id (int): Input-ID of input, which is part of connection
                output_id (int): Output-ID of output, which is part of connection
        """
        WorkspaceModel.__update_input(input_id, output_id)
        WorkspaceModel.__update_output(output_id, input_id)

    @staticmethod
    def calculate_function(output_id: int) -> Callable[[Dict[SensorItem.SensorItem, List[float]]], float]:
        """Calculates lambda-function from output

        Calculates lambda-function from output identified by its ID and all its previous outputs recursively

        Args:
            output_id (int): ID of the output

        Returns:
            Callable[[Dict[SensorItem, List[float]]], float]: Lambda-function from output
        """
        if output_id in WorkspaceModel.__output_list.keys():
            return WorkspaceModel.__output_list[output_id].calculate_function()
        else:
            return lambda data: 0

    @staticmethod
    def calculate_unit(output_id: int) -> str:
        """Calculates unit from output

            Calculates unit from output identified by its ID and all its previous outputs recursively

            Args:
                output_id (int): ID of the output

            Returns:
                str: Unit from output
        """
        if output_id in WorkspaceModel.__output_list.keys():
            return WorkspaceModel.__output_list[output_id].calculate_unit()
        else:
            return ''

    @staticmethod
    def invalidate_functions(output_id: int) -> NoReturn:
        """Invalidates all lambda-function in sequel items after a output

        Invalidates all lambda-function in sequel items after a output identified by its ID

        Args:
            output_id (int): ID of the output
        """
        for input_id in WorkspaceModel.__output_list[output_id].connected_to:
            WorkspaceModel.__input_list[input_id].invalidate_functions()
