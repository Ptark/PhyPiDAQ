import copy

from pathlib import Path
from typing import NoReturn, List
from PyQt5 import QtWidgets, QtCore

from .OptionView import OptionView
from ...model.config.FileOption import FileOption


class FileOptionView(OptionView):
    """This class represents the GUI version of a path-selecting option

    A FileOptionView object is a QWidget.
    It models a path-selecting option with two labels, for the name and the description, one textfield for the path-
    preview and a button for opening the file-selection-dialog.
    """

    def __init__(self, parent: QtWidgets.QWidget, option: FileOption):
        """Initialising an FileOptionView object

        Args:
            parent (QtWidgets.QWidget): The parent widget
            option (EnumOption): Path-selecting option, which this FileOptionView figures
        """
        super().__init__(parent, option.name, option.description)

        self.__option: FileOption = option

        # File-widget (widget for a text-field and a browse-button)
        self.__file_widget: QtWidgets.QWidget = QtWidgets.QWidget(self)
        # Layout for file-widget
        self.__file_layout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout(self.__file_widget)
        # Text-field and browse-button
        self.__text_field: QtWidgets.QLineEdit = QtWidgets.QLineEdit()
        self.__browse_button: QtWidgets.QPushButton = QtWidgets.QPushButton()

        # Calculate letters per text-field
        self.__l_count: int = 0

        self.__init_ui()

        # Configure file-dialog
        self.__file_dialog: QtWidgets.QFileDialog = QtWidgets.QFileDialog(self)
        self.__init_dialog()

    def __init_ui(self) -> NoReturn:
        # Configure text-field
        self.__text_field.setText('')
        self.__text_field.setFixedSize(300, 40)
        self.__l_count = int(self.__text_field.width() / 12)
        self.__text_field.setEnabled(False)
        if self.option.path is None:
            self.__text_field.setText('Select path')
            self.__text_field.setToolTip('No path')
        else:
            self.__set_text_field(self.option.path)

        self.__text_field.setStyleSheet("QLineEdit { color: rgb(90, 90, 90); }")

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
        self.__file_dialog.setDirectory(str(self.__option.start_path))

    @property
    def option(self) -> FileOption:
        """Copy of the option this FileOptionView figures"""
        return copy.deepcopy(self.__option)

    def __on_click(self) -> NoReturn:
        paths: List[str] = []

        if self.__file_dialog.exec():
            self.__file_dialog.setDirectory(str(self.__option.path))
            paths = self.__file_dialog.selectedFiles()
            self.__set_option_data(Path(str(paths[0])))

    def __set_text_field(self, path: Path) -> NoReturn:
        s_path: str = str(path)
        text: str = ''

        self.__text_field.setToolTip(s_path)

        if len(s_path) > self.__l_count:
            file_name: str = path.name
            if len(file_name) > self.__l_count:
                text = file_name
            else:
                text = s_path[:self.__l_count - len(file_name)] + ' [...] /' + file_name
        else:
            text = s_path
        self.__text_field.setText(text)

    def __set_option_data(self, path: Path) -> NoReturn:
        if str(path) == '':
            return

        self.__set_text_field(path)

        self.__option.path = path
