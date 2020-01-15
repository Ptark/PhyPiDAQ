from typing import NoReturn

from PyQt5.QtGui import QMouseEvent

from .ListItemView import ListItemView


class SensorListItemView(ListItemView):
    def mouseReleaseEvent(self, event: QMouseEvent) -> NoReturn:
        # TODO: visibility
        pass
