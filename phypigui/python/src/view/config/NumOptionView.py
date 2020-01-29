from ...model.config.NumOption import NumOption
from .OptionView import OptionView
from PyQt5 import QtWidgets, QtGui, QtCore
from typing import NoReturn


class NumOptionView(OptionView):

    def __init__(self, parent: QtWidgets.QWidget, option: NumOption):
        super().__init__(parent, option.name)
        self.__option: NumOption = option
        self.setMinimumHeight(50)
        self.__text_field: QtWidgets.QLineEdit = QtWidgets.QLineEdit()
        self.__validator: QtGui.QRegExpValidator = QtGui.QRegExpValidator()
        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        self.__validator.setRegExp(QtCore.QRegExp("^([+-]?\\d*\\.?\\d*)$"))
        self.__text_field.setFixedSize(250, 40)
        self.__text_field.setAutoFillBackground(True)
        palette: QtGui.QPalette = QtGui.QPalette()
        palette.setColor(self.__text_field.backgroundRole(), QtCore.Qt.white)
        self.__text_field.setPalette(palette)
        self.__text_field.setText(self.__option.number.__str__())
        self.__text_field.setValidator(self.__validator)
        self.__text_field.textChanged.connect(self.__set_option_data)
        self._layout.addWidget(self.__text_field)

    @property
    def option(self) -> NumOption:
        return self.__option

    def __set_option_data(self, text: str) -> NoReturn:
        if self.__validator.validate(text, 0):
            if QtCore.QRegularExpression("^[-+]?\\.?$").match(text).hasMatch():
                self.__option.number = 0
            else:
                palette: QtGui.QPalette = QtGui.QPalette()
                palette.setColor(self.__text_field.backgroundRole(), OptionView.ERROR_COLOR)
                if float(text) > self.__option.max:
                    self.__option.number = self.__option.max.__str__()
                elif float(text) < self.__option.min:
                    self.__option.number = self.__option.min.__str__()
                else:
                    self.option.number = float(text)
                    palette.setColor(self.__text_field.backgroundRole(), QtCore.Qt.white)
                self.__text_field.setPalette(palette)
