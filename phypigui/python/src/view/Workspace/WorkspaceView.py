from typing import List

from PyQt5 import QtGui
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

from python.src.view.Item import WorkspaceItemView
from python.src.view.List import ListFieldView
from python.src.view.Selectable import Selectable
from python.src.view.Workspace.StartButtonView import StartButtonView
from python.src.view.Workspace.WireView import WireView


class WorkspaceView(QWidget):
    widget: QWidget = None
    selection: Selectable = None

    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("WorkspaceView")

        WorkspaceView.widget = self
        self.selection = None
        self.wire_in_hand: WireView
        self.items = []  # todo: list_of_WorkspaceItemView circular dependency
        self.__wires: List[WireView] = []

        self.vertical_layout = QVBoxLayout()
        self.horizontal_layout = QHBoxLayout()

        self.start_button = StartButtonView(self)
        self.vertical_layout.addWidget(self.start_button, 1)
        self.vertical_layout.addStretch(1)
        self.horizontal_layout.addStretch(1)
        self.horizontal_layout.addLayout(self.vertical_layout)

        self.setLayout(self.horizontal_layout)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.selection = None

    def add_item(self, item: 'WorkspaceItemView') -> None:  # forward referenced to avoid circular dependency
        self.items.append(item)

    def add_wire(self, wire: WireView) -> None:
        self.wires.append(wire)

    def delete_item(self, item: 'WorkspaceItemView') -> None:  # forward referenced to avoid circular dependency
        self.items.remove(item)
        ListFieldView.ListFieldView.make_visible(item.id)
        for wire in self.__wires:
            if item.id == (wire.output or wire.input):
                self.delete_wire(wire)

    def delete_wire(self, wire: WireView) -> None:
        self.wires.remove(wire)
        # todo: was bedeutet aktualisiert alle WorkspaceItemView, die mit der Verbindung verbunden waren.
