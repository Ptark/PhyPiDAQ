from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QPushButton


class Second(QWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


class MaximizeButtonView(QPushButton):

    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(31, 31)
        self.setText("max")
        self.setObjectName("MaximizeButtonView")
       # self.dialog = Second(self)

        #self.clicked.connect(self.on_click())

    def on_click(self):
        # self.dialog.show()
        # for diagram in DiagramFieldView.list
        pass