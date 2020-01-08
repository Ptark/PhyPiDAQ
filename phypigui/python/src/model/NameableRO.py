class NameableRO:
    _name = str

    def __init__(self):
        _name = None

    def get_name(self) -> str:
        if _name is None:
            return ""
        return self._name
