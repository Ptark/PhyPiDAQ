from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

from python.src.view.Selectable import Selectable
from python.src.view.Workspace.StartButtonView import StartButtonView
from python.src.view.Workspace.WireView import WireView


class WorkspaceView(QWidget):
    selection: Selectable
    wire_in_hand: WireView
    items = []  # list_of_WorkspaceItemView
    wires = []  # list_of_WireView
    widget: QWidget = None

    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("WorkspaceView")

        WorkspaceView.widget = self

        self.vertical_layout = QVBoxLayout()
        self.horizontal_layout = QHBoxLayout()

        self.start_button = StartButtonView(self)
        self.vertical_layout.addWidget(self.start_button, 1)
        self.vertical_layout.addStretch(1)
        self.horizontal_layout.addStretch(1)
        self.horizontal_layout.addLayout(self.vertical_layout)

        self.setLayout(self.horizontal_layout)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        pass

    # def add_item(self, item: WorkspaceItemView) -> None:
    #   self.items.append(item)

    def add_wire(self, wire: WireView) -> None:
        self.wires.append(wire)

    # def delete_item(self, item: WorkspaceItemView) -> None:
    #   self.items.remove(item)

    def delete_wire(self, wire: WireView) -> None:
        self.wires.remove(wire)
