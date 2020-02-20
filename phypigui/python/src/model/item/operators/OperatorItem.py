from abc import ABC

from ..InputItem import InputItem
from ..OutputItem import OutputItem
from ...config.ConfigModel import ConfigModel


class OperatorItem(InputItem, OutputItem, ABC):
    """This class is a superclass for all kind of operators"""

    def __init__(self, name: str, description: str, config: ConfigModel, inputs: int, outputs: int):
        """Initialising a OperatorItem object

        Args:
            name (str): Name of this OperatorItem
            description (str): Description of this OperatorItem
            config (ConfigModel): A configuration of adjustable options for this OperatorItem
            inputs (int): Count of outputs for this OperatorItem
            outputs (int): Count of outputs for this OperatorItem
        """
        InputItem.__init__(self, name, description, config, inputs)
        OutputItem.__init__(self, name, description, config, outputs)
