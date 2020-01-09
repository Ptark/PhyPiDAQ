from abc import ABC
from typing import List

from python.src.view import View


class Model(ABC):
    def __init__(self):
        self.__views = List[View]

    def attach(self, view: View):
        self.__views.append(view)

    def detach(self, view: View):
        self.__views.remove(view)

    def notify(self):
        for view in self.__views:
            view.update()
