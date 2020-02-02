from abc import ABC
from typing import List, Callable, Dict

from ..item.Output import Output
from ..item.InputItem import InputItem
from ..item.OutputItem import OutputItem
from ..item.SensorItem import SensorItem
from ..config.ConfigModel import ConfigModel
from ..workspace.WorkspaceModel import WorkspaceModel


class OperatorItem(InputItem, OutputItem, ABC):
    """This class is a superclass for all kind of OperatorItems"""

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

        self._outputs: List[Output] = []
        for i in range(1, outputs):
            self._outputs.append(Output(self._id, i))


class DivisionOperatorItem(OperatorItem):
    """This class models a operator, which divides the first by the second data-stream

    A DivisionOperatorItem has two inputs and one output.
    """

    def __init__(self):
        """Initialising a DivisionOperatorItem object"""
        name: str = "Divisionsoperator"
        description: str = "Dieser Operator dividiert zwei Werte"
        config: ConfigModel = ConfigModel()

        super().__init__(name, description, config, 2, 1)

    def get_rule(self, output_number: int = 0) -> Callable[[Dict[SensorItem, List[float]]], float]:
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[0].id)(data)
        second_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[1].id)(data)
        return lambda data: first_function(data) / second_function(data)

    def get_unit(self, output_number: int = 0) -> str:
        return "(" + WorkspaceModel.calculate_unit(self._inputs[0].id) + ") / (" +\
            WorkspaceModel.calculate_unit(self._inputs[1].id) + ")"


class AbsoluteOperatorItem(OperatorItem):
    """This class models an operator, which makes a data-stream only positive

    A AbsoluteOperatorItem has one inputs and one output.
    """

    def __init__(self):
        """Initialising a AbsoluteOperatorItem object"""
        name: str = "Absolutoperator"
        description: str = "Dieser Operator berechnet den Absolutbetrag"
        config: ConfigModel = ConfigModel()

        super().__init__(name, description, config, 1, 1)

    def get_rule(self, output_number: int = 0):
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[0].id)(data)
        return lambda data: abs(first_function(data))

    def get_unit(self, output_number: int = 0) -> str:
        return "(" + WorkspaceModel.calculate_unit(self._inputs[0].id) + ")"


class MultiplicationOperatorItem(OperatorItem):
    """This class models an operator, which multiply two data-streams

    A MultiplicationOperatorItem has two inputs and one output.
    """

    def __init__(self):
        """Initialising a MultiplicationOperatorItem object"""
        name: str = "Multiplikationsoperator"
        description: str = "Dieser Operator multipliziert zwei Werte"
        config: ConfigModel = ConfigModel()

        super().__init__(name, description, config, 2, 1)

    def get_rule(self, output_number: int = 0):
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[0].id)(data)
        second_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[1].id)(data)
        return lambda data: first_function(data) * second_function(data)

    def get_unit(self, output_number: int = 0) -> str:
        return "(" + WorkspaceModel.calculate_unit(self._inputs[0].id) + ") * (" +\
            WorkspaceModel.calculate_unit(self._inputs[1].id) + ")"


class AdditionOperatorItem(OperatorItem):
    """This class models an operator, which adds two data-streams

    A AdditionOperatorItem has two inputs and one output.
    """

    def __init__(self):
        """Initialising a AdditionOperatorItem object"""
        name: str = "Additionsoperator"
        description: str = "Dieser Operator addiert zwei Werte"
        config: ConfigModel = ConfigModel()
        super().__init__(name, description, config, 2, 1)

    def get_rule(self, output_number: int = 0):
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[0].id)(data)
        second_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[1].id)(data)
        return lambda data: first_function(data) + second_function(data)

    def get_unit(self, output_number: int = 0) -> str:
        return "(" + WorkspaceModel.calculate_unit(self._inputs[0].id) + ") + (" +\
            WorkspaceModel.calculate_unit(self._inputs[1].id) + ")"


class SubtractionOperatorItem(OperatorItem):
    """This class models an operator, which subtract the second of the first data-stream

    A SubtractionOperatorItem has two inputs and one output.
    """

    def __init__(self):
        """Initialising a SubtractionOperatorItem object"""
        name: str = "Subtraktionsoperator"
        description: str = "Dieser Operator subtrahiert zwei Werte"
        config: ConfigModel = ConfigModel()
        super().__init__(name, description, config, 2, 1)

    def get_rule(self, output_number: int = 0):
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[0].id)(data)
        second_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[1].id)(data)
        return lambda data: first_function(data) - second_function(data)

    def get_unit(self, output_number: int = 0) -> str:
        return "(" + WorkspaceModel.calculate_unit(self._inputs[0].id) + ") - (" +\
            WorkspaceModel.calculate_unit(self._inputs[1].id) + ")"
