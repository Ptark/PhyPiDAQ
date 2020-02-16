from ...model.config.NumOption import NumOption
from .OptionView import OptionView
from PyQt5 import QtWidgets, QtGui, QtCore
from typing import NoReturn
from ...Exceptions import NumberTooSmall, NumberTooLarge


class NumOptionView(OptionView):

    def __init__(self, parent: QtWidgets.QWidget, option: NumOption):
        super().__init__(parent, option.name, option.description)
        self.__option: NumOption = option
        if self.__option.decimals == 0 and (self.__option.max - self.__option.min) <= 41:
            # Slider
            self.__slider: QtWidgets.QSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
            # Slider-group
            self.__slider_group: QtWidgets.QGroupBox = QtWidgets.QGroupBox(self)
            # Slider-layout
            self.__slider_layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout(self.__slider_group)
            # Selection-label
            self.__selection_label: QtWidgets.QLabel = QtWidgets.QLabel(self)

            self.__init_slider_ui()
        else:
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
            self.__tf_widget: QtWidgets.QWidget = QtWidgets.QWidget(self)

            self.__init_text_field_ui()

    def __init_text_field_ui(self) -> NoReturn:
        # Set RegEx for validator
        self.__validator.setRegExp(QtCore.QRegExp("^([+-]?\\d*\\.?\\d{0," + str(self.__option.decimals) + "})$"))

        # Configure text-field
        self.__text_field.setFixedSize(250, 40)
        self.__text_field.setStyleSheet('QLineEdit { background-color: white; }')
        self.__text_field.setText(self.__option.number.__str__())
        self.__text_field.setValidator(self.__validator)
        self.__text_field.textChanged.connect(self.__set_text_field_data)

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

    def __init_slider_ui(self) -> NoReturn:
        # Configure slider
        self.__slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.__slider.setFixedSize(250, 40)
        self.__slider.setMinimum(self.__option.min)
        self.__slider.setMaximum(self.__option.max)
        self.__slider.valueChanged.connect(self.__set_slider_data)

        self.__slider_group.setStyleSheet("QGroupBox { border: 1px solid gray; }")

        # Configure slider-label
        self.__selection_label.setText(str(self.__option.number))

        # Add slider-group to layout
        self._option_layout.addWidget(self.__slider_group)

        # Add slider and selection-label to slider-layout
        self.__slider_layout.addWidget(self.__selection_label, 0, QtCore.Qt.AlignCenter)
        self.__slider_layout.addWidget(self.__slider, 0, QtCore.Qt.AlignCenter)

    @property
    def option(self) -> NumOption:
        return self.__option

    def __set_text_field_data(self, text: str) -> NoReturn:
        # Create style-sheet
        style_sheet: str = 'QLineEdit { background-color: white; }'

        # Validate input
        if self.__validator.validate(text, 0):
            # Check for edge-cases
            try:
                if QtCore.QRegularExpression("^[-+]?\\.?$").match(text).hasMatch():
                    self.__option.number = 0
                else:
                    self.__option.number = round(float(text), self.__option.decimals - 1)
                self.__error_label.setVisible(False)
            except Exception:
                style_sheet = 'QLineEdit { background-color: ' + OptionView.ERROR_COLOR + '; }'
                self.__error_label.setVisible(True)
            except NumberTooLarge:
                self.__option.number = self.__option.max
            except NumberTooSmall:
                self.__option.number = self.__option.min
            self.__text_field.setStyleSheet(style_sheet)

    def __set_slider_data(self, number: int) -> NoReturn:
        self.__selection_label.setText(str(number))
        self.__option.number = float(number)
