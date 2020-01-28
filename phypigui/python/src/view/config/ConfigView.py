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

   # def __init__(self, name: str, config: ConfigModel):
    def __init__(self, name: str):
        QtWidgets.QWidget.__init__(self)
        """
        self.__config: ConfigModel = config
        self.__num_options: List[NumOptionView] = []
        self.__bool_options: List[BoolOptionView] = []
        self.__file_options: List[FileOptionView] = []
        self.__enum_options: List[EnumOptionView] = []
        for option in self.__config.bool_options:
            self.__bool_options.append(BoolOptionView(option))
        for option in self.__config.num_options:
            self.__num_options.append(NumOptionView(option))
        for option in self.__config.file_options:
            self.__file_options.append(FileOptionView(option))
        for option in self.__config.enum_options:
            self.__enum_options.append(EnumOptionView(option))
        """
        self.__w1 = OptionView.OptionView(self, "name")
        self.__layout: QtWidgets.QLayout = QtWidgets.QVBoxLayout()



        self.__title: str = name + ' Einstellungsfenster'
        self.__icon = QtGui.QIcon()
        self.__init_ui()
        self.__init__window()

        self.show()

    def __init_ui(self) -> NoReturn:
        self.__icon.addPixmap(QtGui.QPixmap(self.__icon_source))
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle(self.__title)
        self.resize(700, 900)
        self.setWindowIcon(self.__icon)
        self.raise_()
        self.activateWindow()
        self.setWindowModality(QtCore.Qt.ApplicationModal)

    def __init__window(self) -> NoReturn:
        self.__layout.addWidget(self.__w1, 2)

    def __on_close(self) -> NoReturn:
        pass
