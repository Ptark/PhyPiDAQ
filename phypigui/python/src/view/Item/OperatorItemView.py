from abc import ABC
from typing import NoReturn

from PyQt5.QtWidgets import QWidget, QLabel

from ..Translator import Translator
from ..InfoBar.InfoBarView import InfoBarView
from ...model.item.OperatorItem import OperatorItem, AdditionOperatorItem, SubtractionOperatorItem, \
    MultiplicationOperatorItem, DivisionOperatorItem, AbsoluteOperatorItem
from .WorkspaceItemView import WorkspaceItemView


operator_path = "../resources/images/items/operator/"


class OperatorItemView(WorkspaceItemView, ABC):
    """Abstract class for displaying an item of an operator on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    def __init__(self, parent: QWidget):
        self._model: OperatorItem

        super().__init__(parent, self._model.get_input_ids(), self._model.get_output_ids())

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


class AdditionOperatorItemView(OperatorItemView):
    """Class for displaying an item of an addition operator on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: str = operator_path + 'addition.svg'

    def __init__(self, parent: QWidget):
        self._model: AdditionOperatorItem = AdditionOperatorItem()

        super().__init__(parent)


class SubtractionOperatorItemView(OperatorItemView):
    """Class for displaying an item of an subtraction operator on the workspace

        Attributes (QWidget):
            parent: A parent widget.
    """
    icon_path: str = operator_path + 'subtraction.svg'

    def __init__(self, parent: QWidget):
        self._model: SubtractionOperatorItem = SubtractionOperatorItem()

        super().__init__(parent)


class MultiplicationOperatorItemView(OperatorItemView):
    """Class for displaying an item of an multiplication operator on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: str = operator_path + 'multiplication.svg'

    def __init__(self, parent: QWidget):
        self._model: MultiplicationOperatorItem = MultiplicationOperatorItem()

        super().__init__(parent)


class DivisionOperatorItemView(OperatorItemView):
    """Class for displaying an item of an division operator on the workspace

        Attributes:
            parent: A parent widget.
    """
    icon_path: str = operator_path + 'division.svg'

    def __init__(self, parent: QWidget):
        self._model: DivisionOperatorItem = DivisionOperatorItem()

        super().__init__(parent)


class AbsoluteOperatorItemView(OperatorItemView):
    """Class for displaying an item of an absolute operator on the workspace

        Attributes:
            parent (QWidget): A parent widget.
    """
    icon_path: str = operator_path + 'absolute.svg'

    def __init__(self, parent: QWidget):
        self._model: AbsoluteOperatorItem = AbsoluteOperatorItem()

        super().__init__(parent)
