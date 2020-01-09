from typing import Dict, List, NoReturn
from ..item.SensorItem import SensorItem
from ..item.DiagramItem import DiagramItem
from ..item.OutputItem import OutputItem
from ..Model import Model


class ManagerModel(Model):
    __sensors: List[SensorItem] = []
    __diagrams: List[DiagramItem] = []
    __sensor_data: Dict[SensorItem, List[float]] = {}
    __running: bool = False
    selected_item: OutputItem = None

    @staticmethod
    def __init_functions() -> NoReturn:
        for diagram in ManagerModel.__diagrams:
            diagram.calculate_functions()
        return

    @staticmethod
    def __read_data() -> NoReturn:
        for sensor in ManagerModel.__sensor_data:
            #TODO: set value in __sensor_data
            #ManagerModel.__sensor_data[sensor] = sensor.read()
        return

    @staticmethod
    def is_running() -> bool:
        return ManagerModel.__running

    @staticmethod
    def add_sensor(sensor: SensorItem) -> NoReturn:
        ManagerModel.__sensors.append(sensor)
        #TODO: add sensor to __sensor_data
        return

    @staticmethod
    def delete_sensor(sensor: SensorItem) -> NoReturn:
        ManagerModel.__sensors.remove(sensor)
        #TODO: delete sensor from __sensor_data
        return

    @staticmethod
    def add_diagram(diagram: DiagramItem) -> NoReturn:
        ManagerModel.__diagrams.append(diagram)
        return

    @staticmethod
    def delete_diagram(diagram: DiagramItem) -> NoReturn:
        ManagerModel.__diagrams.remove(diagram)
        return

    #This method starts reading from sensors
    @staticmethod
    def start() -> NoReturn:
        ManagerModel.__init_functions()
        ManagerModel.__running = True
        ManagerModel.notify()
        while ManagerModel.__running:
            ManagerModel.__read_data()
            for diagram in ManagerModel.__diagrams:
                diagram.calculate(ManagerModel.__sensor_data.copy())
                diagram.notify()
        return

    #This method stopps reading from sensors
    @staticmethod
    def stop() -> NoReturn:
        ManagerModel.__running = False
        ManagerModel.notify()
        return
