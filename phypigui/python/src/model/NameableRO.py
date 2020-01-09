class NameableRO:
    def __init__(self):
        self._name: str = None

    def get_name(self) -> str:
        if self._name is None:
            return ""
        return self._name
