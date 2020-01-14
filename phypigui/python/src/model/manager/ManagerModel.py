from typing import Dict, List, NoReturn
from ..item.SensorItem import SensorItem
from ..item.DiagramItem import DiagramItem
from ..item.OutputItem import OutputItem
from ..Model import Model

import copy


class ManagerModel(Model):
    __sensors: List[SensorItem] = []
    __diagrams: List[DiagramItem] = []
    __sensor_data: Dict[SensorItem, List[float]] = {}
    __running: bool = False
    __selected_item: OutputItem = None

    @staticmethod
    def __init_functions() -> NoReturn:
        for diagram in ManagerModel.__diagrams:
            diagram.calculate_functions()

    @staticmethod
    def __read_data() -> NoReturn:
        for sensor in ManagerModel.__sensor_data:
            ManagerModel.__sensor_data[sensor] = sensor.read()

    @staticmethod
    def is_running() -> bool:
        return ManagerModel.__running

    @staticmethod
    def get_selected_item() -> OutputItem:
        return copy.deepcopy(ManagerModel.__selected_item)

    @staticmethod
    def set_selected_item(selected: OutputItem) -> NoReturn:
        ManagerModel.__selected_item = selected

    @staticmethod
    def add_sensor(sensor: SensorItem) -> NoReturn:
        ManagerModel.__sensors.append(sensor)
        ManagerModel.__sensor_data[sensor] = []

    @staticmethod
    def delete_sensor(sensor: SensorItem) -> NoReturn:
        ManagerModel.__sensors.remove(sensor)
        ManagerModel.__sensor_data.pop(sensor)

    @staticmethod
    def add_diagram(diagram: DiagramItem) -> NoReturn:
        ManagerModel.__diagrams.append(diagram)

    @staticmethod
    def delete_diagram(diagram: DiagramItem) -> NoReturn:
        ManagerModel.__diagrams.remove(diagram)

    # This method starts reading from sensors
    @staticmethod
    def start() -> NoReturn:
        ManagerModel.__init_functions()
        ManagerModel.__running = True
        while ManagerModel.__running:
            ManagerModel.__read_data()
            for diagram in ManagerModel.__diagrams:
                diagram.calculate(ManagerModel.__sensor_data.copy())
                diagram.notify()

    # This method stops reading from sensors
    @staticmethod
    def stop() -> NoReturn:
        ManagerModel.__running = False
        ManagerModel.notify()
