from abc import ABC
from typing import NoReturn


class View(ABC):
    def update(self) -> NoReturn:
        pass
