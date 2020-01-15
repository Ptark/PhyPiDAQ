from abc import ABC, abstractmethod
from typing import NoReturn


class View:
    def update(self) -> NoReturn:
        pass
