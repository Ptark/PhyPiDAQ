from abc import ABC, abstractmethod

from PyQt5.QtWidgets import QWidget


class Selectable(ABC):
    @abstractmethod
    def get_info_widget(self) -> QWidget:
        pass

    @abstractmethod
    def delete(self) -> None:
        pass
