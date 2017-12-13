"""A simple test harness.

Generate tests for every _input/_output pair.

"""


def validate(func, _input, output):
    assert output == func(_input)


def validate_by_example(func, examples, input_cb=None):
    for _input, output in sorted(examples.items()):
        if input_cb:
            _input = input_cb(_input)
        yield validate, func, _input, output
