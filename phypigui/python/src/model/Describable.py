class Describable:
    """This class is a super class for all classes, which has a description"""

    def __init__(self, description: str):
        """Initialising an Describable object"""
        self._description = description

    @property
    def description(self) -> str:
        """Description of this object"""
        return self._description
