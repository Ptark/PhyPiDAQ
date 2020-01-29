from ...model.config.BoolOption import BoolOption
from .OptionView import OptionView
from PyQt5 import QtWidgets


class BoolOptionView(OptionView):

    def __init__(self, parent: QtWidgets.QWidget, option: BoolOption):
        self.__option: BoolOption = option
        super().__init__(parent, option.name)

    @property
    def option(self) -> BoolOption:
        return self.__option
