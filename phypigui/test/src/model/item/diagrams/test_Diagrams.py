import os
import time

import pytest

from phypigui.python.src.model.item.diagrams.BarDiagramItem import BarDiagramItem
from phypigui.python.src.model.item.diagrams.DiagramItem import DiagramItem
from phypigui.python.src.model.item.diagrams.DualDiagramItem import DualDiagramItem
from phypigui.python.src.model.item.diagrams.ThreeDimDiagramItem import ThreeDimDiagramItem
from phypigui.python.src.model.item.diagrams.TimeDiagramItem import TimeDiagramItem
from phypigui.python.src.model.item.diagrams.WriteToFileItem import WriteToFileItem
from phypigui.python.src.view import List


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


@pytest.fixture
def write_to_file_item():
    """Returns a WriteToFileItem"""
    return WriteToFileItem()


def test_get_name(diagrams):
    assert isinstance(diagrams.get_name(), str)


def test_calculate_functions(diagrams):
    diagrams.calculate_functions()


def test_writer_stop(write_to_file_item):
    writer = write_to_file_item
    sep = os.path.sep
    path = sep + "phypigui" + sep + "test" + sep + "resources" + sep + "test_output" + sep
    writer.path = os.getcwd() + path + str(time.time())
    writer.stop()

