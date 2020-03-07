from phypigui.python.src.model.item.Input import Input


def test_number_of_input():
    input = Input(0, 0)
    assert input.number_of_input == 0
