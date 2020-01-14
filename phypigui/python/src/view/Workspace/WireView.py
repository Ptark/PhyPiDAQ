from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget


class WireView(QPainter):
    # output: OutputView
    # input: InputView

    def redraw(self):
        pass

    def mousePressEvent(self, event) -> None:
        pass

    def mouseMoveEvent(self, event) -> None:
        pass

    def get_info_widget(self) -> QWidget:
        pass

    def delete(self) -> None:
        pass

