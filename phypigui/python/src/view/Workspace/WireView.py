from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget


from python.src.view.InfoBar.InfoBarView import InfoBarView
from python.src.view.Item.InputView import InputView
from python.src.view.Item.OutputView import OutputView
from python.src.view.Workspace import WorkspaceView


class WireView(QPainter):
    output: OutputView
    input: InputView

    def __init__(self,parent):
        super().__init__(parent)
        self.output: OutputView
        self.input: InputView

    def redraw(self):
        pass

    def mousePressEvent(self, event) -> None:
        WorkspaceView.selection = self
        InfoBarView.refresh_infobar()

    def mouseMoveEvent(self, event) -> None: #void ist output noch NULL, so folgt die Spitze der Verbindung dem Mauszeiger, ansonsten tut sich garnichts.
        pass

    def get_info_widget(self) -> QWidget:   #In WireView wird ein QWidget mit dem Ein- und Ausgang zurückgegeben.
        pass

    def delete(self) -> None:
        WorkspaceView.WorkspaceView.delete_wire(self)
