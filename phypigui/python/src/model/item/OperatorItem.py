from abc import ABC, abstractmethod
from ..item import InputItem,Output,Input, OutputItem
from ..config import ConfigModel
from ..workspace import WorkspaceModel


class OperatorItem(ABC, InputItem, OutputItem):

    @abstractmethod
    def get_rule(self, output_number: int):
        first_function = lambda data: WorkspaceModel.WorkspaceModel.calculate_function(self._inputs[0].get_id())(data)
        second_function = lambda data: WorkspaceModel.WorkspaceModel.calculate_function(self._inputs[1].get_id())(data)


    def get_unit(self, output_number: int) -> str:
        return "(" + WorkspaceModel.WorkspaceModel.calculate_unit(self._inputs[0].get_id()) + ") + (" /\
                WorkspaceModel.WorkspaceModel.calculate_unit(self._inputs[1].get_id()) + ")"

    def get_number_of_outputs(self) -> int:
        return 1

    def get_number_of_inputs(self) -> int:
        return 2


class DivisionOperatorItem(OperatorItem):
    def __init__(self):
        self._name: str = "Divisionsoperator"
        self._description: str = "Dieser Operator dividiert zwei Werte"
        self._config: ConfigModel = ConfigModel.ConfigModel()
        self._outputs: [Output] = [Output()]
        self._inputs: [Input] = [Input()] * 2

    def get_rule(self, output_number: int):
        #TODO
         pass


class AbsoluteOperatorItem(OperatorItem):
    def __int__(self):
        self._name: str = "Absoluteoperator"
        self._description: str = "Dieser Operator berechnet den Absolutbetrag"
        self._config: ConfigModel = ConfigModel.ConfigModel()
        self._outputs: [Output] = [Output.Output()]
        self._inputs: [Input] = [Input.Input()]
    
    def get_number_of_inputs(self) -> int:
        return 1

    def get_rule(self, output_number: int):
        #TODO
        pass

    def get_unit(self, output_number: int) -> str:
        return "(" + WorkspaceModel.WorkspaceModel.calculate_unit(self._inputs[0].get_id()) + ")"


class MultiplicationOperatorItem(OperatorItem):
    def __int__(self):
        self._name: str = "Multiplikationsoperator"
        self._description. str = "Dieser Operator multipliziert zwei Werte"
        self._config: ConfigModel = ConfigModel.ConfigModel()
        self._outputs: [Output] = [Output()]
        self._inputs: [Input] = [Input()] * 2

    def get_rule(self, output_number: int):
        #TODO
        pass

    
