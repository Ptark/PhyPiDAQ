from abc import ABC
from typing import NoReturn

from PyQt5.QtWidgets import QWidget, QLabel

from ..Translator import Translator
from ..InfoBar.InfoBarView import InfoBarView
from phypigui.python.src.model.item.OperatorItems.OperatorItem import OperatorItem
from .WorkspaceItemView import WorkspaceItemView


class OperatorItemView(WorkspaceItemView, ABC):
    """Abstract class for displaying an item of an operator on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    def __init__(self, parent: QWidget, operator: 'OperatorEnum'):
        self._model: OperatorItem = operator.model()

        super().__init__(parent, operator.path, self._model.get_input_ids(), self._model.get_output_ids())

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
            for dat in self._model.get_data():
                text += str(round(dat, 5)) + "\n\t"
            self.__data_text.setText(Translator.tr("Daten") + ":\t" + text)
            InfoBarView.refresh_infobar()
