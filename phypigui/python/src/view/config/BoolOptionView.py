import copy

from typing import NoReturn
from PyQt5 import QtWidgets, QtCore

from .OptionView import OptionView
from ...model.config.BoolOption import BoolOption


class BoolOptionView(OptionView):
    """This class represents the GUI version of a boolean option

    A BoolOptionView object is a QWidget.
    It models a boolean option with two labels, for the name and the description and one checkbox.
    """

    def __init__(self, parent: QtWidgets.QWidget, option: BoolOption):
        """Initialising a BoolOptionView object

        Args:
            parent (QtWidgets.QWidget): The parent widget
            option (BoolOption): Boolean option, which this BoolOptionView figures
        """
        super().__init__(parent, option.name, option.description)

        self.__option: BoolOption = option

        # Checkbox
        self.__checkbox: QtWidgets.QCheckBox = QtWidgets.QCheckBox()

        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        # Configure checkbox
        self.__checkbox.setChecked(self.__option.enabled)
        self.__checkbox.toggled.connect(self.__set_option_data)
        # Add Checkbox to option-layout
        self._option_layout.addWidget(self.__checkbox, 0, QtCore.Qt.AlignRight)

    @property
    def option(self) -> BoolOption:
        """Copy of the boolean option this BoolOptionView figures"""
        return copy.deepcopy(self.__option)

    def __set_option_data(self, is_checked: bool) -> NoReturn:
        self.__option.enabled = is_checked
