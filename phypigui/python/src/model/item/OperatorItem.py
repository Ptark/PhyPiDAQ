from abc import ABC
from typing import List, Callable, Dict

from ..item.InputItem import InputItem
from ..item.OutputItem import OutputItem
from ..item.SensorItem import SensorItem
from ..config.NumOption import NumOption
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
        OutputItem.__init__(self, name, description, config, outputs)


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
        return WorkspaceModel.calculate_unit(self._inputs[0].id)


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


class NegativeOperatorItem(OperatorItem):
    """This class models an operator, which makes a data-stream only negative

    A NegativeOperatorItem has one input and one output.
    """

    def __init__(self):
        """Initialising a NegativeOperatorItem object"""
        name: str = "Negativer Betragsoperator"
        description: str = "Dieser Operator negiert alle einkommenden Werte"
        config: ConfigModel = ConfigModel()

        super().__init__(name, description, config, 1, 1)

    def get_rule(self, output_number: int = 0):
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[0].id)(data)
        return lambda data: (-1 * abs(first_function(data)))

    def get_unit(self, output_number: int = 0) -> str:
        return WorkspaceModel.calculate_unit(self._inputs[0].id)


class PowerOperatorItem(OperatorItem):
    """This class models an operator, which exponentiates a data-stream with an adjustable number

    A PowerOperatorItem has one input and one output.
    """

    def __init__(self):
        """Initialising a PowerOperatorItem object"""
        name: str = "Exponentialsoperator"
        description: str = "Dieser Operator potenziert einen Datenstrom mit einer einstellbaren Zahl"
        config: ConfigModel = ConfigModel()
        config.add_num_option(NumOption("Exponent", "Mit dieser Zahl wird der\nDaten-Strom potenziert", 0, -20, 20, 0))

        super().__init__(name, description, config, 1, 1)

    def get_rule(self, output_number: int = 0):
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: + \
            WorkspaceModel.calculate_function(self._inputs[0].id)(data)
        return lambda data: pow(first_function(data), self.config.num_options[0].number)

    def get_unit(self, output_number: int = 0) -> str:
        return "(" + WorkspaceModel.calculate_unit(self._inputs[0].id) + "^" + str(self.config.num_options[0].number) \
               + ")"


class RootOperatorItem(OperatorItem):
    """This class models an operator, which exponentiates a data-stream with 1 divided through an adjustable number

    A OperatorItem has one input and one output.
    """

    def __init__(self):
        """Initialising a RootOperatorItem object"""
        name: str = "Wurzeloperator"
        description: str = "Dieser Operator potenziert einen Datenstrom mit 1 geteilt durch eine einstellbare Zahl"
        config: ConfigModel = ConfigModel()
        config.add_num_option(NumOption("n-te Wurzel", "Hier kann man die Zahl n\neinstellen", 0, -20, 20, 0))

        super().__init__(name, description, config, 1, 1)

    def get_rule(self, output_number: int = 0):
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: + \
            WorkspaceModel.calculate_function(self._inputs[0].id)(data)
        return lambda data: pow(first_function(data), 1 / self.config.num_options[0].number)

    def get_unit(self, output_number: int = 0) -> str:
        return "(" + WorkspaceModel.calculate_unit(self._inputs[0].id) + "^ 1/" \
                + str(self.config.num_options[0].number) + ")"


class CloneItem(OperatorItem):
    """This class models an operator, which doubles a data-stream

    A CloneItem has one input and two output.
    """

    def __init__(self):
        """Initialising a DoubleItem object"""
        name: str = "Klonoperator"
        description: str = "Dieser Operator vordoppelt einen Datenstrom"
        config: ConfigModel = ConfigModel()

        super().__init__(name, description, config, 1, 2)

    def get_rule(self, output_number: int = 0):
        first_function: Callable[[Dict[SensorItem, List[float]]], float] = lambda data: +\
            WorkspaceModel.calculate_function(self._inputs[0].id)(data)
        return lambda data: first_function(data)

    def get_unit(self, output_number: int = 0) -> str:
        return WorkspaceModel.calculate_unit(self._inputs[0].id)
