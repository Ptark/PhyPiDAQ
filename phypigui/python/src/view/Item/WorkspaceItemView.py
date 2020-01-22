from abc import ABC
from typing import NoReturn, List

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMenu

# from ...model.item.ItemModel import ItemModel
from .InputView import InputView
from .OutputView import OutputView
from .Draggable import Draggable
from ..Selectable import Selectable
from ..Workspace.WorkspaceView import WorkspaceView


class WorkspaceItemView(Draggable, Selectable, ABC):
    icon_path: str

    def __init__(self, main: QWidget, num_of_inputs: int = 0, num_of_outputs: int = 0):
        super().__init__(main, self.icon_path)

        self.__id: int = 0  # WorkspaceView.add_item(self)
        # self.__model: ItemModel = None
        self.__selected: bool = False
        self.__inputs: List[InputView] = []
        self.__outputs: List[OutputView] = []

        self.__lastPos: QPoint = None

        for i in range(0, num_of_inputs):
            self.__inputs.append(InputView())
        for i in range(0, num_of_outputs):
            self.__outputs.append(OutputView())

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.__context_menu)

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

    @property
    def id(self) -> int:
        return self.__id

    @property
    def selected(self) -> bool:
        return self.__selected

    @selected.setter
    def selected(self, new_selected: bool) -> NoReturn:
        if self.__selected == new_selected:
            return

        self.__selected = new_selected

        if self.selected:
            if WorkspaceView.selection is not None:
                WorkspaceView.selection.selected = False
            border = "blue"
            background = "#CCCCEE"
            WorkspaceView.selection = self
        else:
            border = "black"
            background = "#CCCCCC"
            WorkspaceView.selection = None

        self.setStyleSheet("""
            QFrame {
                border: 2px solid """ + border + """;
                border-radius: 5px;
                background-color: """ + background + """;
                }
            """)

    def __context_menu(self, pos: QPoint) -> NoReturn:
        menu = QMenu()
        # menu.addAction(self.tr("Einstellungen"), self.open_settings)
        menu.addAction(self.tr("Entfernen"), self.delete)
        menu.exec(self.mapToGlobal(pos))

    def _on_click(self):
        self.selected = not self.selected

    def get_info_widget(self) -> QWidget:
        return QWidget()  # TODO: infobar system

    def delete(self) -> NoReturn:
        # WorkspaceView.delete_item(self)
        if WorkspaceView.selection is self:
            WorkspaceView.selection = None
        self.close()

    def mousePressEvent(self, event: QMouseEvent) -> NoReturn:
        if event.buttons() == Qt.LeftButton:
            self.__lastPos = self.pos()
            self._save_position(event)
            self.raise_()

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
