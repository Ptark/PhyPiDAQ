from abc import ABC, abstractmethod
from typing import NoReturn


class View(ABC):
    def update(self) -> NoReturn:
        pass
