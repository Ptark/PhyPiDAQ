from typing import Dict, NoReturn, List, Callable


class WorkspaceModel:
    __next_id: int = 0
    __input_list: Dict[int, 'Input'] = {}
    __output_list: Dict[int, 'Output'] = {}
    __input_item_list: Dict[int, 'InputItem'] = {}
    __output_item_list: Dict[int, 'OutputItem'] = {}
    __connection_list: Dict[int, 'Connection'] = {}

    @staticmethod
    def __is_output_item(item_id: int) -> bool:
        return item_id in WorkspaceModel.__output_item_list

    @staticmethod
    def get_connection_to_input(input_id: int) -> int:
        """Returns the ID of the output, which is connected to this input identified by its ID

        Args:
            input_id (int): ID of the input

        Returns:
            int: ID of the output or -1, if no connection exists
        """
        if input_id in WorkspaceModel.__connection_list:
            return WorkspaceModel.__connection_list[input_id].output
        return -1

    @staticmethod
    def get_connections_from_output(output_id: int) -> List[int]:
        """Returns a list of IDs of inputs, which are connected to this output identified by its ID

        Args:
            output_id (int): ID of the output

        Returns:
            List[int]: list of input-IDs connected to this output
        """
        inputs: List[int] = []
        for connection in WorkspaceModel.__connection_list.values():
            if connection.output == output_id:
                inputs.append(connection.input)
        return inputs

    @staticmethod
    def check_input_id(input_id: int) -> bool:
        """Checks of an input with this ID exists

        Args:
            input_id (int): ID to be checked

         Returns:
             bool: False, if no input with this ID exists
        """
        return input_id in WorkspaceModel.__input_list

    @staticmethod
    def check_output_id(output_id: int) -> bool:
        """Checks of an output with this ID exists

                Args:
                    output_id (int): ID to be checked

                 Returns:
                     bool: False, if no output with this ID exists
                """
        return output_id in WorkspaceModel.__output_list

    @staticmethod
    def check_item_id(item_id: int) -> bool:
        """Checks of an item with this ID exists

                Args:
                    item_id (int): ID to be checked

                 Returns:
                     bool: False, if no item with this ID exists
                """
        return item_id in WorkspaceModel.__output_item_list or item_id in WorkspaceModel.__input_item_list

    @staticmethod
    def add_input(input: 'Input') -> int:
        """Adds an Input-Object to global list of inputs

            Adds an Input-Object to global list of inputs and returns next free ID.
            This method is called every time a Input-Object was created.
            The returned ID should set as id for this input.

            Args:
                input (Input): Input, which will be added to the list

            Returns:
                int: Next free ID
        """
        id: int = WorkspaceModel.__next_id
        WorkspaceModel.__next_id += 1
        WorkspaceModel.__input_list[id] = input
        return id

    @staticmethod
    def add_output(output: 'Output') -> int:
        """Adds an Output-Object to global list of outputs

        Adds an Output-Object to global list of outputs and returns next free ID.
        This method is called every time a Output-Object was created.
        The returned ID should set as id for this output.

        Args:
            output (Output): Output, which will be added to the list

        Returns:
            int: Next free ID
        """
        id: int = WorkspaceModel.__next_id
        WorkspaceModel.__next_id += 1
        WorkspaceModel.__output_list[id] = output
        return id

    @staticmethod
    def add_input_item(item: 'InputItem') -> int:
        """Adds an InputItem-Object to global list of input-items

        Adds an InputItem-Object to global list of input-items and returns next free ID.
        This method is called every time a InputItem-Object was created.
        The returned ID should set as id for this item.

        Args:
            item (InputItem.InputItem): Item, which will be added to the list

        Returns:
            int: Next free ID
        """
        id: int = WorkspaceModel.__next_id
        WorkspaceModel.__next_id += 1
        WorkspaceModel.__input_item_list[id] = item
        return id

    @staticmethod
    def add_output_item(item: 'OutputItem') -> int:
        """Adds an OutputItem-Object to global list of output-items

        Adds an OutputItem-Object to global list of output-items and returns next free ID.
        This method is called every time a OutputItem-Object was created.
        The returned ID should set as id for this item.

        Args:
            item (OutputItem.OutputItem): Item, which will be added to the list

        Returns:
            int: Next free ID
        """
        id: int = WorkspaceModel.__next_id
        WorkspaceModel.__next_id += 1
        WorkspaceModel.__output_item_list[id] = item
        return id

    @staticmethod
    def delete_item(item_id: int) -> NoReturn:
        """Deletes an item identified by its ID

        Args:
            item_id (int):
        """
        if WorkspaceModel.__is_output_item(item_id):
            WorkspaceModel.__output_item_list.pop(item_id)
        if item_id in WorkspaceModel.__input_item_list:
            WorkspaceModel.__input_item_list.pop(item_id)

    @staticmethod
    def delete_input(input_id: int) -> NoReturn:
        """Deletes an input

        Deletes an input and refreshes all items, which are connected to this input

        Args:
            input_id (int): ID of input, which will be deleted
        """
        if WorkspaceModel.delete_connection(input_id):
            WorkspaceModel.__input_list.pop(input_id)

    @staticmethod
    def delete_output(output_id: int) -> NoReturn:
        """Deletes an output

        Deletes an output und refreshes all items, which are connected to this output

        Args:
            output_id (int): ID of output, which will be deleted
        """
        if WorkspaceModel.delete_all_output_connections(output_id):
            WorkspaceModel.__output_list.pop(output_id)

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
        if input_id in WorkspaceModel.__connection_list:
            input: Input = WorkspaceModel.__input_list[input_id]
            WorkspaceModel.__connection_list.pop(input_id)
            if WorkspaceModel.__is_output_item(input.parent_item_id):
                WorkspaceModel.__output_item_list[input.parent_item_id].invalidate_functions()
            return True
        else:
            return False

    @staticmethod
    def delete_all_output_connections(output_id: int) -> NoReturn:
        """Deletes all connection from one output

        Deletes all connections identified by an output-ID and refreshes all items, which ire part of the connection

        Args:
            output_id (int): ID of output, which are part of all connections to be deleted
        """
        WorkspaceModel.invalidate_functions(output_id)
        for connection in WorkspaceModel.__connection_list.values():
            if connection.output == output_id:
                WorkspaceModel.__connection_list.pop(connection.input)

    @staticmethod
    def connect(input_id: int, output_id: int) -> bool:
        """Connects two items

            Connects two items and updates there attributes

            Args:
                input_id (int): Input-ID of input, which is part of connection
                output_id (int): Output-ID of output, which is part of connection

            Returns:
                bool: False, if no input with input_id or output with output_id exists or if input is already connected
        """
        if input_id in WorkspaceModel.__input_list and output_id in WorkspaceModel.__output_list:
            if input_id not in WorkspaceModel.__connection_list:
                WorkspaceModel.__connection_list[input_id] = Connection(input_id, output_id)
                return True
        return False

    @staticmethod
    def calculate_function(input_id: int) -> Callable[[Dict['SensorItem', List[float]]], float]:
        """Calculates lambda-function from input

        Returns the stored function in the connected output if it is valid.
        Otherwise it calculates lambda-function from connected output and all its previous items recursively

        Args:
            input_id (int): ID of the input

        Returns:
            Callable[[Dict[SensorItem, List[float]]], float]: Lambda-function composed of all previous items
        """
        if input_id in WorkspaceModel.__input_list and input_id in WorkspaceModel.__connection_list:
            output: Output = WorkspaceModel.__output_list[WorkspaceModel.__connection_list[input_id].output]
            if not output.is_function_valid:
                output.function = WorkspaceModel.__output_item_list[output.parent_item_id].\
                    get_rule(output.number_of_output)
                return output.function
        else:
            return lambda data: 0

    @staticmethod
    def calculate_unit(input_id: int) -> str:
        """Calculates unit from input

        Calculates unit from connected output and all its previous items recursively

        Args:
            input_id (int): ID of the input

        Returns:
            str: Unit from output
        """
        if input_id in WorkspaceModel.__input_list and input_id in WorkspaceModel.__connection_list:
            output: Output = WorkspaceModel.__output_list[WorkspaceModel.__connection_list[input_id].output]
            output.unit = WorkspaceModel.__output_item_list[output.parent_item_id].get_unit(output.number_of_output)
            return output.unit
        else:
            return ''

    @staticmethod
    def invalidate_functions(output_id: int) -> NoReturn:
        """Invalidates all lambda-function in the items, which are connected to this output and  all following items

        Args:
            output_id (int): ID of the output
        """
        for connection in WorkspaceModel.__connection_list.values():
            if connection.output == output_id:
                input: Input = WorkspaceModel.__input_list[connection.input]
                if WorkspaceModel.__is_output_item(input.parent_item_id):
                    WorkspaceModel.__output_item_list[input.parent_item_id].invalidate_functions()
