from typing import NoReturn

from PyQt5.QtCore import QLine
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget

from ..Item.InputView import InputView
from ..Item.OutputView import OutputView
from . import WorkspaceView


class WireView(QLine):
    output: OutputView
    input: InputView

    def __init__(self, parent):
        super().__init__(parent)
        self.output: OutputView
        self.input: InputView
        # TODO: Wire zeichnen

    def redraw(self):
        pass

    def _change_selected_view(self) -> NoReturn:
        pass

    def get_info_widget(self) -> QWidget:
        pass

    def open_config(self) -> NoReturn:
        pass

    def delete(self) -> NoReturn:
        WorkspaceView.WorkspaceView.delete_wire(self)

    def mousePressEvent(self, event: QMouseEvent) -> NoReturn:
        self.selected = True

    def mouseMoveEvent(self, event) -> NoReturn:
        pass
