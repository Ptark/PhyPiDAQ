from ...model.config.FileOption import FileOption
from .OptionView import OptionView
from PyQt5 import QtWidgets, QtCore
from typing import NoReturn, List


class FileOptionView(OptionView):

    def __init__(self, parent: QtWidgets.QWidget, option: FileOption):
        self.__option: FileOption = option
        super().__init__(parent, option.name, option.description)
        # File-widget (widget for a text-field and a browse-button)
        self.__file_widget: QtWidgets.QWidget = QtWidgets.QWidget(self)
        # Layout for file-widget
        self.__file_layout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout(self.__file_widget)
        # Text-field and browse-button
        self.__text_field: QtWidgets.QLineEdit = QtWidgets.QLineEdit()
        self.__browse_button: QtWidgets.QPushButton = QtWidgets.QPushButton()

        self.__init_ui()

        # Configure file-dialog
        self.__file_dialog: QtWidgets.QFileDialog = QtWidgets.QFileDialog(self)
        self.__init_dialog()

    def __init_ui(self) -> NoReturn:
        # Configure text-field
        self.__text_field.setText('')
        self.__text_field.setFixedSize(300, 40)
        self.__text_field.setEnabled(False)
        self.__text_field.setText('/home/user')
        self.__text_field.setToolTip('No path')
        # Configure browse-button
        self.__browse_button.setText('...')
        self.__browse_button.setFixedSize(40, 40)
        self.__browse_button.setToolTip('Click to select the path')
        self.__browse_button.clicked.connect(self.__on_click)

        # Add widget for text-field and browse-button to option-layout
        self._option_layout.addWidget(self.__file_widget, 0, QtCore.Qt.AlignRight)
        # Add text-field and browse-button to file-layout
        self.__file_layout.addWidget(self.__text_field, 0, QtCore.Qt.AlignLeft)
        self.__file_layout.addWidget(self.__browse_button, 0, QtCore.Qt.AlignRight)

    def __init_dialog(self) -> NoReturn:
        file_type: str = ''
        if self.__option.file_endings is not None:
            if self.__option.file_type == '':
                file_type += 'Dateiformat'
            else:
                file_type += self.__option.file_type
            file_type += ' ( '
            for ending in self.__option.file_endings:
                file_type += '*.' + ending + ' '
            file_type += ')'
            self.__file_dialog.setNameFilter(file_type)

        if self.__option.file_mode == self.__option.ANYFILE:
            self.__file_dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        elif self.__option.file_mode == self.__option.EXISTINGFILE:
            self.__file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        else:
            self.__file_dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly, True)
            self.__file_dialog.setFileMode(QtWidgets.QFileDialog.Directory)

    @property
    def option(self) -> FileOption:
        return self.__option

    def __on_click(self) -> NoReturn:
        paths: List[str] = []
        if self.__file_dialog.exec():
            paths = self.__file_dialog.selectedFiles()
            self.__set_option_data(str(paths[0]))

    def __set_option_data(self, path: str) -> NoReturn:
        if path == '':
            return
        self.__text_field.setText(path)
        self.__option.path = path
