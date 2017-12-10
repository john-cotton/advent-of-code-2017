from .captcha import part1, part2
from utl.testers import validate_by_example


part1_examples = {
    '1122': 3,
    '1111': 4,
    '1234': 0,
    '91212129': 9,
    '': 0,
}


def test_part1():
    yield from validate_by_example(part1, part1_examples)


part2_examples = {
    '1212': 6,
    '1221': 0,
    '123425': 4,
    '123123': 12,
    '12131415': 4,
    '': 0,
}


def test_part2():
    yield from validate_by_example(part2, part2_examples)
