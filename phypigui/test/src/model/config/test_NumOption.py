import sys

import pytest

from phypigui.python.src.Exceptions import NumberTooLarge, NumberTooSmall
from phypigui.python.src.model.config.NumOption import NumOption


def test_num_option():
    num_option = NumOption("Num")
    assert num_option.number == 0
    assert num_option.min == -sys.float_info.max
    assert num_option.max == sys.float_info.max
    assert num_option.decimals == 20
    num_option.number = -13.001
    assert num_option.number == -13.001

    num_option = NumOption("Num", "", 2.001, -10, 13.254, 8)
    assert num_option.number == 2.001
    assert num_option.min == -10
    assert num_option.max == 13.254
    assert num_option.decimals == 8

    num_option.number = -10

    with pytest.raises(NumberTooSmall):
        num_option.number = -20

    with pytest.raises(NumberTooLarge):
        num_option.number = 15

    assert num_option.number == -10

    num_option.number = 0.123456789123456789
    assert num_option.number == 0.12345679
