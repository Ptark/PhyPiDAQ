from ..view.Translator import Translator


class NumberTooSmall(Exception):
    """Raises if a number is smaller than the minimum allowed number in this context"""
    pass


class NumberTooLarge(Exception):
    """Raises if a number is larger than the maximum allowed number in this context"""
    pass


class OutOfRange(Exception):
    """Raises if a number is out of range of this context"""
    pass


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


class IDNotFound(Exception):
    """Raises if a given ID is not founded in this context"""
    pass


class InputAlreadyConnected(Exception):
    """Raises if you trying to connect a input, which is already connected"""
    pass
