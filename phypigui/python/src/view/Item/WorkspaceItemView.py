from abc import ABC
from typing import NoReturn, List

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMenu, QLabel

from ..Translator import Translator
from ...model.item.ItemModel import ItemModel
from .InputView import InputView
from .OutputView import OutputView
from .Draggable import Draggable
from ..Selectable import Selectable
from ..Workspace.WorkspaceView import WorkspaceView
from ..config.ConfigView import ConfigView


class WorkspaceItemView(Draggable, Selectable, ABC):
    """Abstract class for displaying an item on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: str

    def __init__(self, parent: QWidget, num_of_inputs: int = 0, num_of_outputs: int = 0, unique: bool = False):
        WorkspaceView.add_item(self, unique)

        Draggable.__init__(self, parent, self.icon_path)
        Selectable.__init__(self)

        self._model: ItemModel
        self.__inputs: List[InputView] = []
        self.__outputs: List[OutputView] = []

        self.__config_window: ConfigView.ConfigView = None

        self.__lastPos: QPoint = None

        for i in range(0, num_of_inputs):
            self.__inputs.append(InputView(self))
        for i in range(0, num_of_outputs):
            self.__outputs.append(OutputView(self))

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.__context_menu)
        Translator.language_changed.signal.connect(self.__update_text)

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

        self.__update_text()

    def __context_menu(self, pos: QPoint) -> NoReturn:
        """Creates a context menu at the given position

            Args:
                pos (QPoint): Position at which the menu should appear.
        """
        menu = QMenu()
        menu.addAction(Translator.tr("Einstellungen"), self.open_config)
        menu.addAction(Translator.tr("Entfernen"), self.delete)
        menu.exec(self.mapToGlobal(pos))

    def __update_text(self):
        self.setToolTip(Translator.tr(self._model.name))

    def _on_click(self) -> NoReturn:
        if WorkspaceView.wire_in_hand is None:
            self.selected = not self.selected

    def _update_selected_view(self) -> NoReturn:
        if self.selected:
            border = "blue"
            background = "#CCCCEE"
        else:
            border = "black"
            background = "#CCCCCC"

        self.setStyleSheet("""
            QFrame {
                border: 2px solid """ + border + """;
                border-radius: 5px;
                background-color: """ + background + """;
                }
            """)

    def open_config(self) -> NoReturn:
        """Creates and opens the settings-window for this Item"""
        self.__config_window = ConfigView(self._model.name, self._model.config)

    def get_info_widget(self) -> QWidget:
        widget = QWidget()

        name = QLabel(Translator.tr(self._model.name))
        desc = QLabel(Translator.tr(self._model.description))
        desc.setWordWrap(True)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        layout.addWidget(name)
        layout.addWidget(desc)
        layout.addStretch()

        widget.setLayout(layout)
        return widget

    def delete(self) -> NoReturn:
        WorkspaceView.delete_item(self)
        super().delete()
        for inout in (self.__inputs + self.__outputs):
            inout.delete_all_wires()
        self.close()

    def mousePressEvent(self, event: QMouseEvent) -> NoReturn:
        if event.buttons() == Qt.LeftButton:
            self.__lastPos = self.pos()
            self._save_position(event.globalPos())
            self.raise_()

    def mouseMoveEvent(self, event: QMouseEvent) -> NoReturn:
        if event.buttons() == Qt.LeftButton:
            self._move_item(event.globalPos())
            for inout in (self.__inputs + self.__outputs):
                inout.redraw_wires()

    def mouseReleaseEvent(self, event: QMouseEvent) -> NoReturn:
        if not WorkspaceView.is_on_workspace(self):
            self.move(self.__lastPos)
            for inout in (self.__inputs + self.__outputs):
                inout.redraw_wires()
            return

        super().mouseReleaseEvent(event)
