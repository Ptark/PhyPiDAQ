class Identifiable:
    """This class is a super class for all classes, which are using an id-system"""

    def __init__(self, id: int):
        """Initialising an Identifiable object"""
        self._id: int = id

    @property
    def id(self) -> int:
        """ID, an unique identification number"""
        return self._id
