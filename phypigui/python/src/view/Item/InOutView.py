from abc import ABC

from PyQt5.QtWidgets import QWidget

from ..View import View
from .WorkspaceItemView import WorkspaceItemView


class InOutView(ABC, QWidget, View):
    def __init__(self, parent: QWidget, item: WorkspaceItemView):
        super().__init__(parent)

        self.__item: WorkspaceItemView = item
