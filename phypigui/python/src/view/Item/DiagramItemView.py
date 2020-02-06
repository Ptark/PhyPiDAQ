from abc import ABC
from typing import NoReturn

from PyQt5.QtWidgets import QWidget, QLabel

from ..Translator import Translator
from ..InfoBar.InfoBarView import InfoBarView
from ...model.manager.ManagerModel import ManagerModel
from ..DiagramField.DiagramFieldView import DiagramFieldView
from ..DiagramField.DiagramView import DiagramView
from ...model.item.DiagramItem import DiagramItem
from ..Item.WorkspaceItemView import WorkspaceItemView


class DiagramItemView(WorkspaceItemView, ABC):
    """Abstract class for displaying an item of an diagram on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    def __init__(self, parent: QWidget, diagram: 'DiagramEnum'):
        self._model: DiagramItem = diagram.model()
        self._diagram: DiagramView = diagram.diagram(self._model)
        DiagramFieldView.add_diagram(self._diagram)

        super().__init__(parent, diagram.path, self._model.get_input_ids(), [])

        self.__data_text = QLabel()
        self._info_layout.insertWidget(3, self.__data_text)

        Translator.language_changed.signal.connect(self.__update_text)
        self.__update_text()

    def __update_text(self) -> NoReturn:
        self.__data_text.setText(Translator.tr("Daten") + ":")
        self.update_view()

    def update_view(self) -> NoReturn:
        if self.selected:
            text = ""
            for dat in self._model.data:
                text += str(round(dat, 5)) + "\n\t"
            self.__data_text.setText(Translator.tr("Daten") + ":\t" + text)
            InfoBarView.refresh_infobar()

    def delete(self) -> NoReturn:
        DiagramFieldView.delete_diagram(self._diagram)
        ManagerModel.delete_diagram(self._model)
        super().delete()
