from typing import NoReturn

from PyQt5.QtGui import QMouseEvent

# from ..Workspace.WorkspaceView import WorkspaceView
# from ..Workspace.WireView import WireView
from .InOutView import InOutView


class OutputView(InOutView):
    def mousePressEvent(self, event: QMouseEvent) -> NoReturn:
        """
        if WorkspaceView.wire_in_hand is None:
            WorkspaceView.wire_in_hand = WireView(self.parent().parent())
            WorkspaceView.wire_in_hand.output = self
        """
        super(OutputView, self).mousePressEvent(event)
