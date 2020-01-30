from ...model.config.EnumOption import EnumOption
from .OptionView import OptionView
from PyQt5 import QtWidgets, QtCore
from typing import NoReturn


class EnumOptionView(OptionView):

    def __init__(self, parent: QtWidgets.QWidget, option: EnumOption):
        self.__option: EnumOption = option
        super().__init__(parent, option.name, option.description)
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
        return self.__option

    def __set_option_data(self, new_index: int) -> NoReturn:
        if 0 <= new_index < len(self.option.samples):
            self.option.selection = new_index
