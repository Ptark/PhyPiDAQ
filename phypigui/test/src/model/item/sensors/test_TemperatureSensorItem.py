import pytest

from phypigui.python.src.model.item.sensors.TemperatureSensorItem import TemperatureSensorItem


@pytest.fixture
def temperature_sensor():
    """Returns a temperature sensor"""
    return TemperatureSensorItem()


def test_get_unit(temperature_sensor):
    assert isinstance(temperature_sensor.get_unit(), str)


def test_get_name(temperature_sensor):
    assert isinstance(temperature_sensor.get_name(), str)

