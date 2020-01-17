from typing import NoReturn, List

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget, QVBoxLayout

# from ...model.item.ItemModel import ItemModel
from .InputView import InputView
from .OutputView import OutputView
from .Draggable import Draggable
from ..Selectable import Selectable
from ..Workspace.WorkspaceView import WorkspaceView


class WorkspaceItemView(Draggable, Selectable):
    icon_path: str

    def __init__(self, main: QWidget, num_of_inputs: int, num_of_outputs: int):
        super().__init__(main, self.icon_path)

        self.__lastPos: QPoint = None

        # self.__model: ItemModel = None
        # self.__selected: bool = False
        self.__inputs: List[InputView] = []
        self.__outputs: List[OutputView] = []

        for i in range(0, num_of_inputs):
            self.__inputs.append(InputView())
        for i in range(0, num_of_outputs):
            self.__outputs.append(OutputView())

        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        in_layout = QVBoxLayout()
        for input in self.__inputs:
            in_layout.addWidget(input)
        in_widget = QWidget(self)
        in_widget.setFixedSize(30, 60)
        in_widget.setLayout(in_layout)
        in_widget.move(-19, 0)

        out_layout = QVBoxLayout()
        for output in self.__outputs:
            out_layout.addWidget(output)
        out_widget = QWidget(self)
        out_widget.setFixedSize(20, 60)
        out_widget.setLayout(out_layout)
        out_widget.move(101, 0)

    def _on_click(self):
        # WorkspaceView.set_selected_item(self)  # TODO: selection system
        self.setStyleSheet("""
            QFrame {
                border: 2px solid blue;
                border-radius: 5px;
                background-color: #CCCCEE;
                }
            """)

    def get_info_widget(self) -> QWidget:
        pass  # TODO: infobar system

    def delete(self) -> NoReturn:
        # WorkspaceView.delete_item(self)
        self.close()

    def mousePressEvent(self, event: QMouseEvent) -> NoReturn:
        if event.buttons() == Qt.LeftButton:
            self.__lastPos = self.pos()
            self._save_position(event)

        # for testing:  TODO: deletion system
        if event.buttons() == Qt.RightButton:
            self.delete()
            return

        super(WorkspaceItemView, self).mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> NoReturn:
        if event.buttons() == Qt.LeftButton:
            self._move_item(event)

        super(WorkspaceItemView, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> NoReturn:
        if not WorkspaceView.widget.geometry().contains(self.geometry()):
            self.move(self.__lastPos)
            return

        super(WorkspaceItemView, self).mouseReleaseEvent(event)
