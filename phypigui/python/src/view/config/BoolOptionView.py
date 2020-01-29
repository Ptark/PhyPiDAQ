from ...model.config.BoolOption import BoolOption
from .OptionView import OptionView
from PyQt5 import QtWidgets, QtCore
from typing import NoReturn


class BoolOptionView(OptionView):

    def __init__(self, parent: QtWidgets.QWidget, option: BoolOption):
        super().__init__(parent, option.name, option.description)
        self.__option: BoolOption = option
        # Checkbox
        self.__checkbox: QtWidgets.QRadioButton = QtWidgets.QRadioButton()

        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        # Configure checkbox
        self.__checkbox.setChecked(self.__option.enabled)
        self.__checkbox.toggled.connect(self.__set_option_data)
        # Add Checkbox to option-layout
        self._option_layout.addWidget(self.__checkbox, 0, QtCore.Qt.AlignRight)

    @property
    def option(self) -> BoolOption:
        return self.__option

    def __set_option_data(self, is_checked: bool) -> NoReturn:
        self.__option.enabled = is_checked
