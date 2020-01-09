from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QPainter, QMouseEvent
from PyQt5.QtWidgets import QWidget, QPushButton


class WireView(QPainter, Selectable):
    output = None  # Todo: OutPutView
    input = None  # Todo: InPutView

    def redraw(self):
        pass

    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        pass

    def get_info_widget(self):
        pass

    def delete(self):
        pass


class StartButtonView(QPushButton):
    start_image: ""
    stop_image: ""
    is_started: bool

    def __on_click(self):
        pass


class WorkspaceView(QWidget):
    selection: Selectable
    wire_in_hand: WireView
    items = []  # list_of_WorkspaceItemView
    wires = []  # list_of_WireView

    def __init__(self, parent):
        super().__init__(parent)
        self.init_view()

    def mousePressEvent(event: QMouseEvent) -> None:
        pass

    def add_item(item: WorkspaceItemView) -> None:
        pass

    def add_wire(wire: WireView) -> None:
        pass

    def delete_item(item: WorkspaceItemView) -> None:
        pass

    def delete_wire(wire: WireView) -> None:
        pass
