import time
from threading import Thread

import pytest

from phypigui.test.src.test_helpers import main_window
from phypigui.python.src.model.item.diagrams.TimeDiagramItem import TimeDiagramItem
from phypigui.python.src.model.item.operators.AbsoluteOperatorItem import AbsoluteOperatorItem
from phypigui.python.src.model.item.sensors.TemperatureSensorItem import TemperatureSensorItem
from phypigui.python.src.model.manager.ManagerModel import ManagerModel


class ManagerTestThread(Thread):
    def run(self):
        ManagerModel.start()


@pytest.fixture
def init_manager(main_window):
    ManagerModel._ManagerModel__sensors = []
    ManagerModel._ManagerModel__operators = []
    ManagerModel._ManagerModel__diagrams = []
    ManagerModel._ManagerModel__sensor_data = {}
    ManagerModel._ManagerModel__running = False
    ManagerModel._ManagerModel__selected_item = None


def test_running(init_manager):
    TimeDiagramItem()
    ManagerModel.set_selected_item(TemperatureSensorItem())

    thread = ManagerTestThread()
    thread.start()
    time.sleep(0.1)
    assert ManagerModel.is_running()

    ManagerModel.stop()
    thread.join()
    assert not ManagerModel.is_running()


def test_add_delete(init_manager):
    sensor = TemperatureSensorItem()
    operator = AbsoluteOperatorItem()
    diagram = TimeDiagramItem()

    assert sensor in ManagerModel._ManagerModel__sensors
    assert sensor in ManagerModel._ManagerModel__sensors
    assert sensor in ManagerModel._ManagerModel__sensors

    ManagerModel.add_sensor(sensor)
    assert len(ManagerModel._ManagerModel__sensors) == 1
    ManagerModel.add_operator(operator)
    assert len(ManagerModel._ManagerModel__operators) == 1
    ManagerModel.add_diagram(diagram)
    assert len(ManagerModel._ManagerModel__diagrams) == 1

    ManagerModel.delete_sensor(sensor)
    assert sensor not in ManagerModel._ManagerModel__sensors
    ManagerModel.delete_operator(operator)
    assert operator not in ManagerModel._ManagerModel__operators
    ManagerModel.delete_diagram(diagram)
    assert diagram not in ManagerModel._ManagerModel__diagrams
