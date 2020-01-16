from PyQt5 import QtGui
from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QPushButton


class Second(QWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


class MaximizeButtonView(QPushButton):
    __icon_source = "../resources/images/buttons/maxbutton.png"

    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(31, 31)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(self.__icon_source))
        self.setIcon(self.icon)
       # self.dialog = Second(self)

        #self.clicked.connect(self.on_click())

    def on_click(self):
        # self.dialog.show()
        # for diagram in DiagramFieldView.list

        pass