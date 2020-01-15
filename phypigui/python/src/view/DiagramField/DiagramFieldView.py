from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from python.src.view.DiagramField.DiagramView import DiagramView
from python.src.view.DiagramField.MaximizeButton import MaximizeButtonView


class DiagramFieldView(QWidget):
    list = []  # List of DiagramView

    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("DiagramFieldView")

        vertical_layout = QVBoxLayout()
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addStretch(2)
        horizontal_layout.addWidget(MaximizeButtonView(self))
        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addWidget(DiagramView(self))
        vertical_layout.addWidget(DiagramView(self))
        # vertical_layout.addWidget(DiagramView(self))

        self.setLayout(vertical_layout)

        """for diagram in self.list:
                vertical_layout.addWidget(diagram)
        """

    def add_diagram(self, diagram: DiagramView) -> None:
        list.append(diagram)

    def delete_diagram(self, diagram: DiagramView) -> None:
        list.remove(diagram)

