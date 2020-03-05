from PyQt5.QtCore import QLocale

from phypigui.python.src.view.Translator import Translator


def test_install_translator():
    assert Translator.install_translator(QLocale.German)
    assert _translator() is None

    assert Translator.install_translator(QLocale.English)
    assert _translator() is not None

    english = _translator()
    assert not Translator.install_translator(QLocale.French)
    assert not Translator.install_translator(0)
    assert not Translator.install_translator(-1)
    assert not Translator.install_translator(999999999999999999)
    assert not Translator.install_translator(None)
    assert _translator() == english

    Translator.install_translator(QLocale.German)
    assert _translator() is None

    Translator.install_translator(QLocale.English)
    assert _translator() == english


def test_translate():
    Translator.install_translator(QLocale.German)

    _assert_tr_same("Datei")
    _assert_tr_same("Kein Dateipfad in \"%s\" ausgewählt")
    _assert_tr_same("Test123!")
    _assert_tr_same("Datei\nHilfe")
    _assert_tr_same("")
    _assert_tr_same("\t\0")

    Translator.install_translator(QLocale.English)

    assert Translator.tr("Datei") == "File"
    assert Translator.tr("No file path in the item \"%s\" selected")

    _assert_tr_same("Test123!")
    _assert_tr_same("Datei\nHilfe")
    _assert_tr_same("")
    _assert_tr_same("\t\0")


def test_language_changed_signal(qtbot):
    Translator.install_translator(QLocale.German)

    with qtbot.waitSignal(Translator.language_changed.signal, timeout=5000):
        Translator.install_translator(QLocale.English)
    with qtbot.assertNotEmitted(Translator.language_changed.signal):
        Translator.install_translator(QLocale.English)

    with qtbot.waitSignal(Translator.language_changed.signal, timeout=5000):
        Translator.install_translator(QLocale.German)
    with qtbot.assertNotEmitted(Translator.language_changed.signal):
        Translator.install_translator(QLocale.German)

    with qtbot.assertNotEmitted(Translator.language_changed.signal):
        Translator.install_translator(QLocale.French)


def _translator():
    return Translator._Translator__translator


def _assert_tr_same(text):
    assert Translator.tr(text) == text
