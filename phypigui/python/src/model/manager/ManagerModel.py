
class ManagerModel:
    __sensors = List[SensorItem]
    __diagrams = List[DiagramItem]
    __sensor_data = Dict[SensorItem, ]
    __running = False
    selected_item = OutputItem

    @staticmethod
    def __init_functions() -> NoReturn:
        return

    @staticmethod
    def __read_data() -> bool:
        return

    @staticmethod
    def add_sensor(sensor: SensorItem) -> NoReturn:
        return

    @staticmethod
    def delete_sensor(sensor: SensorItem) -> NoReturn:
        return

    @staticmethod
    def add_diagram(diagram: DiagramItem) -> NoReturn:
        return

    @staticmethod
    def delete_diagram(diagram: DiagramItem) -> NoReturn:
        return

    @staticmethod
    def start() -> NoReturn:
        return

    @staticmethod
    def stop() -> NoReturn:
        return
