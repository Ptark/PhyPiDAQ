from ...model.config.EnumOption import EnumOption
from .OptionView import OptionView
from PyQt5 import QtWidgets, QtGui, QtCore
from typing import NoReturn


class EnumOptionView(OptionView):

    def __init__(self, parent: QtWidgets.QWidget, option: EnumOption):
        self.__option: EnumOption = option
        super().__init__(parent, option.name, option.description)
        self.__dropbox: QtWidgets.QComboBox = QtWidgets.QComboBox(self)

        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        self._option_layout.addWidget(self.__dropbox, QtCore.Qt.AlignRight)
        self.__dropbox.setFixedSize(280, 40)
        for entry in self.option.samples:
            self.__dropbox.addItem(entry.value)
        self.__dropbox.setCurrentIndex(self.option.selection)

    @property
    def option(self) -> EnumOption:
        return self.__option

    def __set_option_data(self) -> NoReturn:
        pass
