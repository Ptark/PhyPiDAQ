from typing import Callable, Dict, List

from phypigui.python.src.model.config.ConfigModel import ConfigModel
from phypigui.python.src.model.item.InputItem import InputItem
from phypigui.python.src.model.item.OutputItem import OutputItem


class IItem(InputItem):
    def __init__(self, name: str, des: str, config: ConfigModel, inputs: int):
        super().__init__(name, des, config, inputs)

    def get_name(self) -> str:
        return ""


class OItem(OutputItem):
    def __init__(self, name: str, des: str, config: ConfigModel, outputs: int):
        super().__init__(name, des, config, outputs)

    def get_name(self) -> str:
        return ""

    def get_unit(self):
        return ""

    def get_rule(self, output_number: int = 0) -> Callable[[Dict['SensorItem', List[float]]], float]:
        return lambda data: 0


def test_get_count_of_inputs():
    input_item = IItem("", "", None, 5)
    assert input_item.get_count_of_inputs() == 5


def test_connect_input():
    input_item = IItem("", "", None, 1)
    output_item = OItem("", "", None, 1)
    input_item.connect_input(0, output_item.get_output_id(0))


def test_get_input_id():
    input_item = IItem("", "", None, 3)
    assert input_item.get_input_id(1) == input_item.get_input_ids()[1]
    assert input_item.get_input_id(0) == input_item.get_input_ids()[0]
    assert input_item.get_input_id(-3) == -1
    assert input_item.get_input_id(3) == -1
