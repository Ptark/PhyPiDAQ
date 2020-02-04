from abc import ABC

from ..NameableRO import NameableRO
from ..Describable import Describable


class OptionModel(NameableRO, Describable, ABC):
    """This class contains the basic structure for all item-options

    Every option for Drag and Drop items extends from this class
    """

    def __init__(self, name: str, description: str = ''):
        """Initialising an OptionModel object

        Args:
            name (str): Name of this option
            description (str): Description of this option
                If description is empty this constructor creates an description based on argument name
        """
        NameableRO.__init__(self, name)
        if description == '':
            Describable.__init__(self, name + ' einstellen')
        else:
            Describable.__init__(self, description)
