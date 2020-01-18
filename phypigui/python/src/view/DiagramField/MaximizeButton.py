from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout

from python.src.view import MainWindow
from python.src.view.DiagramField import DiagramFieldView, DiagramView


class Dialog(QMainWindow):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.central_widget = QtWidgets.QWidget(self)

        screen = QtWidgets.QDesktopWidget().screenGeometry(-1)
        window_width = screen.width()
        window_height = screen.height()
        self.resize(window_width, window_height)
        self.central_widget.setGeometry(0, 0, self.width(), self.height())

        self.horizontal_layout = QHBoxLayout()

        self.central_widget.setLayout(self.horizontal_layout)

    def add_diagram(self, diagram: DiagramView):
        self.horizontal_layout.addWidget(diagram)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        for diagram in DiagramFieldView.DiagramFieldView.list:  # remove diagrams from right side
            DiagramFieldView.DiagramFieldView.vertical_layout.removeWidget(diagram)
        for diagram in DiagramFieldView.DiagramFieldView.list:  # adds diagrams to right side
            DiagramFieldView.DiagramFieldView.vertical_layout.addWidget(diagram)


class MaximizeButtonView(QPushButton):
    __icon_source = "../resources/images/buttons/maxbutton.png"

    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(31, 31)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(self.__icon_source))
        self.setIcon(self.icon)
        self.dialog = Dialog(self)
        self.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):  # todo: fix minimize
        for diagram in DiagramFieldView.DiagramFieldView.list:
            self.dialog.add_diagram(diagram)
        self.dialog.show()
