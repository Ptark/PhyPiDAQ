from abc import ABC, abstractmethod
from typing import NoReturn, List

from PyQt5.QtCore import QPoint, Qt, pyqtSlot
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMenu, QLabel

from ..InfoBar.InfoBarView import InfoBarView
from ..InfoBar.SettingsButtonView import SettingsButtonView
from ...model.workspace.WorkspaceModel import WorkspaceModel
from ..Translator import Translator
from ...model.item.ItemModel import ItemModel
from ...model.config.ConfigModel import ConfigModel
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

    def __init__(self, parent: QWidget, icon_path: str, model_input_ids: List[int], model_output_ids: List[int], unique: bool = False):
        WorkspaceView.add_item(self, unique)

        Draggable.__init__(self, parent, icon_path)
        Selectable.__init__(self)

        self._model: ItemModel
        self._model.attach(self)

        self.__inputs: List[InputView] = []
        self.__outputs: List[OutputView] = []

        self.__config_window: ConfigView.ConfigView = None
        self.__info_widget: QWidget = QWidget()
        self._info_layout: QVBoxLayout = QVBoxLayout()
        self.__name = QLabel()
        self.__desc = QLabel()
        self.__data_text = QLabel()

        self.__lastPos: QPoint = None

        for input in model_input_ids:
            self.__inputs.append(InputView(self, input))
        for output in model_output_ids:
            self.__outputs.append(OutputView(self, output))

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

        self.__desc.setWordWrap(True)

        self._info_layout.setContentsMargins(5, 5, 5, 5)
        self._info_layout.setSpacing(5)

        self._info_layout.addWidget(self.__name)
        self._info_layout.addSpacing(5)
        self._info_layout.addWidget(self.__desc)
        self._info_layout.addWidget(self.__data_text)
        self._info_layout.addStretch()

        self.__info_widget.setLayout(self._info_layout)

    def __context_menu(self, pos: QPoint) -> NoReturn:
        """Creates a context menu at the given position

            Args:
                pos (QPoint): Position at which the menu should appear.
        """
        menu = QMenu()
        menu.addAction(Translator.tr("Einstellungen"), self.open_config).setEnabled(not self._model.config.empty)
        menu.addAction(Translator.tr("Entfernen"), self.delete)
        menu.exec(self.mapToGlobal(pos))

    def __update_text(self):
        self.setToolTip(Translator.tr(self._model.name))
        self.__name.setText(Translator.tr(self._model.name))
        self.__desc.setText(Translator.tr(self._model.description) + ".")
        self.__data_text.setText(Translator.tr("Daten") + ":")
        self.update_view()

    @pyqtSlot(ConfigModel)
    def __set_config_data(self, config: ConfigModel) -> NoReturn:
        self._model.set_config(config)

    def _on_click(self) -> NoReturn:
        if WorkspaceView.wire_in_hand is None:
            self.selected = not self.selected

    def _select(self) -> NoReturn:
        SettingsButtonView.set_enabled(not self._model.config.empty if self.selected else False)

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
        self.__config_window.set_data.connect(self.__set_config_data)

    def get_info_widget(self) -> QWidget:
        return self.__info_widget

    def delete(self) -> NoReturn:
        WorkspaceView.delete_item(self)
        WorkspaceModel.delete_item(self._model.id)
        super().delete()
        for inout in (self.__inputs + self.__outputs):
            inout.delete_all_wires()
        self.close()

    def update_view(self) -> NoReturn:
        if self.selected:
            str_data = list(map(lambda x: str(round(x, 5)), self.get_data()))
            data_units = [str_data[i] + ' ' + self.get_units()[i] for i in range(len(str_data))]
            text = ""
            for s in data_units:
                text += s + "\n\t"
            self.__data_text.setText(Translator.tr("Daten") + ":\t" + text)

    @abstractmethod
    def get_data(self) -> List[float]:
        pass

    @abstractmethod
    def get_units(self) -> List[str]:
        pass

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
