from typing import List, NoReturn, Dict

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from PyQt5.QtGui import QCloseEvent, QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout

from ...Exceptions import DiagramMaximumReachedException
from .DiagramView import DiagramView
from .StartButtonView import StartButtonView


class DiagramFieldView(QWidget):
    """ A Diagram field where up to three diagrams would be presented
        Attributes:
            main (QWidget): The main widget.
    """
    __diagram_field: 'DiagramFieldView'

    def __init__(self, parent:QWidget):
        """Initialising of a diagram field view
        Args:
            parent(QWidget)
        """
        super().__init__(parent)
        DiagramFieldView.__diagram_field = self

        self.__list: List[DiagramView] = []
        self.__dialog: Dialog = None
        self.__diagram_layout = QVBoxLayout()
        self.__maximize_button = QPushButton()
        # TODO Es gibt 3 Versionen für das Diagramfeld. Alle zielen zu den Versionen sind gekennzeichnet (Aktiv: v3)
        """                                                                                                 # 2
        self.__group_list: List[QtWidgets.QGroupBox] = []
        self.__group_layouts: List[QtWidgets.QVBoxLayout] = []
        """
        self.__diagram_group: QtWidgets.QGroupBox = QtWidgets.QGroupBox(self)                               # 3
        self.__group_layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout(self.__diagram_group)            # 3
        self.__stretch_widget: QtWidgets.QWidget = QtWidgets.QWidget(self)                                  # 3
        self.__diagram_count: int = 0                                                                       # 3

        self.__maximize_button.clicked.connect(self.__maximize_on_click)
        self.__init_ui()

    def __init_ui(self):
        """ this method initialises the user interface of the diagram field"""
        self.__maximize_button.setFixedSize(31, 31)
        self.__maximize_button.setIcon(QIcon("../resources/images/buttons/maximize.svg"))


        """for n in range(0, 3):                                                                            # 2
            self.__group_list.append(QtWidgets.QGroupBox(self))
            self.__group_list[n].setStyleSheet("QGroupBox { border: 1px solid gray; background: white; }")
            self.__diagram_layout.addWidget(self.__group_list[n])
            self.__group_layouts.append(QtWidgets.QVBoxLayout(self.__group_list[n]))
        """
        self.__diagram_group.setStyleSheet("QGroupBox { border: 1px solid gray; background: white; }")      # 3
        self.__diagram_layout.addWidget(self.__diagram_group)                                               # 3

        buttons = QHBoxLayout()
        buttons.addWidget(StartButtonView(self))
        buttons.addStretch()
        buttons.addWidget(self.__maximize_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(buttons, 1)
        main_layout.addLayout(self.__diagram_layout, 1)
        main_layout.addStretch(0)

        self.setLayout(main_layout)

    def __maximize_on_click(self):
        """ if maximize button clicked open dialog that contains diagrams on screen"""
        self.__dialog = Dialog(self.__list)
        self.__dialog.close_signal.connect(self.__update_diagrams)
        self.__maximize_button.clearFocus()

    @pyqtSlot()
    def __update_diagrams(self):
        """adds diagrams in the diagram field view when maximized window is closed"""
        for diagram in self.__list:
            diagram.resize(280, 350)
            #index_of_diagram: int = self.__list.index(diagram)                                         # 2
            #self.__group_layouts[index_of_diagram].addWidget(diagram, 0, Qt.AlignTop)                  # 2
            #self.__diagram_layout.addWidget(diagram)                                                   # 1
            self.__group_layout.addWidget(diagram)                                                      # 3
        if self.__diagram_count == 1:                                                                   # 3
            self.add_stretch()                                                                          # 3

    @staticmethod
    def add_diagram(diagram: DiagramView) -> NoReturn:
        """adds diagram to list of diagrams & add it to the layout """
        if len(DiagramFieldView.__diagram_field.__list) >= 3:
            raise DiagramMaximumReachedException
        DiagramFieldView.__diagram_field.__list.append(diagram)
        #index_of_diagram: int = DiagramFieldView.__diagram_field.__list.index(diagram)                 # 2
        #DiagramFieldView.__diagram_field.__group_layouts[index_of_diagram].addWidget(diagram)          # 2
        DiagramFieldView.__diagram_field.__diagram_count += 1                                           # 3
        if DiagramFieldView.__diagram_field.__diagram_count == 2:                                       # 3
            DiagramFieldView.__diagram_field.__group_layout.removeWidget(
                DiagramFieldView.__diagram_field.__stretch_widget)                                      # 3
        DiagramFieldView.__diagram_field.__group_layout.addWidget(diagram, 10, Qt.AlignTop)             # 3
        if DiagramFieldView.__diagram_field.__diagram_count == 1:                                       # 3
            DiagramFieldView.add_stretch()                                                              # 3

        #DiagramFieldView.__diagram_field.__diagram_layout.addWidget(diagram)                           # 1

    @staticmethod
    def delete_diagram(diagram: DiagramView) -> NoReturn:
        """delete diagram from list of diagrams and then removes it from layout"""
        #index_of_diagram: int = DiagramFieldView.__diagram_field.__list.index(diagram)                 # 2
        #DiagramFieldView.__diagram_field.__group_layouts[index_of_diagram].removeWidget(diagram)       # 2
        DiagramFieldView.__diagram_field.__list.remove(diagram)
        DiagramFieldView.__diagram_field.__diagram_count -= 1                                           # 3
        DiagramFieldView.__diagram_field.__group_layout.removeWidget(diagram)                           # 3
        if DiagramFieldView.__diagram_field.__diagram_count == 1:                                       # 3
            DiagramFieldView.add_stretch()                                                              # 3
        #DiagramFieldView.__diagram_field.__diagram_layout.removeWidget(diagram)                        # 1
        diagram.close()

    @staticmethod
    def add_stretch() -> NoReturn:
        DiagramFieldView.__diagram_field.__group_layout.addWidget(
            DiagramFieldView.__diagram_field.__stretch_widget, 10, Qt.AlignBottom)

class Dialog(QWidget):
    close_signal = pyqtSignal()

    def __init__(self, list: List[DiagramView]):
        """initialising of he dialog that will be popped when maximized button is clicked"""
        super().__init__()

        self.__init_ui(list)

    def __init_ui(self, list: List[DiagramView]):
        """initialises the user interface of the dialog window"""
        minimize_button = QtWidgets.QPushButton()
        minimize_button.setIcon(QIcon("../resources/images/buttons/minimize.svg"))
        minimize_button.setFixedSize(31, 31)
        minimize_button.clicked.connect(self.__minimize_on_click)

        horizontal_layout = QHBoxLayout()
        for diagram in list:
            horizontal_layout.addWidget(diagram)

        central_layout = QGridLayout()
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(horizontal_layout)
        central_layout.addWidget(central_widget, 1, 0)
        central_layout.addWidget(minimize_button, 0, 1)

        self.setLayout(central_layout)

        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.showMaximized()

    @pyqtSlot()
    def __minimize_on_click(self):
        """method to close dialog when minimize button is clicked"""
        self.close()

    def closeEvent(self, event: QCloseEvent):
        """method to signal that the dialog is closed """
        self.close_signal.emit()
