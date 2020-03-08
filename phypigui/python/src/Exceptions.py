from .view.Translator import Translator


class InvalidOptionInput(Exception):
    """Raises if an option receives the wrong input"""
    def __init__(self, option_name: str):
        super().__init__()
        self.__option_name: str = option_name

    def __str__(self) -> str:
        return Translator.tr("Ungültige Eingabe bei der Option \"%s\"") % Translator.tr(self.__option_name)


class NumberTooSmall(InvalidOptionInput):
    """Raises if a number is smaller than the minimum allowed number in this context"""
    def __init__(self, option_name: str, number: float):
        super().__init__(option_name)
        self.__number: float = number

    def __str__(self) -> str:
        return super().__str__() + ": " + Translator.tr("Zahl sollte größer gleich %d sein") % self.__number


class NumberTooLarge(InvalidOptionInput):
    """Raises if a number is larger than the maximum allowed number in this context"""
    def __init__(self, option_name: str, number: float):
        super().__init__(option_name)
        self.__number: float = number

    def __str__(self) -> str:
        return super().__str__() + ": " + Translator.tr("Zahl sollte kleiner gleich %d sein") % self.__number


class OutOfRange(InvalidOptionInput):
    """Raises if a number is out of range of this context"""
    def __init__(self, option_name: str, selection_index: int):
        super().__init__(option_name)
        self.__selection_index: int = selection_index

    def __str__(self) -> str:
        return super().__str__() + ": " + Translator.tr("Index %d außerhalb des Bereichs") % self.__selection_index


class PathDoesntExist(Exception):
    """Raises if a file or directory doesn't exist"""
    def __init__(self, path: str, item_name: str):
        super().__init__()
        self.__path: str = path
        self.__item_name: str = item_name

    def __str__(self) -> str:
        if self.__path == "None":
            return Translator.tr("Kein Dateipfad in \"%s\" ausgewählt") % Translator.tr(self.__item_name)
        return Translator.tr("Der ausgewählte Dateipfad \"%s\" in \"%s\" wurde nicht gefunden") % \
               (self.__path, Translator.tr(self.__item_name))


class IllegalFileType(Exception):
    """Raises if a file or directory doesn't exist"""
    def __init__(self, text: str, path: str):
        super().__init__()
        self.__text: str = text
        self.__path: str = path

    def __str__(self) -> str:
        return Translator.tr(self.__text) % self.__path


class IDNotFound(Exception):
    """Raises if a given ID is not founded in this context"""
    def __init__(self, id: int, context: str):
        super().__init__()
        self.__id: int = id
        self.__context: str = context

    def __str__(self) -> str:
        return Translator.tr("Die ID %d existiert nicht im Kontext \"%s\"") % (self.__id, Translator.tr(self.__context))


class InputAlreadyConnected(Exception):
    """Raises if you trying to connect a input, which is already connected"""
    def __init__(self, id: int):
        super().__init__()
        self.__id: int = id

    def __str__(self) -> str:
        return Translator.tr("Der Eingang mit der ID %d ist schon verbunden") % self.__id


class DuplicateWorkspaceItem(Exception):
    """Raises if an item, which can only exist once on the workspace, is dragged on to the workspace a second time"""
    pass


class DiagramMaximumReached(Exception):
    """Raises if the maximum number of diagrams that can be displayed is reached"""
    pass


class SensorDAQError(Exception):
    """Raises if an error occured while initializing a PhyPiDAQ Sensor Configuration"""
    pass
