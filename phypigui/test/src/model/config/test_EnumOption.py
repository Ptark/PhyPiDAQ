from enum import Enum

import pytest

from phypigui.python.src.Exceptions import OutOfRange
from phypigui.python.src.model.config.EnumOption import EnumOption


class __SampleEnum(Enum):
    TEST_1 = 1
    TEST_2 = 2
    TEST_3 = 3
    TEST_4 = 4


class __EmptyEnum(Enum):
    pass


def test_enum_option():
    enum_option = EnumOption("Enum", __SampleEnum)
    assert enum_option.selection == 0
    assert enum_option.samples == __SampleEnum

    with pytest.raises(OutOfRange):
        enum_option.selection = 15
    with pytest.raises(OutOfRange):
        enum_option.selection = -1
    assert enum_option.selection == 0

    enum_option.selection = 1
    assert enum_option.selection == 1

    with pytest.raises(OutOfRange):
        EnumOption("Enum", __SampleEnum, start_selection=10)

    with pytest.raises(OutOfRange):
        EnumOption("Enum", __EmptyEnum)
