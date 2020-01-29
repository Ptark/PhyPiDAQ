from ...model.config.NumOption import NumOption
from .OptionView import OptionView
from PyQt5 import QtWidgets, QtGui, QtCore
from typing import NoReturn


class NumOptionView(OptionView):

    def __init__(self, parent: QtWidgets.QWidget, option: NumOption):
        super().__init__(parent, option.name, option.description)
        self.__option: NumOption = option
        # Text-field
        self.__text_field: QtWidgets.QLineEdit = QtWidgets.QLineEdit()
        # Validator for input
        self.__validator: QtGui.QRegExpValidator = QtGui.QRegExpValidator()
        # Error-label
        self.__error_label: QtWidgets.QLabel = QtWidgets.QLabel("Min: " + str(self.__option.min) + "  Max: "
                                                                        + str(self.__option.max))
        # Text-field-layout
        self.__tf_layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout(self)
        # Text-field-widget
        self.__tf_widget = QtWidgets.QWidget(self)

        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        # Set RegEx for validator
        self.__validator.setRegExp(QtCore.QRegExp("^([+-]?\\d*\\.?\\d*)$"))

        # Configure text-field
        self.__text_field.setFixedSize(250, 40)
        self.__text_field.setStyleSheet('QLineEdit { background-color: white; }')
        self.__text_field.setText(self.__option.number.__str__())
        self.__text_field.setValidator(self.__validator)
        self.__text_field.textChanged.connect(self.__set_option_data)

        # Configure error-label
        self.__error_label.setStyleSheet("QLabel { color: red; }")
        self.__error_label.setVisible(False)

        # Add text-field-widget to layout
        self._option_layout.addWidget(self.__tf_widget)

        # Set text-field-layout as layout for text-field-widget
        self.__tf_widget.setLayout(self.__tf_layout)

        # Add text-field and error-label to text-field-layout
        self.__tf_layout.addWidget(self.__text_field, 0, QtCore.Qt.AlignRight)
        self.__tf_layout.addWidget(self.__error_label, 0, QtCore.Qt.AlignRight)

    @property
    def option(self) -> NumOption:
        return self.__option

    def __set_option_data(self, text: str) -> NoReturn:
        # Create style-sheet
        style_sheet: str = 'QLineEdit { background-color: white; }'

        # Validate input
        if self.__validator.validate(text, 0):
            # Check for edge-cases
            if QtCore.QRegularExpression("^[-+]?\\.?$").match(text).hasMatch():
                self.__option.number = 0
                self.__error_label.setVisible(False)
            else:
                if float(text) > self.__option.max or float(text) < self.__option.min:
                    self.__option.number = \
                        str(self.__option.max) if float(text) > self.__option.max else str(self.__option.min)
                    style_sheet = 'QLineEdit { background-color: ' + OptionView.ERROR_COLOR + '; }'
                    self.__error_label.setVisible(True)
                else:
                    self.option.number = round(float(text), self.__option.decimals - 1)
                    self.__error_label.setVisible(False)
            self.__text_field.setStyleSheet(style_sheet)
