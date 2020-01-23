class Identifiable:
    def __init__(self, id: int):
        self.__id: int = id

    @property
    def id(self) -> int:
        return self.__id