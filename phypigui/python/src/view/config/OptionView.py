from abc import ABC

from typing import NoReturn
from PyQt5 import QtWidgets, QtCore

from ..Translator import Translator


class OptionViewMeta(type(ABC), type(QtWidgets.QWidget)):
    pass


class OptionView(ABC, QtWidgets.QWidget, metaclass=OptionViewMeta):
    """This class is a superclass for all kind of item-options in the view"""

    # style-sheet rgb value
    ERROR_COLOR: str = 'rgb(255, 158, 158)'

    def __init__(self, parent: QtWidgets.QWidget, name: str, description: str):
        """Initialising an OptionView object

        Args:
            parent (QtWidgets.QWidget): The parent widget
            name (str): Name of the option, which will be figured by a label
            description (str): Description of this option, which will be figured by a label
        """
        super().__init__(parent)

        # Group-box and its layout
        self.__box = QtWidgets.QGroupBox()
        if name == '':
            self.__box.setTitle(name)
        else:
            self.__box.setTitle(Translator.tr(name) + ':')
        layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.__box, 0, QtCore.Qt.AlignTop)
        # Layout for the whole option
        self._option_layout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout(self.__box)
        # Label, which stores name of option
        if description[-10:] == "einstellen":
            description = Translator.tr("%s einstellen") % Translator.tr(name)
        else:
            description = Translator.tr(description)
        self._description_label: QtWidgets.QLabel = QtWidgets.QLabel(description, self)

        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        # Add description-label to option-layout
        self._option_layout.addWidget(self._description_label, 0, QtCore.Qt.AlignLeft)
