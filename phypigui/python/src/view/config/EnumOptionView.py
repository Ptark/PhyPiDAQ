import copy

from typing import NoReturn
from PyQt5 import QtWidgets, QtCore

from .OptionView import OptionView
from ...model.config.EnumOption import EnumOption


class EnumOptionView(OptionView):
    """This class represents the GUI version of a enumerable option

    A EnumOptionView object is a QWidget.
    It models a enumerable option with two labels, for the name and the description and one combobox (Drop-down-menu).
    """

    def __init__(self, parent: QtWidgets.QWidget, option: EnumOption):
        """Initialising an EnumOptionView object

        Args:
            parent (QtWidgets.QWidget): The parent widget
            option (EnumOption): Enumerable option, which this EnumOptionView figures
        """
        super().__init__(parent, option.name, option.description)

        self.__option: EnumOption = option

        # Dropbox
        self.__dropbox: QtWidgets.QComboBox = QtWidgets.QComboBox(self)

        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        # Configure dropbox
        self.__dropbox.setFixedSize(280, 40)
        # Add all samples from this option to the dropbox and set selected-index
        for entry in self.option.samples:
            self.__dropbox.addItem(entry.value)
        self.__dropbox.setCurrentIndex(self.option.selection)
        # Connect change-event to __set_option_data()
        self.__dropbox.currentIndexChanged.connect(self.__set_option_data)
        # Add dropbox to option-layout
        self._option_layout.addWidget(self.__dropbox, QtCore.Qt.AlignRight)

    @property
    def option(self) -> EnumOption:
        """Copy of the enumerable option this EnumOptionView figures"""
        return copy.deepcopy(self.__option)

    def __set_option_data(self, selection_index: int) -> NoReturn:
        if 0 <= selection_index < len(self.__option.samples):
            self.__option.selection = selection_index
