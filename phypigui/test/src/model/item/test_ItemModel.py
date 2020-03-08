import enum
import copy

from pathlib import Path

import pytest

from phypigui.python.src.model.config.BoolOption import BoolOption
from phypigui.python.src.model.config.ConfigModel import ConfigModel
from phypigui.python.src.model.config.EnumOption import EnumOption
from phypigui.python.src.model.config.FileOption import FileOption
from phypigui.python.src.model.config.NumOption import NumOption
from phypigui.python.src.model.item.ItemModel import ItemModel


class IMItem(ItemModel):
    def __init__(self, name: str, description: str, config: ConfigModel, item_id: int):
        super().__init__(name, description, config, item_id)

    def get_name(self):
        return ""


class TestEnum(enum.Enum):
    ZERO = 0
    ONE = 1


def create_item(config: ConfigModel, item_id: int) -> IMItem:
    return IMItem("", "", copy.deepcopy(config), item_id)


def test_set_config():
    config = ConfigModel()
    config.add_bool_option(BoolOption("", "", False))
    config.add_enum_option(EnumOption("", TestEnum, "", 0))
    config.add_file_option(FileOption(""))
    config.add_num_option(NumOption("", "", 0))
    item = create_item(config, 1)

    config.set_bool_option(0, True)
    config.set_enum_option(0, 1)
    config.set_num_option(0, 5.5)
    config.set_file_option(0, Path("/PhyPiDAQ/phypigui/test/resources/test_data/test_force.ppg"))
    item.set_config(config)

    assert item.config.bool_options[0].enabled is True
    assert item.config.enum_options[0].selection == 1
    assert item.config.num_options[0].number == 5.5
    assert item.config.file_options[0].path == Path("/PhyPiDAQ/phypigui/test/resources/test_data/test_force.ppg")


def test_set_bool_option():
    config = ConfigModel()
    for i in range(10):
        config.add_bool_option(BoolOption(""))
    item = create_item(config, 1)

    with pytest.raises(IndexError):
        item.set_bool_option(-1, True)

    with pytest.raises(IndexError):
        item.set_bool_option(10, True)

    item.set_bool_option(3, True)
    assert item.config.bool_options[3].enabled is True


def test_set_num_option():
    config = ConfigModel()
    for i in range(10):
        config.add_num_option(NumOption(""))
    item = create_item(config, 1)

    with pytest.raises(IndexError):
        item.set_num_option(-1, 4)

    with pytest.raises(IndexError):
        item.set_num_option(10, 4)

    item.set_num_option(0, 1234)
    assert item.config.num_options[0].number == 1234


def test_set_enum_option():
    config = ConfigModel()
    for i in range(10):
        config.add_enum_option(EnumOption("", TestEnum))
    item = create_item(config, 1)

    with pytest.raises(IndexError):
        item.set_num_option(-1, 1)

    with pytest.raises(IndexError):
        item.set_enum_option(10, 1)

    item.set_enum_option(9, 1)
    assert item.config.enum_options[9].selection == 1


def test_set_file_option():
    config = ConfigModel()
    for i in range(10):
        config.add_file_option(FileOption(""))
    item = create_item(config, 1)

    with pytest.raises(IndexError):
        item.set_file_option(-1, Path(""))

    with pytest.raises(IndexError):
        item.set_file_option(10, Path(""))

    item.set_file_option(4, Path("/PhyPiDAQ/phypigui/test/resources/test_data/test_force.ppg"))
    assert item.config.file_options[4].path == Path("/PhyPiDAQ/phypigui/test/resources/test_data/test_force.ppg")
