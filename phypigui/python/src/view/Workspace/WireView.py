from typing import NoReturn

from PyQt5.QtCore import pyqtSignal, QObject, QPoint
from PyQt5.QtWidgets import QWidget, QMenu, QLabel, QVBoxLayout

from ...Exceptions import IDNotFound
from ..Selectable import Selectable
from .WorkspaceView import WorkspaceView
from ..Translator import Translator
from ...model.workspace.WorkspaceModel import WorkspaceModel


class WireViewMeta(type(Selectable), type(QObject)):
    pass


class WireView(Selectable, QObject, metaclass=WireViewMeta):
    """This class represents a Wire connecting two WorkspaceItemViews """
    __CLICKABLE_MARGIN: int = 1400
    redraw_signal = pyqtSignal()
    deletion_signal = pyqtSignal(QObject)

    def __init__(self, output: QPoint, input: QPoint, output_id: int):
        """Initializes a Wire
            Args:
                output(QPoint): the output from which the connection originates.
                input(QPoint): the input to which the connection points.
                output_id(int): The identification number for the output of the wire
        """
        Selectable.__init__(self)
        QObject.__init__(self)

        self.__output: QPoint = output
        self.__input: QPoint = input
        self.__output_id: int = output_id
        self.__input_id: int = None

        self.__info_widget: QWidget = QWidget()
        self.__input_label: QLabel = QLabel()
        self.__output_label: QLabel = QLabel()

        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        """
        Initializes the user interface for the wire
        """
        info_layout = QVBoxLayout()
        info_layout.setContentsMargins(5, 5, 5, 5)
        info_layout.setSpacing(5)

        info_layout.addWidget(QLabel(Translator.tr("Verbindung")))
        info_layout.addSpacing(5)
        info_layout.addWidget(self.__output_label)
        info_layout.addWidget(self.__input_label)
        info_layout.addStretch()

        self.__info_widget.setLayout(info_layout)

    @property
    def output(self) -> QPoint:
        """Position of the connected output"""
        return self.__output

    @property
    def input(self) -> QPoint:
        """Position of the connected input"""
        return self.__input

    def connect(self, input_id: int) -> NoReturn:
        """connect two items with the wire"""
        self.__input_id = input_id
        WorkspaceModel.connect(input_id, self.__output_id)

    def redraw(self, output: QPoint = None, input: QPoint = None) -> NoReturn:
        """Updates the position of the connected in- and/or output

            Args:
                output (QPoint): The new output position. If not given, output position does not change.
                input (QPoint): The new input position. If not given, input position does not change.
        """
        if output is not None:
            self.__output = output
        if input is not None:
            self.__input = input

        self.redraw_signal.emit()

    def point_on_line(self, point: QPoint) -> bool:
        """Checks if the given point is on the wire

            Args:
                point (QPoint): Thw point to check.

            Returns:
                bool: Returns true when the given point is on the wire.
        """
        p1_x = self.__output.x()
        p1_y = self.__output.y()
        p2_x = self.__input.x()
        p2_y = self.__input.y()
        p_x = point.x()
        p_y = point.y()

        cross_product = (p_y - p1_y) * (p2_x - p1_x) - (p_x - p1_x) * (p2_y - p1_y)
        if abs(cross_product) > WireView.__CLICKABLE_MARGIN:
            return False

        dot_product = (p_x - p1_x) * (p2_x - p1_x) + (p_y - p1_y)*(p2_y - p1_y)
        if dot_product < 0:
            return False

        squared_length = (p2_x - p1_x)*(p2_x - p1_x) + (p2_y - p1_y)*(p2_y - p1_y)
        if dot_product > squared_length:
            return False

        return True

    def open_context_menu(self, pos: QPoint) -> NoReturn:
        """Creates a context menu at the given position

            Args:
                pos (QPoint): Position at which the menu should appear.
        """
        menu = QMenu()
        menu.addAction(Translator.tr("Entfernen"), self.delete)
        menu.exec(pos)

    def _update_selected_view(self) -> NoReturn:
        """updates the selected view"""
        self.redraw()

    def get_info_widget(self) -> QWidget:
        """show the input and output of wire in info bar"""

        output_name = WorkspaceModel.get_output_item_name(self.__output_id)
        input_name = WorkspaceModel.get_input_item_name(self.__input_id)

        self.__output_label.setText(Translator.tr("Ausgang") + ": " + output_name)
        self.__input_label.setText(Translator.tr("Eingang") + ": " + input_name)

        return self.__info_widget

    def open_config(self) -> NoReturn:
        """configuration of the Wire can not be opened because there is nothing to set in WireView"""
        pass

    def delete(self) -> NoReturn:
        """deletes the wire and sends a message then deletes wire from workspaceView """
        WorkspaceView.delete_wire(self)
        if self.__input_id is not None:
            try:
                WorkspaceModel.delete_connection(self.__input_id)
            except IDNotFound:
                pass

        super().delete()
        self.deletion_signal.emit(self)
        self.redraw()
