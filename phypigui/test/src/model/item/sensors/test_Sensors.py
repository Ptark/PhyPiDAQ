import pytest

from phypigui.python.src.model.item.sensors.AccelerationSensorItem import AccelerationSensorItem
from phypigui.python.src.model.item.sensors.ConstantItems import ConstantItem, NatureConstantItem
from phypigui.python.src.model.item.sensors.CurrentSensorItem import CurrentSensorItem
from phypigui.python.src.model.item.sensors.DistanceSensorItem import DistanceSensorItem
from phypigui.python.src.model.item.sensors.ForceSensorItem import ForceSensorItem
from phypigui.python.src.model.item.sensors.ProxySensorItem import ProxySensorItem
from phypigui.python.src.model.item.sensors.RGBSensorItem import RGBSensorItem
from phypigui.python.src.model.item.sensors.TemperatureSensorItem import TemperatureSensorItem
from phypigui.python.src.model.item.sensors.VoltageSensorItem import VoltageSensorItem


# fixture method sets up for the tests
@pytest.fixture(scope="class", params=[
    AccelerationSensorItem,
    ConstantItem,
    NatureConstantItem,
    CurrentSensorItem,
    DistanceSensorItem,
    ForceSensorItem,
    ProxySensorItem,
    RGBSensorItem,
    TemperatureSensorItem,
    VoltageSensorItem
])
def sensors(request):
    """Returns all sensors sequentially"""
    return request.param()


def test_get_unit(sensors):
    assert isinstance(sensors.get_unit(), str)


def test_get_name(sensors):
    assert isinstance(sensors.get_name(), str)


def test_del(sensors):
    sensors.__del__()


