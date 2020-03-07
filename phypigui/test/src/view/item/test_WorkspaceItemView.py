import pytest

from phypigui.test.src.test_helpers import main_window
from phypigui.python.src.model.manager.ManagerModel import ManagerModel
from phypigui.python.src.view.Workspace.WorkspaceView import WorkspaceView
from phypigui.python.src.view.Item.ItemEnum import SensorEnum, OperatorEnum, DiagramEnum
from phypigui.python.src.view.InfoBar.InfoBarView import InfoBarView


@pytest.fixture(scope="class", params=list(SensorEnum))
def sensors(request):
    return request.param


@pytest.fixture(scope="class", params=list(OperatorEnum))
def operators(request):
    return request.param


@pytest.fixture(scope="class", params=list(DiagramEnum))
def diagrams(request):
    return request.param


def test_sensor(qtbot, main_window, sensors):
    item = _test_item_creation(sensors)
    assert item._model in ManagerModel._ManagerModel__sensors

    _test_item_selection(item)
    assert ManagerModel._ManagerModel__selected_item is item._model

    _test_item_deletion(item)
    assert item._model not in ManagerModel._ManagerModel__sensors
    assert ManagerModel._ManagerModel__selected_item is not item._model


def test_operator(qtbot, main_window, operators):
    item = _test_item_creation(operators)
    assert item._model in ManagerModel._ManagerModel__operators

    _test_item_selection(item)
    assert ManagerModel._ManagerModel__selected_item is item._model

    _test_item_deletion(item)
    assert item._model not in ManagerModel._ManagerModel__operators
    assert ManagerModel._ManagerModel__selected_item is not item._model


def test_diagram(qtbot, main_window, diagrams):
    item = _test_item_creation(diagrams)
    if diagrams.diagram is not None:
        assert isinstance(item._diagram, diagrams.diagram)
    assert item._model in ManagerModel._ManagerModel__diagrams

    _test_item_selection(item)

    _test_item_deletion(item)


def _test_item_creation(enum):
    item = enum.create_workspace_item(WorkspaceView.widget)

    assert isinstance(item._model, enum.model)
    assert item in item._model._Model__views
    assert len(WorkspaceView.items) == 1

    return item

def _test_item_selection(item):
    assert item is not None
    assert not item.selected
    assert InfoBarView._InfoBarView__infobar._InfoBarView__info_widget is not item._WorkspaceItemView__info_widget

    item._on_click()
    assert item.selected
    assert InfoBarView._InfoBarView__infobar._InfoBarView__info_widget is item._WorkspaceItemView__info_widget

    item._on_click()
    assert not item.selected
    assert InfoBarView._InfoBarView__infobar._InfoBarView__info_widget is not item._WorkspaceItemView__info_widget

    item._on_click()
    assert item.selected


def _test_item_deletion(item):
    assert item is not None
    item.delete()

    assert len(WorkspaceView.items) == 0
    assert InfoBarView._InfoBarView__infobar._InfoBarView__info_widget is not item._WorkspaceItemView__info_widget
