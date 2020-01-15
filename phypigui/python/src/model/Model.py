from abc import ABC
from typing import List, NoReturn

from ..view.View import View


class Model(ABC):
    def __init__(self):
        self.__views = List[View]

    def attach(self, view: View) -> NoReturn:
        self.__views.append(view)

    def detach(self, view: View) -> NoReturn:
        self.__views.remove(view)

    def notify(self) -> NoReturn:
        for view in self.__views:
            view.update()
