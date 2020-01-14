from PyQt5 import QtCore
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget

from python.src.view.Selectable import Selectable
from python.src.view.Workspace.StartButtonView import StartButtonView
from python.src.view.Workspace.WireView import WireView


class WorkspaceView(QWidget):
    selection: Selectable
    wire_in_hand: WireView
    items = []  # list_of_WorkspaceItemView
    wires = []  # list_of_WireView

    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(190, 40, 401, 391))
        self.setObjectName("WorkspaceView")

        StartButtonView(self)

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
