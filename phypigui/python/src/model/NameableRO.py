class NameableRO:
    """This class is a super class for all classes, which are nameable

    Caution, the name can never be changed.
    """

    def __init__(self, name: str = ""):
        """Initialising an NameableRO object"""
        self._name: str = name

    @property
    def name(self) -> str:
        """Name of this object"""
        return self._name
