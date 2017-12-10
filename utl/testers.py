"""A simple test harness.

Generate tests for every _input/_output pair.

"""


def validate(func, _input, output):
    assert output == func(_input)


def validate_by_example(func, examples):
    for _input, output in sorted(examples.items()):
        yield validate, func, _input, output
