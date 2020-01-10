from PyQt5.QtGui import QMouseEvent

from python.src.view.item.ListItemView import ListItemView


class SensorListItemView(ListItemView):
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        # TODO: visibility
        pass