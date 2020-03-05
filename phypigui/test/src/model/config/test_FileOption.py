import pytest

from pathlib import Path

from phypigui.python.src.Exceptions import PathDoesntExist
from phypigui.python.src.model.config.FileOption import FileOption


def test_file_option():
    file_option = FileOption("File")
    assert file_option.file_mode == 0
    assert file_option.file_type == ''
    assert file_option.file_endings is None
    assert file_option.path is None
    assert file_option.start_path == Path()

    file_option.path = Path("test_FileOption.py")
    assert file_option.path == Path("test_FileOption.py")
    assert file_option.start_path == Path()

    file_option.path = None
    assert file_option.path is None

    file_option.path = Path()
    assert file_option.path == Path()

    file_option = FileOption("File", "", FileOption.EXISTINGFILE)
    with pytest.raises(PathDoesntExist):
        file_option.path = Path("doest_exist.no")

    file_option = FileOption("File", "", FileOption.DIR)
    file_option.path = Path("..\\")
    assert file_option.path == file_option.start_path == Path("..\\")

    # TODO: more tests
