from .jump import to_exit
from utl.testers import validate_by_example


part1_examples = {
    # jumps : steps_to_exit
    ('0 3 0 1 -3'): 5
}


def test_part1():
    yield from validate_by_example(to_exit, part1_examples,
                                   input_cb=lambda x: [int(n) for n in x.split()])
