import copy
import time

from typing import Dict, List, NoReturn

from numpy import random

from ..workspace.WorkspaceModel import WorkspaceModel


class ManagerModel:
    """This class manages the initialising of the lambda-functions, the reading of data from all sensors
    and the calculating of the results

    ManagerModel has only static attributes and methods and holds lists from all SensorItems for reading data and all
    DiagramItems for calculating its data.
    This class holds also the current, from the user, selected OutputItem to calculate its data too.
    If no OutputItem is selected, the Manager will ignore it.
    The main methods of this class are start() and stop().
    """

    __sensors: List['SensorItem'] = []
    __diagrams: List['DiagramItem'] = []
    __sensor_data: Dict['SensorItem', List[float]] = {}
    __running: bool = False
    __selected_item: 'OutputItem' = None

    @staticmethod
    def __init_functions() -> NoReturn:
        for diagram in ManagerModel.__diagrams:
            diagram.calculate_functions()

    @staticmethod
    def __read_data() -> NoReturn:
        for sensor in ManagerModel.__sensor_data:
            ManagerModel.__sensor_data[sensor] = [random.random()]  # sensor.read()

    @staticmethod
    def is_running() -> bool:
        """Indicates, if the Manager is running and reading data

        Returns:
            bool: True, if Manager is running
        """
        return ManagerModel.__running

    @staticmethod
    def get_selected_item() -> 'OutputItem':
        """Returns a copy of the current selected OutputItem

        Returns:
             OutputItem: Copy of current selected item.
                If no OutputItem is selected, it will return None.
        """
        return copy.deepcopy(ManagerModel.__selected_item)

    @staticmethod
    def set_selected_item(selected: 'ItemModel') -> NoReturn:
        """Sets current selected OutputItem

        Args:
            selected (OutputItem): Current selected OutputItem
        """
        if selected is not None and not WorkspaceModel.is_input_item(selected.id):
            return
        ManagerModel.__selected_item = selected

    @staticmethod
    def add_sensor(sensor: 'SensorItem') -> NoReturn:
        """Adds a SensorItem to the global list of SensorItems

        This method is typically called in the constructor of a SensorItem to add it to the list.

        Args:
            sensor (SensorItem): SensorItem to be added
        """
        ManagerModel.__sensors.append(sensor)
        ManagerModel.__sensor_data[sensor] = []

    @staticmethod
    def delete_sensor(sensor: 'SensorItem') -> NoReturn:
        """Deletes a SensorItem from the global list of SensorItems

        This method is typically called in the destructor af a SensorItem.

        Args:
            sensor (SensorItem): SensorItem to be deleted
        """
        ManagerModel.__sensors.remove(sensor)
        ManagerModel.__sensor_data.pop(sensor)

    @staticmethod
    def add_diagram(diagram: 'DiagramItem') -> NoReturn:
        """Adds a DiagramItem to the global list of DiagramItems

        This method is typically called in the constructor of a DiagramItem to add it to the list.

        Args:
            diagram (DiagramItem): DiagramItem to be added
        """
        ManagerModel.__diagrams.append(diagram)

    @staticmethod
    def delete_diagram(diagram: 'DiagramItem') -> NoReturn:
        """Deletes a DiagramItem from the global list of DiagramItems

        This method is typically called in the destructor af a DiagramItem.

        Args:
            diagram (DiagramItem): DiagramItem to be deleted
        """
        ManagerModel.__diagrams.remove(diagram)

    @staticmethod
    def start() -> NoReturn:
        """Starts a measuring process and calculates for all DiagramItems and the selected item their data

        Typically called if the start button was clicked.
        First this method calculates all lambda-functions and units recursively starting in the DiagramItems.
        Second this method continuously reads the current data from each SensorItem in its list and and put it in the
        lambda-function of every DiagramItem. Also it notify the View. After that the method puts in the read data in
        the selected OutputItem and notify the View.
        The second step is repeated until stop() is called.
        """
        ManagerModel.__init_functions()
        ManagerModel.__running = True
        while ManagerModel.__running:
            ManagerModel.__read_data()
            for diagram in ManagerModel.__diagrams:
                diagram.calculate(ManagerModel.__sensor_data)
                diagram.notify()
            if ManagerModel.__selected_item is not None and ManagerModel.__selected_item not in ManagerModel.__diagrams:
                ManagerModel.__selected_item.calculate(ManagerModel.__sensor_data)
                ManagerModel.__selected_item.notify()
            time.sleep(0.1)  # TODO: async

    @staticmethod
    def stop() -> NoReturn:
        """Stops the measuring process

        Typically called if the stop button was clicked.
        """
        ManagerModel.__running = False

    @staticmethod
    def restart() -> NoReturn:
        """Restarts the measuring process

        Typically called if a item or connection was deleted.
        """
        ManagerModel.stop()
        ManagerModel.start()
