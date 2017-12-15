from .realloc import redistribute, part1
from utl.testers import validate_by_example


def test_redistribute():
    [2, 4, 1, 2] == redistribute([0, 2, 7, 0], i=2)


part1_examples = {
    # input : output
    '0 2 7 0': 5,
}


def test_part1():
    yield from validate_by_example(part1, part1_examples)
