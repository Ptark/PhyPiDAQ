import pytest

from phypigui.python.src.model.Model import Model
from phypigui.python.src.view.View import View


class IModel(Model):
    @property
    def views(self):
        return self._Model__views


class IView(View):
    def __init__(self):
        self.__was_called = False

    @property
    def was_called(self):
        called = self.__was_called
        self.__was_called = False
        return called

    def update_view(self):
        self.__was_called = True


@pytest.fixture(scope='class')
def model_view():
    return IModel(), IView()


def test_attach_detach(model_view):
    model, view = model_view

    assert len(model.views) == 0

    model.attach(view)
    assert len(model.views) == 1
    assert view in model.views

    model.attach(view)
    assert len(model.views) == 1

    model.detach(view)
    assert len(model.views) == 0

    model.detach(view)
    assert len(model.views) == 0


def test_update_view(model_view):
    model, view1 = model_view
    view2 = IView()
    view3 = IView()

    model.attach(view1)
    model.attach(view2)
    assert not view1.was_called
    assert not view2.was_called
    assert not view3.was_called

    model.notify()
    assert view1.was_called
    assert view2.was_called
    assert not view3.was_called

    model.detach(view2)
    model.attach(view3)
    model.notify()
    assert view1.was_called
    assert not view2.was_called
    assert view3.was_called

    model.detach(view1)
    model.detach(view3)
    model.notify()
    assert not view1.was_called
    assert not view2.was_called
    assert not view3.was_called
