import pytest

from pathlib import Path

from phypigui.python.src.Exceptions import PathDoesntExist, IllegalFileType
from phypigui.python.src.model.config.FileOption import FileOption


file = Path("phypigui/test/resources/test_data/test_force.ppg")
image = Path("phypigui/python/resources/images/PhiPi_icon.png")
dir = Path("phypigui/test/resources/")


def test_file_option():
    file_option = FileOption("File")
    assert file_option.file_mode == FileOption.ANYFILE
    assert file_option.file_type == ''
    assert file_option.file_endings is None
    assert file_option.path is None
    assert file_option.start_path == Path()


def test_any_file():
    file_option = FileOption("File", file_opening_mode=FileOption.ANYFILE)

    file_option.path = file
    assert file_option.path == file
    assert file_option.start_path == Path()

    file_option.path = dir
    assert file_option.path == dir
    assert file_option.start_path == dir

    file_option.path = Path("doest_exist.no")

    file_option.path = None
    assert file_option.path is None


def test_existing_file():
    file_option = FileOption("File", file_opening_mode=FileOption.EXISTINGFILE)

    file_option.path = file
    assert file_option.path == file
    assert file_option.start_path == Path()

    with pytest.raises(IllegalFileType):
        file_option.path = dir
    assert file_option.path == file
    assert file_option.start_path == Path()

    with pytest.raises(PathDoesntExist):
        file_option.path = Path("doest_exist.no")

    file_option.path = None
    assert file_option.path is None


def test_dir():
    file_option = FileOption("File", file_opening_mode=FileOption.DIR)

    file_option.path = dir
    assert file_option.path == dir
    assert file_option.start_path == dir

    with pytest.raises(IllegalFileType):
        file_option.path = file
    assert file_option.path == dir
    assert file_option.start_path == dir

    with pytest.raises(PathDoesntExist):
        file_option.path = Path("doesnt_exist.no")
    with pytest.raises(PathDoesntExist):
        file_option.path = Path("phypigui/doesnt_exist/")

    file_option.path = None
    assert file_option.path is None


def test_file_endings():
    file_option = FileOption("File", file_opening_mode=FileOption.EXISTINGFILE)

    file_option.path = file
    assert file_option.path == file
    file_option.path = image
    assert file_option.path == image

    file_option = FileOption("File", file_opening_mode=FileOption.EXISTINGFILE, file_endings=['ppg'])
    file_option.path = file
    assert file_option.path == file
    with pytest.raises(IllegalFileType):
        file_option.path = image

    file_option = FileOption("File", file_opening_mode=FileOption.EXISTINGFILE, file_endings=['py'])
    with pytest.raises(IllegalFileType):
        file_option.path = file
    with pytest.raises(IllegalFileType):
        file_option.path = image

    file_option = FileOption("File", file_opening_mode=FileOption.EXISTINGFILE, file_endings=[])
    file_option.path = file
    assert file_option.path == file
    file_option.path = image
    assert file_option.path == image

    file_option = FileOption("File", file_opening_mode=FileOption.EXISTINGFILE, file_endings=['ppg', 'png'])
    file_option.path = file
    assert file_option.path == file
    file_option.path = image
    assert file_option.path == image

    file_option = FileOption("File", file_opening_mode=FileOption.DIR, file_endings=['ppg', 'png'])
    file_option.path = dir
    assert file_option.path == dir
    with pytest.raises(IllegalFileType):
        file_option.path = file
