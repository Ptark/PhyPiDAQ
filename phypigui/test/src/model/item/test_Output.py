from phypigui.python.src.model.item.Output import Output


def test_function():
    output = Output(1, 0)
    for i in range(3, 24):
        assert output.function(i) == 0
    for i in range(67, 79):
        assert output.function(i) == 0

    output.function = lambda data: data
    for i in range(0, 24):
        assert output.function(i) == i
