import pytest

from phypigui.python.src.view.MainWindow import MainWindow


@pytest.fixture
def main_window(qtbot):
    main = MainWindow()
    qtbot.addWidget(main)
    return main