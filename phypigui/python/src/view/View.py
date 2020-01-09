from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def update(self):
        pass
