class NameableRO:
    def __init__(self, name: str = ""):
        self._name: str = name

    def get_name(self) -> str:
        return self._name
