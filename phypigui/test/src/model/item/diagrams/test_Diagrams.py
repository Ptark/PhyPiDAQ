import pytest

from phypigui.python.src.model.item.diagrams.BarDiagramItem import BarDiagramItem
from phypigui.python.src.model.item.diagrams.DiagramItem import DiagramItem
from phypigui.python.src.model.item.diagrams.DualDiagramItem import DualDiagramItem
from phypigui.python.src.model.item.diagrams.ThreeDimDiagramItem import ThreeDimDiagramItem
from phypigui.python.src.model.item.diagrams.TimeDiagramItem import TimeDiagramItem
from phypigui.python.src.model.item.diagrams.WriteToFileItem import WriteToFileItem


@pytest.fixture(scope="class", params=[
    BarDiagramItem,
    DualDiagramItem,
    ThreeDimDiagramItem,
    TimeDiagramItem,
    WriteToFileItem
])
def diagrams(request):
    """Returns all operators sequentially"""
    return request.param()


def test_get_name(diagrams):
    assert isinstance(diagrams.get_name(), str)

