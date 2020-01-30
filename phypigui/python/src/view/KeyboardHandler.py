from typing import NoReturn

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent

from .DiagramField.StartButtonView import StartButtonView
from .InfoBar.DeleteButtonView import DeleteButtonView
from .InfoBar.SettingsButtonView import SettingsButtonView


def delete_selection() -> NoReturn:
    DeleteButtonView.click()


def config_selection() -> NoReturn:
    SettingsButtonView.click()


def start_stop() -> NoReturn:
    StartButtonView.click()


class KeyboardHandler:
    __key_functions = {
        Qt.Key_Delete: delete_selection,
        Qt.Key_Backspace: delete_selection,
        Qt.Key_Return: config_selection,
        Qt.Key_Enter: config_selection,
        Qt.Key_Space: start_stop
    }

    @staticmethod
    def key_pressed(event: QKeyEvent) -> NoReturn:
        KeyboardHandler.__key_functions.get(event.key(), lambda: "")()
