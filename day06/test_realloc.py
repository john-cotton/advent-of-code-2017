from .realloc import convert, redistribute, reallocate
from utl.testers import validate_by_example


def test_redistribute():
    [2, 4, 1, 2] == redistribute([0, 2, 7, 0], i=2)


examples = {
    # banks : (cycles_to_detect_loop, cycles_in_loop)
    '0 2 7 0': (5, 4)
}


def test_reallocate():
    yield from validate_by_example(reallocate, examples, convert)
