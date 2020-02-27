import pytest

from phypigui.python.src.model.item.operators.AbsoluteOperatorItem import AbsoluteOperatorItem
from phypigui.python.src.model.item.operators.AdditionOperatorItem import AdditionOperatorItem
from phypigui.python.src.model.item.operators.CloneItem import CloneItem
from phypigui.python.src.model.item.operators.DivisionOperatorItem import DivisionOperatorItem
from phypigui.python.src.model.item.operators.MultiplicationOperatorItem import MultiplicationOperatorItem
from phypigui.python.src.model.item.operators.NegativeOperatorItem import NegativeOperatorItem
from phypigui.python.src.model.item.operators.PowerOperatorItem import PowerOperatorItem
from phypigui.python.src.model.item.operators.RootOperatorItem import RootOperatorItem
from phypigui.python.src.model.item.operators.SubtractionOperatorItem import SubtractionOperatorItem


@pytest.fixture(scope="class", params=[
    AbsoluteOperatorItem,
    AdditionOperatorItem,
    CloneItem,
    DivisionOperatorItem,
    MultiplicationOperatorItem,
    NegativeOperatorItem,
    PowerOperatorItem,
    RootOperatorItem,
    SubtractionOperatorItem
])
def operators(request):
    """Returns all operators sequentially"""
    return request.param()


def test_get_rule(operators):
    assert operators.get_rule() is not None


def test_get_unit(operators):
    assert isinstance(operators.get_unit(), str)


def test_get_name(operators):
    assert isinstance(operators.get_name(), str)

