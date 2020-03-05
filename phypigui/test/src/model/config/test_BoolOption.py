from phypigui.python.src.model.config.BoolOption import BoolOption


def test_bool_option():
    bool_option = BoolOption("Bool", start_value=True)
    assert bool_option.enabled
    bool_option.enabled = False
    assert not bool_option.enabled
