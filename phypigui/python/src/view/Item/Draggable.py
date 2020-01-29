from abc import ABC
from typing import NoReturn

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget

from .ItemView import ItemView


class Draggable(ItemView, ABC):
    """Abstract class for displaying a drag- and drop-able item

        Attributes:
            parent (QWidget): The main widget of the window.
            icon_path (str): A file path of the icon displayed on the item.
    """
    def __init__(self, parent: QWidget, icon_path: str):
        super().__init__(parent, icon_path)

        self.__mousePressPos: QPoint = None
        self.__mouseMovePos: QPoint = None

    def _save_position(self, pos: QPoint) -> NoReturn:
        """Saves the given global position

            Saves the given global position which is used for drag and drop.
            It is usually called when the user presses on the widget.

            Args:
                pos (QPoint): The current global position to save.
        """
        self.__mousePressPos = pos
        self.__mouseMovePos = pos

    def _move_item(self, pos: QPoint) -> NoReturn:
        """Moves the item to the given global position

            Moves the item to the given global position.
            It is used for drag and drop.
            It is usually called when the user moves the mouse over the widget when a button is pressed.

            Args:
                pos (QPoint): The current global position to move to.
        """
        if self.__mouseMovePos is not None:
            curr_pos = self.mapToGlobal(self.pos())
            diff = pos - self.__mouseMovePos
            new_pos = self.mapFromGlobal(curr_pos + diff)
            self.move(new_pos)
            self.__mouseMovePos = pos

    def _on_click(self) -> NoReturn:
        """Is called when the Widget is clicked on"""
        pass

    def mouseReleaseEvent(self, event: QMouseEvent) -> NoReturn:
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return

        if event.button() == Qt.LeftButton:
            self._on_click()
