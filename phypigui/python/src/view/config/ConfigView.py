import copy

from typing import List, NoReturn
from PyQt5 import QtWidgets, QtCore, QtGui

from ...SystemInfo import SystemInfo
from ..Translator import Translator
from .NumOptionView import NumOptionView
from .BoolOptionView import BoolOptionView
from .FileOptionView import FileOptionView
from .EnumOptionView import EnumOptionView
from ...model.config.ConfigModel import ConfigModel
from ..DiagramField.DiagramFieldView import DiagramFieldView


class ConfigView(QtWidgets.QWidget):
    """This class represents the settings-window of every item

    It creates all GUI versions of the options for the selected item and builds a new Window, which is always on top.
    """

    icon_path: str = SystemInfo.RESOURCES + 'images/Settings_window.png'
    set_data: QtCore.pyqtSignal = QtCore.pyqtSignal(ConfigModel)

    def __init__(self, name: str, config: ConfigModel):
        """Initialising a ConfigView object and the whole window

        Args:
            name (str): Name of the item
            config (ConfigModel): The config of the item, which contains all adjustable options
        """
        QtWidgets.QWidget.__init__(self)

        self.__has_interrupted_mp: bool = DiagramFieldView.interrupt_mp()

        self.__config: ConfigModel = config
        self.__num_options: List[NumOptionView] = []
        self.__bool_options: List[BoolOptionView] = []
        self.__file_options: List[FileOptionView] = []
        self.__enum_options: List[EnumOptionView] = []
        for option in self.__config.bool_options:
            self.__bool_options.append(BoolOptionView(self, option))
        for option in self.__config.num_options:
            self.__num_options.append(NumOptionView(self, option))
        for option in self.__config.file_options:
            self.__file_options.append(FileOptionView(self, option))
        for option in self.__config.enum_options:
            self.__enum_options.append(EnumOptionView(self, option))

        # Configure settings-window
        self.__title: str = Translator.tr(name) + ' ' + Translator.tr("Einstellungsfenster")
        self.__icon = QtGui.QIcon()

        self.__init_ui()
        self.__init__window()

        self.show()

    def __init_ui(self) -> NoReturn:
        self.resize(700, 900)
        self.__icon.addPixmap(QtGui.QPixmap(self.icon_path))
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle(self.__title)
        self.setWindowIcon(self.__icon)
        self.raise_()
        self.activateWindow()
        self.setWindowModality(QtCore.Qt.ApplicationModal)

    def __init__window(self) -> NoReturn:
        # Layout for scroll-area
        scroll_layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout(self)
        # Scroll-area
        scroll: QtWidgets.QScrollArea = QtWidgets.QScrollArea(self)
        # Add scroll-area to scroll_layout
        scroll_layout.addWidget(scroll)
        # Widget in scroll-area
        content: QtWidgets.QWidget = QtWidgets.QWidget(scroll)
        # Set widget for scroll-bar
        scroll.setWidget(content)
        # Layout for all options in this window
        option_layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout(content)
        # Set widget in scroll-area dynamic resizeable
        scroll.setWidgetResizable(True)

        # Add options to layout
        for option in self.__file_options:
            option_layout.addWidget(option, 0, QtCore.Qt.AlignTop)
        for option in self.__enum_options:
            option_layout.addWidget(option, 0, QtCore.Qt.AlignTop)
        for option in self.__num_options:
            option_layout.addWidget(option, 0, QtCore.Qt.AlignTop)
        for option in self.__bool_options:
            option_layout.addWidget(option, 0, QtCore.Qt.AlignTop)

        # Add stretch-widget to option-layout
        option_layout.addWidget(QtWidgets.QWidget(self), 10, QtCore.Qt.AlignBottom)

    def __on_close(self) -> NoReturn:
        for option in self.__file_options:
            self.__config.set_file_option(self.__file_options.index(option), option.option.path)
        for option in self.__enum_options:
            self.__config.set_enum_option(self.__enum_options.index(option), option.option.selection)
        for option in self.__num_options:
            self.__config.set_num_option(self.__num_options.index(option), option.option.number)
        for option in self.__bool_options:
            self.__config.set_bool_option(self.__bool_options.index(option), option.option.enabled)
        self.set_data.emit(self.__config)

        if self.__has_interrupted_mp:
            DiagramFieldView.start_mp()

    def closeEvent(self, close_event: QtGui.QCloseEvent):
        self.__on_close()
