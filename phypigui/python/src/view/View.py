from abc import ABC, abstractmethod
from typing import NoReturn


class View(ABC):
    @abstractmethod
    def update(self) -> NoReturn:
        pass
