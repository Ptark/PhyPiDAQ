from copy import copy
from typing import NoReturn, List

from PyQt5.QtCore import Qt, QRect, QPointF
from PyQt5.QtGui import QMouseEvent, QPaintEvent, QResizeEvent, QPainter, QPen, QWheelEvent
from PyQt5.QtWidgets import QWidget, QGridLayout, QScrollArea, QScrollBar

from ...Exceptions import DuplicateWorkspaceItem


class WorkspaceContentView(QWidget):
    def paintEvent(self, event: QPaintEvent) -> NoReturn:
        rect: QRect = event.rect()
        spacing = 25

        paint = QPainter()
        paint.begin(self)
        for i in range(rect.x(), rect.x() + rect.width() + spacing, spacing):
            for j in range(rect.y(), rect.y() + rect.height() + spacing, spacing):
                paint.drawPoint(QPointF(int(i / spacing) * spacing, int(j / spacing) * spacing))

        pen = QPen(Qt.black, 3, Qt.SolidLine, Qt.RoundCap)
        for wire in WorkspaceView.wires:
            pen.setColor(Qt.blue if wire.selected else Qt.black)
            paint.setPen(pen)
            paint.drawLine(wire.output, wire.input)
        paint.end()

    def mousePressEvent(self, event: QMouseEvent) -> NoReturn:
        for wire in WorkspaceView.wires:
            if wire.point_on_line(event.pos()) and WorkspaceView.wire_in_hand is None:
                if event.buttons() == Qt.LeftButton:
                    wire.selected = not wire.selected
                elif event.buttons() == Qt.RightButton:
                    wire.open_context_menu(event.globalPos())
                event.ignore()
                return

        if event.buttons() == Qt.LeftButton:
            if WorkspaceView.wire_in_hand is not None:
                WorkspaceView.wire_in_hand.delete()

        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> NoReturn:
        if WorkspaceView.wire_in_hand is not None:
            WorkspaceView.wire_in_hand.redraw(input=event.pos())

        super().mouseMoveEvent(event)


class WorkspaceScrollView(QScrollArea):
    def __init__(self):
        super().__init__()
        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        scroll_contents = WorkspaceContentView()
        scroll_contents.setMinimumSize(10000, 10000)
        scroll_contents.setMouseTracking(True)
        WorkspaceView.widget = scroll_contents
        self.setWidget(scroll_contents)

        self.horizontalScrollBar().setValue(scroll_contents.width() / 2)
        self.verticalScrollBar().setValue(scroll_contents.height() / 2)

    def wheelEvent(self, event: QWheelEvent) -> NoReturn:
        event.ignore()


class WorkspaceView(QWidget):
    selection: 'Selectable' = None
    wire_in_hand: 'WireView' = None

    __items = None
    wires: List['WireView'] = None
    __widget: QWidget = None
    __boundary: QWidget = None
    __main: QWidget = None

    def __init__(self, main: QWidget):
        """initializes the WorkspaceView
        Args:
            main(QWidget): the main widget
        """
        super().__init__(main)

        WorkspaceView.boundary = self
        WorkspaceView.main = main
        WorkspaceView.items = []
        WorkspaceView.wires = []

        self.__h_scroll_bar: QScrollBar = None
        self.__v_scroll_bar: QScrollBar = None
        self.__h_last_pos = 0
        self.__v_last_pos = 0

        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        """initializes the user interface of the workspace"""
        layout = QGridLayout()
        scroll_area = WorkspaceScrollView()

        self.__h_scroll_bar = scroll_area.horizontalScrollBar()
        self.__v_scroll_bar = scroll_area.verticalScrollBar()

        layout.addWidget(scroll_area)
        self.setLayout(layout)

    def mouseMoveEvent(self, event: QMouseEvent) -> NoReturn:
        """
         Args:
            event(QMouseEvent): an event of the mouse movement
        """
        if event.buttons() == Qt.LeftButton:
            if self.__h_last_pos == 0:
                self.__h_last_pos = event.pos().x()

            h_distance = self.__h_last_pos - event.pos().x()
            self.__h_scroll_bar.setValue(self.__h_scroll_bar.value() + h_distance)

            self.__h_last_pos = event.pos().x()

            if self.__v_last_pos == 0:
                self.__v_last_pos = event.pos().y()

            v_distance = self.__v_last_pos - event.pos().y()
            self.__v_scroll_bar.setValue(self.__v_scroll_bar.value() + v_distance)

            self.__v_last_pos = event.pos().y()

    def mouseReleaseEvent(self, event: QMouseEvent) -> NoReturn:
        """on mouse release event sets horizontal and vertical position to zero
            Args:
                event(QMouseEvent): an event of the mouse realse
        """
        self.__h_last_pos = 0
        self.__v_last_pos = 0

    def resizeEvent(self, event: QResizeEvent) -> NoReturn:
        w_diff = event.size().width() - event.oldSize().width()
        h_diff = event.size().height() - event.oldSize().height()
        self.__h_scroll_bar.setValue(self.__h_scroll_bar.value() - w_diff / 2)
        self.__v_scroll_bar.setValue(self.__v_scroll_bar.value() - h_diff / 2)

    @staticmethod
    def add_item(item: 'WorkspaceItemView', unique: bool = False) -> NoReturn:
        """adds item to workspace
            Args:
                item: item to be added on workspace
                unique(bool): true if item is unique, false otherwise
        """
        if unique:
            for i in WorkspaceView.items:
                if i.__class__ is item.__class__:
                    raise DuplicateWorkspaceItem
        WorkspaceView.items.append(item)

    @staticmethod
    def add_wire(wire: 'WireView') -> NoReturn:
        """adds wire to Workspace
            Args:
                wire(WireView): wire to be added on workspace
        """
        WorkspaceView.wires.append(wire)
        WorkspaceView.wire_in_hand = wire
        wire.redraw_signal.connect(WorkspaceView.widget.update)

    @staticmethod
    def delete_item(item: 'WorkspaceItemView') -> NoReturn:
        """deletes item from workspace
            Args:
                item(WorkspaceView): the item to be deleted from workspace
        """
        WorkspaceView.items.remove(item)

    @staticmethod
    def delete_wire(wire: 'WireView') -> NoReturn:
        """deletes wire from workspace
           Args:
               wire(WireView): the wire to be deleted from workspace
        """
        WorkspaceView.wires.remove(wire)
        if WorkspaceView.wire_in_hand is wire:
            WorkspaceView.wire_in_hand = None

    @staticmethod
    def delete_all() -> NoReturn:
        """deletes all items and wires on workspace"""
        for item in copy(WorkspaceView.items):
            item.delete()
        for wire in copy(WorkspaceView.wires):
            wire.delete()
        WorkspaceView.items = []
        WorkspaceView.wires = []

    @staticmethod
    def get_widget() -> QWidget:
        """a getter method for the workspace widget"""
        return WorkspaceView.widget

    @staticmethod
    def is_on_workspace(widget: QWidget) -> bool:
        """checks if the widget is currently on the workspace
           Args:
               widget(QWidget): the widget to test_output if its on workspaceview
        """
        widget_rect = QRect(widget.parent().mapToGlobal(widget.pos()), widget.size())
        boundary_rect = QRect(WorkspaceView.main.mapToGlobal(WorkspaceView.boundary.pos()), WorkspaceView.boundary.size())
        return boundary_rect.contains(widget_rect)
