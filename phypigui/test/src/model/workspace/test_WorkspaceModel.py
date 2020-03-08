import pytest

from phypigui.python.src.Exceptions import IDNotFound, InputAlreadyConnected
from phypigui.python.src.model.item.operators.AbsoluteOperatorItem import AbsoluteOperatorItem
from phypigui.python.src.model.item.operators.AdditionOperatorItem import AdditionOperatorItem
from phypigui.python.src.model.item.sensors.ForceSensorItem import ForceSensorItem
from phypigui.python.src.model.item.sensors.TemperatureSensorItem import TemperatureSensorItem
from phypigui.python.src.model.workspace.WorkspaceModel import WorkspaceModel


@pytest.fixture
def init_workspace():
    WorkspaceModel._WorkspaceModel__next_id = 0
    WorkspaceModel._WorkspaceModel__input_list = {}
    WorkspaceModel._WorkspaceModel__output_list = {}
    WorkspaceModel._WorkspaceModel__input_item_list = {}
    WorkspaceModel._WorkspaceModel__output_item_list = {}
    WorkspaceModel._WorkspaceModel__connection_list = {}


def test_input(init_workspace):
    assert WorkspaceModel._WorkspaceModel__next_id == 0
    assert WorkspaceModel.add_input(None) == 0
    assert WorkspaceModel._WorkspaceModel__next_id == 1
    assert len(WorkspaceModel._WorkspaceModel__input_list) == 1

    assert WorkspaceModel.check_input_id(0)

    with pytest.raises(IDNotFound):
        WorkspaceModel.check_input_id(10)
    with pytest.raises(IDNotFound):
        WorkspaceModel.check_input_id(-999999999999)

    assert WorkspaceModel.get_connection_to_input(0) == -1
    assert WorkspaceModel.get_connection_to_input(10) == -1
    assert WorkspaceModel.get_connection_to_input(-999999999999) == -1

    WorkspaceModel.delete_input(0)
    assert len(WorkspaceModel._WorkspaceModel__input_list) == 0

    with pytest.raises(IDNotFound):
        WorkspaceModel.delete_input(0)
    with pytest.raises(IDNotFound):
        WorkspaceModel.delete_input(-999999999999)


def test_output(init_workspace):
    assert WorkspaceModel._WorkspaceModel__next_id == 0
    assert WorkspaceModel.add_output(None) == 0
    assert WorkspaceModel._WorkspaceModel__next_id == 1
    assert len(WorkspaceModel._WorkspaceModel__output_list) == 1

    assert WorkspaceModel.check_output_id(0)

    with pytest.raises(IDNotFound):
        WorkspaceModel.check_output_id(10)
    with pytest.raises(IDNotFound):
        WorkspaceModel.check_output_id(-999999999999)

    assert len(WorkspaceModel.get_connections_from_output(0)) == 0
    assert len(WorkspaceModel.get_connections_from_output(10)) == 0
    assert len(WorkspaceModel.get_connections_from_output(-999999999999)) == 0

    WorkspaceModel.delete_output(0)
    assert len(WorkspaceModel._WorkspaceModel__output_list) == 0

    with pytest.raises(IDNotFound):
        WorkspaceModel.delete_output(0)
    with pytest.raises(IDNotFound):
        WorkspaceModel.delete_output(-999999999999)


def test_input_item(init_workspace):
    assert WorkspaceModel._WorkspaceModel__next_id == 0
    assert WorkspaceModel.add_input_item(None) == 0
    assert WorkspaceModel._WorkspaceModel__next_id == 1
    assert len(WorkspaceModel._WorkspaceModel__input_item_list) == 1

    assert WorkspaceModel.check_item_id(0)

    with pytest.raises(IDNotFound):
        WorkspaceModel.check_item_id(10)
    with pytest.raises(IDNotFound):
        WorkspaceModel.check_item_id(-999999999999)

    assert WorkspaceModel._WorkspaceModel__is_input_item(0)
    assert not WorkspaceModel._WorkspaceModel__is_output_item(0)

    assert not WorkspaceModel._WorkspaceModel__is_input_item(10)
    assert not WorkspaceModel._WorkspaceModel__is_input_item(-999999999999)


def test_output_item(init_workspace):
    assert WorkspaceModel._WorkspaceModel__next_id == 0
    assert WorkspaceModel.add_output_item(None) == 0
    assert WorkspaceModel._WorkspaceModel__next_id == 1
    assert len(WorkspaceModel._WorkspaceModel__output_item_list) == 1

    assert WorkspaceModel.check_item_id(0)

    with pytest.raises(IDNotFound):
        WorkspaceModel.check_item_id(10)
    with pytest.raises(IDNotFound):
        WorkspaceModel.check_item_id(999999999999)

    assert WorkspaceModel._WorkspaceModel__is_output_item(0)
    assert not WorkspaceModel._WorkspaceModel__is_input_item(0)

    assert not WorkspaceModel._WorkspaceModel__is_output_item(10)
    assert not WorkspaceModel._WorkspaceModel__is_output_item(-999999999999)


def test_item(init_workspace):
    item = AbsoluteOperatorItem()

    assert item.id == 0
    assert item._inputs[0].id == 1
    assert item._outputs[0].id == 2

    assert len(WorkspaceModel._WorkspaceModel__input_item_list) == 1
    assert len(WorkspaceModel._WorkspaceModel__output_item_list) == 1
    assert len(WorkspaceModel._WorkspaceModel__input_list) == 1
    assert len(WorkspaceModel._WorkspaceModel__output_list) == 1

    assert WorkspaceModel.get_input_item_name(1) == "Absolutoperator"
    with pytest.raises(IDNotFound):
        WorkspaceModel.get_input_item_name(2)
    with pytest.raises(IDNotFound):
        WorkspaceModel.get_input_item_name(-999999999999)

    assert WorkspaceModel.get_output_item_name(2) == "Absolutoperator"
    with pytest.raises(IDNotFound):
        WorkspaceModel.get_output_item_name(1)
    with pytest.raises(IDNotFound):
        WorkspaceModel.get_output_item_name(-999999999999)

    WorkspaceModel.delete_item(0)

    assert len(WorkspaceModel._WorkspaceModel__input_item_list) == 0
    assert len(WorkspaceModel._WorkspaceModel__output_item_list) == 0
    assert len(WorkspaceModel._WorkspaceModel__input_list) == 0
    assert len(WorkspaceModel._WorkspaceModel__output_list) == 0

    with pytest.raises(IDNotFound):
        WorkspaceModel.delete_item(0)
    with pytest.raises(IDNotFound):
        WorkspaceModel.delete_item(1)
    with pytest.raises(IDNotFound):
        WorkspaceModel.delete_item(-999999999999)


def test_connection(init_workspace):
    assert AbsoluteOperatorItem().id == 0
    assert AbsoluteOperatorItem().id == 3

    WorkspaceModel.connect(4, 2)
    assert len(WorkspaceModel._WorkspaceModel__connection_list) == 1

    with pytest.raises(IDNotFound):
        WorkspaceModel.connect(0, 2)
    with pytest.raises(IDNotFound):
        WorkspaceModel.connect(4, 3)
    with pytest.raises(IDNotFound):
        WorkspaceModel.connect(10, -999999999)
    with pytest.raises(InputAlreadyConnected):
        WorkspaceModel.connect(4, 2)

    assert WorkspaceModel.get_connection_to_input(4) == 2
    assert WorkspaceModel.get_connections_from_output(2) == [4]

    assert AbsoluteOperatorItem()._inputs[0].id == 7
    WorkspaceModel.connect(7, 2)
    assert len(WorkspaceModel._WorkspaceModel__connection_list) == 2
    assert WorkspaceModel.get_connections_from_output(2) == [4, 7]

    assert WorkspaceModel.delete_connection(4)
    assert len(WorkspaceModel._WorkspaceModel__connection_list) == 1
    assert WorkspaceModel.get_connections_from_output(2) == [7]

    assert not WorkspaceModel.delete_connection(4)
    with pytest.raises(IDNotFound):
        WorkspaceModel.delete_connection(10)
    with pytest.raises(IDNotFound):
        WorkspaceModel.delete_connection(-999999999999)

    WorkspaceModel.delete_all_output_connections(2)
    assert len(WorkspaceModel._WorkspaceModel__connection_list) == 0
    assert WorkspaceModel.get_connections_from_output(2) == []

    with pytest.raises(IDNotFound):
        WorkspaceModel.delete_all_output_connections(10)
    with pytest.raises(IDNotFound):
        WorkspaceModel.delete_all_output_connections(-999999999999)


def test_calculate_unit(init_workspace):
    temp = TemperatureSensorItem()
    force = ForceSensorItem()
    data = {temp: [10], force: [5]}

    assert temp.id == 0
    assert force.id == 2
    assert AdditionOperatorItem().id == 4
    assert AbsoluteOperatorItem().id == 8
    assert AbsoluteOperatorItem().id == 11

    WorkspaceModel.connect(5, 1)
    WorkspaceModel.connect(6, 3)
    WorkspaceModel.connect(9, 7)

    assert WorkspaceModel.calculate_unit(5) == '°C'
    assert WorkspaceModel.calculate_unit(6) == 'N'
    assert WorkspaceModel.calculate_unit(9) == '(°C+N)'

    assert WorkspaceModel.calculate_unit(12) == ''
    with pytest.raises(IDNotFound):
        WorkspaceModel.calculate_unit(0)
    with pytest.raises(IDNotFound):
        WorkspaceModel.calculate_unit(-999999999999)

    assert WorkspaceModel.calculate_function(5)(data) == 10
    assert WorkspaceModel.calculate_function(6)(data) == 5
    assert WorkspaceModel.calculate_function(9)(data) == 15

    assert WorkspaceModel.calculate_function(12)(data) == 0
    with pytest.raises(IDNotFound):
        WorkspaceModel.calculate_function(0)
    with pytest.raises(IDNotFound):
        WorkspaceModel.calculate_function(-999999999999)
