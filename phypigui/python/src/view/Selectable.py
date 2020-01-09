from abc import ABC, abstractmethod


class Selectable(ABC):
    @abstractmethod
    def get_info_widget(self):
        pass

    @abstractmethod
    def delete(self):
        pass
