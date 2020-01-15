from typing import Final

from PyQt5.QtWidgets import QWidget

from ...model.item import DiagramItem
from ..DiagramField.DiagramView import DiagramView
from ..Item.WorkspaceItemView import WorkspaceItemView


class DiagramItemView(WorkspaceItemView):
    FRAME_PATH: Final[str] = ""  # TODO: frame erstellen

    def __init__(self, parent: QWidget, id: int, icon_path: str):
        super().__init__(parent, id, icon_path)

        self.__model: DiagramItem = None
        self.__diagram: DiagramView = DiagramView()
