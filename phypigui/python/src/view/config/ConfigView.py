from python.src.model.config.ConfigModel import ConfigModel
from typing import List, NoReturn
from PyQt5 import QtWidgets, QtCore, QtGui
from .NumOptionView import NumOptionView
from .BoolOptionView import BoolOptionView
from .FileOptionView import FileOptionView
from .EnumOptionView import EnumOptionView
from .OptionView import OptionView


class ConfigView(QtWidgets.QWidget):
    __icon_source = "../resources/images/buttons/settingsbutton.png"

   #def __init__(self, name: str, config: ConfigModel):
    def __init__(self, name: str, config: ConfigModel):
        QtWidgets.QWidget.__init__(self)

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


        self.__title: str = name + ' Einstellungsfenster'
        self.__icon = QtGui.QIcon()

        self.__init_ui()
        self.__init__window()

        self.show()

    def __init_ui(self) -> NoReturn:
        self.resize(700, 900)
        self.__icon.addPixmap(QtGui.QPixmap(self.__icon_source))
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
            option_layout.addWidget(option)
        for option in self.__enum_options:
            option_layout.addWidget(option)
        for option in self.__num_options:
            option_layout.addWidget(option)
        for option in self.__bool_options:
            option_layout.addWidget(option)
        end_widget: QtWidgets.QWidget = QtWidgets.QWidget(self)
        option_layout.addWidget(end_widget, 10)
        """
        for i in range(0, 100):
            option = OptionView(scroll, i.__str__())
            option.setMinimumHeight(100)
            option_layout.addWidget(option)
"""
    def __on_close(self) -> ConfigModel:
        """
        config: ConfigModel = ConfigModel()
        for option in self.__file_options:
            config.add_file_option(option.option)
        for option in self.__enum_options:
            config.add_enum_option(option.option)
        for option in self.__num_options:
            config.add_num_option(option.option)
        for option in self.__bool_options:
            config.add_bool_option(option.option)
        self.__config = config
        """

    def closeEvent(self, close_event: QtGui.QCloseEvent):
        self.__on_close()
