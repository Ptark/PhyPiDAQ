from ...model.config.EnumOption import EnumOption
from .OptionView import OptionView
from PyQt5 import QtWidgets


class EnumOptionView(OptionView):

    def __init__(self, parent: QtWidgets.QWidget, option: EnumOption):
        self.__option: EnumOption = option
        super().__init__(parent, option.name, option.description)

    @property
    def option(self) -> EnumOption:
        return self.__option
