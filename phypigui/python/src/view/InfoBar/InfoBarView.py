from typing import NoReturn

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

from .DeleteButtonView import DeleteButtonView
from .SettingsButtonView import SettingsButtonView
from ..Translator import Translator
from ..Workspace import WorkspaceView


class InfoBarView(QWidget):
    """This class represents the Info bar which contains Delete button and Settings button"""
    __infobar: 'InfoBarView' = None

    def __init__(self, parent):
        super().__init__(parent)

        InfoBarView.infobar = self

        self.__horizontal_layout: QHBoxLayout = QHBoxLayout()
        self.__info_widget: QWidget = QWidget()

        Translator.language_changed.signal.connect(InfoBarView.refresh_infobar)
        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        button_layout = QVBoxLayout()
        button_layout.addWidget(DeleteButtonView(self))
        button_layout.addWidget(SettingsButtonView(self))

        self.__horizontal_layout.addWidget(self.__info_widget)
        self.__horizontal_layout.addLayout(button_layout)

        self.setLayout(self.__horizontal_layout)

    def update_info_widget(self, widget: QWidget) -> NoReturn:
        """adds the information about the selected WorkspaceItemView in the info bar"""
        self.__horizontal_layout.replaceWidget(self.__info_widget, widget)
        self.__info_widget.hide()
        self.__info_widget = widget
        self.__info_widget.show()

    @staticmethod
    def refresh_infobar() -> NoReturn:
        """refreshes the info bar if there is a selected WorkspaceItemView"""
        if WorkspaceView.WorkspaceView.selection is not None:
            widget = WorkspaceView.WorkspaceView.selection.get_info_widget()
        else:
            widget = QWidget()
        InfoBarView.infobar.update_info_widget(widget)
