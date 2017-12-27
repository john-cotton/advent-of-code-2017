from .registers import process
from utl.testers import validate_by_example


part1_examples = {
    # input : output
    """\
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""": 1
}


def input_cb(i):
    return i.split('\n')


def test_part1():
    yield from validate_by_example(process, part1_examples, input_cb)
