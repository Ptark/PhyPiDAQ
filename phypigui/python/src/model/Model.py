from abc import ABC
from typing import List, NoReturn

from ..view.View import View


class Model(ABC):
    """This class represents the model of the model-view design pattern"""
    def __init__(self):
        self.__views: List[View] = []

    def attach(self, view: View) -> NoReturn:
        """Subscribes a view

            Args:
                view (View): A view, which will be subscribed to this model.
        """
        self.__views.append(view)

    def detach(self, view: View) -> NoReturn:
        """Unsubscribes a subscribed view

            Args:
                view (View): The subscribed view.
        """
        self.__views.remove(view)

    def notify(self) -> NoReturn:
        """Notify all subscribers"""
        for view in self.__views:
            view.update_view()
