from abc import ABC
from typing import NoReturn


class View(ABC):
    """This class represents the view of the model-view design pattern

        It can attach itself to a model to receive updates from it.
    """
    def update_view(self) -> NoReturn:
        """Is called when a model it is subscribed to, broadcasts an update"""
        pass
