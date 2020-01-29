from typing import NoReturn, List

from PyQt5.QtCore import Qt, QRect, QPointF
from PyQt5.QtGui import QMouseEvent, QPaintEvent, QResizeEvent, QPainter, QPen
from PyQt5.QtWidgets import QWidget, QGridLayout, QScrollArea, QScrollBar

from ..Item import WorkspaceItemView


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


class WorkspaceView(QWidget):
    selection: 'Selectable' = None
    wire_in_hand: 'WireView' = None

    __items = None
    wires: List['WireView'] = None
    __widget: QWidget = None
    __boundary: QWidget = None
    __main: QWidget = None

    def __init__(self, main: QWidget):
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
        layout = QGridLayout()
        scroll_area = QScrollArea()

        self.__h_scroll_bar = scroll_area.horizontalScrollBar()
        self.__v_scroll_bar = scroll_area.verticalScrollBar()
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        scroll_contents = WorkspaceContentView()
        scroll_contents.setMinimumSize(10000, 10000)
        scroll_contents.setMouseTracking(True)
        WorkspaceView.widget = scroll_contents
        scroll_area.setWidget(scroll_contents)
        layout.addWidget(scroll_area)
        self.setLayout(layout)

        self.__h_scroll_bar.setValue(scroll_contents.width() / 2)
        self.__v_scroll_bar.setValue(scroll_contents.height() / 2)

    def mouseMoveEvent(self, event: QMouseEvent) -> NoReturn:
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
        self.__h_last_pos = 0
        self.__v_last_pos = 0

    def resizeEvent(self, event: QResizeEvent) -> NoReturn:
        w_diff = event.size().width() - event.oldSize().width()
        h_diff = event.size().height() - event.oldSize().height()
        self.__h_scroll_bar.setValue(self.__h_scroll_bar.value() - w_diff / 2)
        self.__v_scroll_bar.setValue(self.__v_scroll_bar.value() - h_diff / 2)

    @staticmethod
    def add_item(item: WorkspaceItemView) -> NoReturn:
        WorkspaceView.items.append(item)

    @staticmethod
    def add_wire(wire: 'WireView') -> NoReturn:
        WorkspaceView.wires.append(wire)
        WorkspaceView.wire_in_hand = wire
        wire.redraw_signal.connect(WorkspaceView.widget.update)

    @staticmethod
    def delete_item(item: WorkspaceItemView) -> NoReturn:
        WorkspaceView.items.remove(item)

    @staticmethod
    def delete_wire(wire: 'WireView') -> NoReturn:
        WorkspaceView.wires.remove(wire)
        if WorkspaceView.wire_in_hand is wire:
            WorkspaceView.wire_in_hand = None

    @staticmethod
    def delete_all() -> NoReturn:
        for item in WorkspaceView.items:
            item.delete()
        for wire in WorkspaceView.wires:
            wire.delete()
        WorkspaceView.items = []
        WorkspaceView.wires = []

    @staticmethod
    def get_widget() -> QWidget:
        return WorkspaceView.widget

    @staticmethod
    def is_on_workspace(widget: QWidget) -> bool:
        widget_rect = QRect(widget.parent().mapToGlobal(widget.pos()), widget.size())
        boundary_rect = QRect(WorkspaceView.main.mapToGlobal(WorkspaceView.boundary.pos()), WorkspaceView.boundary.size())
        return boundary_rect.contains(widget_rect)
