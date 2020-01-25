class Connection:
    def __init__(self, input_id: int, output_id: int):
        self.__input: int = input_id
        self.__output: int = output_id

    @property
    def input(self) -> int:
        return self.__input

    @property
    def output(self) -> int:
        return self.__output
