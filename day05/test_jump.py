from .jump import part1, part2
from utl.testers import validate_by_example


def input_cb(jumps):
    return [int(n) for n in jumps.split()]


part1_examples = {
    # jumps : steps_to_exit
    ('0 3 0 1 -3'): 5
}


def test_part1():
    yield from validate_by_example(part1, part1_examples, input_cb)


part2_examples = {
    # jumps : steps_to_exit
    ('0 3 0 1 -3'): 10,
    ('0'): 2,
}


def test_part2():
    yield from validate_by_example(part2, part2_examples, input_cb)
