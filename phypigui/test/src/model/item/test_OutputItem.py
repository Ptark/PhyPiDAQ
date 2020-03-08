import copy
from typing import Callable, Dict, List

from phypigui.python.src.model.config.BoolOption import BoolOption
from phypigui.python.src.model.config.ConfigModel import ConfigModel
from phypigui.python.src.model.item.Input import Input
from phypigui.python.src.model.item.OutputItem import OutputItem
from phypigui.python.src.model.workspace.WorkspaceModel import WorkspaceModel


class OItem(OutputItem):
    def __init__(self, name: str, description: str, config: ConfigModel, outputs: int):
        super().__init__(name, description, config, outputs)

    def get_name(self) -> str:
        return ""

    def get_rule(self, output_number: int = 0) -> Callable[[Dict['SensorItem', List[float]]], float]:
        pass

    def get_unit(self, output_number: int = 0) -> str:
        pass


def test_set_config():
    config = ConfigModel()
    config.add_bool_option(BoolOption(""))
    item = OItem("", "", copy.deepcopy(config), 1)
    config.set_bool_option(0, True)
    item.set_config(config)
    assert item.config.bool_options[0].enabled is True


def test_connect_output():
    input = Input(12, 0)
    input_id = WorkspaceModel.add_input(input)
    item = OItem("", "", None, 3)
    item.connect_output(2, input_id)


def test_get_output_id():
    item = OItem("", "", None, 3)
    assert item.get_output_id(3) == -1
    assert item.get_output_id(-1) == -1