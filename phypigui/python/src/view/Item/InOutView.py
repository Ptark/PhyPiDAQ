from abc import ABC, abstractmethod
from typing import NoReturn

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QFrame, QWidget

from ..Workspace.WireView import WireView
from ..View import View


class InOutViewMeta(type(QFrame), type(View)):
    pass


class InOutView(QFrame, View, ABC, metaclass=InOutViewMeta):
    """Abstract class for displaying an item input or output"""

    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        self.setFixedSize(20, 12)

        self.setStyleSheet("""
            QFrame {
                border: 2px solid black;
                border-radius: 5px;
                background-color: #FF4444;
                }
            """)

    def _get_connection_point(self) -> QPoint:
        p = self.parent().mapTo(self.parent().parent().parent(), self.pos())
        p.setX(p.x() + self.width() / 2)
        p.setY(p.y() + self.height() / 2)
        return p

    @abstractmethod
    def redraw_wires(self) -> NoReturn:
        """Redraws all connected wires"""
        pass

    @abstractmethod
    def _remove_wire(self, wire: WireView) -> NoReturn:
        """Removes the given wire

            This does not call delete on the given wire.

            Args:
                wire (WireView): The wire to remove
        """
        pass

    @abstractmethod
    def delete_all_wires(self) -> NoReturn:
        """Deletes all connected wires"""
        pass

    # Catches and stops all mouse events so other widgets under
    # the in-/outputs (items and workspace) don't get mouse events
    def mousePressEvent(self, event: QMouseEvent) -> NoReturn:
        pass

    def mouseMoveEvent(self, event: QMouseEvent) -> NoReturn:
        pass

    def mouseReleaseEvent(self, event: QMouseEvent) -> NoReturn:
        pass
