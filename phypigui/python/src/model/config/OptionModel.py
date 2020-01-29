from ..NameableRO import NameableRO
from ..Describable import Describable


class OptionModel(NameableRO, Describable):
    def __init__(self, name: str, description: str = ''):
        NameableRO.__init__(self, name)
        if description == '':
            Describable.__init__(self, name)
        else:
            Describable.__init__(self, description)
