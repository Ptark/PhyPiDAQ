from typing import Final

from PyQt5.QtWidgets import QWidget

from ...model.item.SensorItem import SensorItem
from .WorkspaceItemView import WorkspaceItemView


class SensorItemView(WorkspaceItemView):
    FRAME_PATH: Final[str] = ""  # TODO: frame erstellen

    def __init__(self, parent: QWidget, id: int, icon_path: str):
        super().__init__(parent, id, icon_path)

        self.__model: SensorItem = None
