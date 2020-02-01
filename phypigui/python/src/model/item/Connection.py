class Connection:
    """This class represents a connection between a OutputItem and a InputItem"""

    def __init__(self, input_id: int, output_id: int):
        """Initialising a Connection object

        Args:
            input_id (int): ID of the InputItem, which is part of the connection
            output_id (int): ID of the OutputItem, which is part of the connection
        """
        self.__input: int = input_id
        self.__output: int = output_id

    @property
    def input(self) -> int:
        """ID of the InputItem, which is part of the connection"""
        return self.__input

    @property
    def output(self) -> int:
        """ID of the OutputItem, which is part of the connection"""
        return self.__output
