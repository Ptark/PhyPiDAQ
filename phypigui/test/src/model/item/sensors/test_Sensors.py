import pytest

from pathlib import Path
from phypigui.python.src.Exceptions import PathDoesntExist
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
    RGBSensorItem,
    TemperatureSensorItem,
    VoltageSensorItem
])
def sensors(request):
    """Returns all sensors sequentially"""
    return request.param()


@pytest.fixture
def proxy_sensor():
    return ProxySensorItem()


def test_get_unit(sensors):
    assert isinstance(sensors.get_unit(), str)


def test_get_name(sensors):
    assert isinstance(sensors.get_name(), str)


def test_del(sensors):
    sensors.__del__()


def test_proxy_get_unit(proxy_sensor):
    with pytest.raises(PathDoesntExist):
        proxy_sensor.get_unit()


def test_proxy_get_name(proxy_sensor):
    assert isinstance(proxy_sensor.get_name(), str)


def test_proxy_read(proxy_sensor):
    proxy_sensor.data = [0, 1]
    proxy_sensor.read()
    proxy_sensor.data = [0]
    proxy_sensor.read()


def test_proxy_close(proxy_sensor):
    proxy_sensor.close()






