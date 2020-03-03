import copy
import time

from typing import Dict, List, NoReturn

from ..config.ConfigModel import ConfigModel
from ..config.NumOption import NumOption


class ManagerModel:
    """This class manages the initialising of the lambda-functions, the reading of data from all sensors
    and the calculating of the results

    ManagerModel has only static attributes and methods and holds lists from all sensors for reading data and all
    diagrams for calculating its data.
    This class holds also the current, from the user, selected OutputItem to calculate its data too.
    If no OutputItem is selected, the Manager will ignore it.
    The main methods of this class are start() and stop().
    """

    __sensors: List['SensorItem'] = []
    __operators: List['OperatorItem'] = []
    __diagrams: List['DiagramItem'] = []
    __sensor_data: Dict['SensorItem', List[float]] = {}
    __running: bool = False
    __selected_item: 'OutputItem' = None
    __diagram_notifier: 'View' = None
    __settings: ConfigModel = ConfigModel()

    @staticmethod
    def init_config():
        ManagerModel.__settings.add_num_option(NumOption("Aktualisierungsrate",
                                                        "Aktualisierungsrate der Daten und Diagramme in "
                                                        "Aktualisierungen pro Sekunde", 10, min=0.1, max=100))

    @staticmethod
    def get_settings() -> ConfigModel:
        return ManagerModel.__settings

    @staticmethod
    def __init_functions() -> NoReturn:
        """Initialises and constructs all lambda-functions and unit recursively starting at the diagrams

        Raises:
            IDNotFound: If something went wrong with the recursion
        """
        for diagram in ManagerModel.__diagrams:
            diagram.calculate_functions()

    @staticmethod
    def __read_data() -> NoReturn:
        for sensor in ManagerModel.__sensor_data:
            ManagerModel.__sensor_data[sensor] = sensor.read()

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
    def set_selected_item(selected: 'OutputItem') -> NoReturn:
        """Sets current selected OutputItem

        Args:
            selected (OutputItem): Current selected OutputItem
        """
        ManagerModel.__selected_item = selected

    @staticmethod
    def add_sensor(sensor: 'SensorItem') -> NoReturn:
        """Adds a SensorItem to the global list of sensors

        This method is typically called in the constructor of a SensorItem to add it to the list.

        Args:
            sensor (SensorItem): SensorItem to be added
        """
        if sensor is not None:
            ManagerModel.__sensors.append(sensor)
            ManagerModel.__sensor_data[sensor] = []

    @staticmethod
    def delete_sensor(sensor: 'SensorItem') -> NoReturn:
        """Deletes a SensorItem from the global list of sensors

        This method is typically called in the destructor af a SensorItem.

        Args:
            sensor (SensorItem): SensorItem to be deleted
        """
        if sensor is not None:
            ManagerModel.__sensors.remove(sensor)
            ManagerModel.__sensor_data.pop(sensor)

    @staticmethod
    def add_operator(operator: 'OperatorItem') -> NoReturn:
        """Adds a OperatorItem to the global list of operators

        This method is typically called in the constructor of a OperatorItem to add it to the list.

        Args:
            operator (OperatorItem): OperatorItem to be added
        """
        if operator is not None:
            ManagerModel.__operators.append(operator)

    @staticmethod
    def delete_operator(operator: 'OperatorItem') -> NoReturn:
        """Deletes a OperatorItem from the global list of operators

        This method is typically called in the destructor af a OperatorItem.

        Args:
            operator (OperatorItem): OperatorItem to be deleted
        """
        if operator is not None:
            ManagerModel.__operators.remove(operator)

    @staticmethod
    def add_diagram(diagram: 'DiagramItem') -> NoReturn:
        """Adds a DiagramItem to the global list of diagrams

        This method is typically called in the constructor of a DiagramItem to add it to the list.

        Args:
            diagram (DiagramItem): DiagramItem to be added
        """
        if diagram is not None:
            ManagerModel.__diagrams.append(diagram)

    @staticmethod
    def delete_diagram(diagram: 'DiagramItem') -> NoReturn:
        """Deletes a DiagramItem from the global list of diagrams

        This method is typically called in the destructor af a DiagramItem.

        Args:
            diagram (DiagramItem): DiagramItem to be deleted
        """
        if diagram is not None:
            ManagerModel.__diagrams.remove(diagram)

    @staticmethod
    def start() -> NoReturn:    # TODO Exceptions
        """Starts a measuring process and calculates for all diagrams and the selected item their data

        Typically called if the start button was clicked.
        First this method calculates all lambda-functions and units recursively starting in the diagrams.
        Second this method continuously reads the current data from each SensorItem in its list and and put it in the
        lambda-function of every DiagramItem. Also it notify the View. After that the method puts in the read data in
        the selected OutputItem and notify the View.
        The second step is repeated until stop() is called.
        """
        ManagerModel.__init_functions()
        ManagerModel.__running = True
        diagrams: List['DiagramItem'] = ManagerModel.__diagrams.copy()
        update_rate = ManagerModel.__settings.num_options[0].number
        while ManagerModel.__running:
            start_time = time.time()
            ManagerModel.__read_data()
            for diagram in diagrams:
                diagram.calculate(ManagerModel.__sensor_data)
                diagram.notify()
            ManagerModel.__diagram_notifier.update_view()
            if ManagerModel.__selected_item is not None:
                ManagerModel.__selected_item.calculate(ManagerModel.__sensor_data)
                ManagerModel.__selected_item.notify()
            time_to_wait = 1/update_rate - time.time() + start_time
            if time_to_wait > 0:
                time.sleep(time_to_wait)
        for d in diagrams:
            d.stop()
        for i in ManagerModel.__sensors + ManagerModel.__operators + ManagerModel.__diagrams:
            i.calculate(ManagerModel.__sensor_data)
            i.notify()

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

    @staticmethod
    def set_diagram_notifier(new_notifier: 'View'):
        if ManagerModel.__diagram_notifier is None:
            ManagerModel.__diagram_notifier = new_notifier
