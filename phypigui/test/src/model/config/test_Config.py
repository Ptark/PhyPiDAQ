import pytest

from enum import Enum
from pathlib import Path

from phypigui.python.src.SystemInfo import SystemInfo
from phypigui.python.src.model.config.BoolOption import BoolOption
from phypigui.python.src.model.config.ConfigModel import ConfigModel
from phypigui.python.src.model.config.EnumOption import EnumOption
from phypigui.python.src.model.config.FileOption import FileOption
from phypigui.python.src.model.config.NumOption import NumOption


class __SampleEnum(Enum):
    TEST_1 = 1
    TEST_2 = 2


@pytest.fixture
def config():
    return ConfigModel()


def test_config_empty(config):
    bool_option = BoolOption("Bool")
    assert config.empty
    config.add_bool_option(bool_option)
    assert not config.empty


def test_bool_options(config):
    bool_option = BoolOption("Bool", start_value=True)

    assert config.add_bool_option(bool_option) == 0
    assert len(config.bool_options) == 1
    assert config.bool_options is not config._ConfigModel__bool_options

    config.set_bool_option(0, False)
    assert not config.bool_options[0].enabled

    with pytest.raises(IndexError):
        config.set_bool_option(10, True)


def test_num_options(config):
    num_option = NumOption("Num", num=1)

    assert config.add_num_option(num_option) == 0
    assert len(config.num_options) == 1
    assert config.num_options is not config._ConfigModel__num_options

    config.set_num_option(0, 13)
    assert config.num_options[0].number == 13

    with pytest.raises(IndexError):
        config.set_num_option(-1, 1)


def test_enum_options(config):
    enum_option = EnumOption("Enum", __SampleEnum, start_selection=0)

    assert config.add_enum_option(enum_option) == 0
    assert len(config.enum_options) == 1
    assert config.enum_options is not config._ConfigModel__enum_options

    config.set_enum_option(0, 1)
    assert config.enum_options[0].selection == 1

    with pytest.raises(IndexError):
        config.set_enum_option(2, 0)


def test_file_options(config):
    file_option = FileOption("File", Path(SystemInfo.RESOURCES + r"data\test_force.ppg"))

    assert config.add_file_option(file_option) == 0
    assert len(config.file_options) == 1
    assert config.file_options is not config._ConfigModel__file_options

    path = Path(SystemInfo.RESOURCES + r"data\test_temp_celsius.ppg")
    config.set_file_option(0, path)
    assert config.file_options[0].path == path

    with pytest.raises(IndexError):
        config.set_file_option(999999999999, Path())
