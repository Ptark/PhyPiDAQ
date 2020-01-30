from abc import ABC
from typing import NoReturn, List

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMenu, QLabel

from ...model.config import ConfigModel, NumOption, BoolOption, FileOption, EnumOption
from .InputView import InputView
from .OutputView import OutputView
from .Draggable import Draggable
from ..Selectable import Selectable
from ..Workspace.WorkspaceView import WorkspaceView
from ..config import ConfigView
from ..EnumTest import EnumTest


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

        #self.__model: ItemModel.ItemModel = None
        self.__inputs: List[InputView] = []
        self.__outputs: List[OutputView] = []

        self.__config_window: ConfigView.ConfigView = None

        self.__lastPos: QPoint = None

        # TODO: Input Output Erstellung überarbeiten
        for i in range(0, num_of_inputs):
            self.__inputs.append(InputView(self))
        for i in range(0, num_of_outputs):
            self.__outputs.append(OutputView(self))

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

    def __context_menu(self, pos: QPoint) -> NoReturn:
        """Creates a context menu at the given position

            Args:
                pos (QPoint): Position at which the menu should appear.
        """
        menu = QMenu()
        menu.addAction(self.tr("Einstellungen"), self.open_config)
        menu.addAction(self.tr("Entfernen"), self.delete)
        menu.exec(self.mapToGlobal(pos))

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
        #self.__config_window = ConfigView.ConfigView(self.__model.name, self.__model.config)
        config = ConfigModel.ConfigModel()
        config.add_num_option(NumOption.NumOption("Num\nOption1", "", 0, -20000.0000, 200000.00000))
        config.add_num_option(NumOption.NumOption("123456789012345678901234567890", "", 13423545, 0, 3234234242, 4))
        config.add_num_option(NumOption.NumOption("NumOption3", "", -234.65672))
        config.add_bool_option(BoolOption.BoolOption("", 'BoolOption2'))
        config.add_bool_option(BoolOption.BoolOption("12345678901234567890123456789012345678901234567890", "", True))
        config.add_enum_option(EnumOption.EnumOption("EnumOption1", EnumTest, "Beschreibung blablabla"))
        config.add_enum_option(EnumOption.EnumOption("", EnumTest, "EnumOption", 2))
        self.__config_window = ConfigView.ConfigView("Item", config)

    def get_info_widget(self) -> QWidget:
        # TODO: infobar erstellen
        widget = QWidget()
        QLabel(self.__class__.__name__, widget)
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
