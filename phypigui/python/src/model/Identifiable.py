class Identifiable:
    def __init__(self, id: int):
        self._id: int = id

    @property
    def id(self) -> int:
        return self._id