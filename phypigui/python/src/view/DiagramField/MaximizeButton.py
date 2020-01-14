from PyQt5.QtWidgets import QPushButton


class MaximizeButtonView(QPushButton):

    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(31, 31)
        self.setText("max")
        self.setObjectName("MaximizeButtonView")

    def on_click(self):
        pass
