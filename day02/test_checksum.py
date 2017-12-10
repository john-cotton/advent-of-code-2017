from .checksum import part1, part2
from utl.testers import validate_by_example


part1_examples = {
    # spreadsheet: checksum
    ('5 1 9 5',
     '7 5 3',
     '2 4 6 8'): 18,

    ('1 2 3',
     '4 5 6',
     '7 8 9'): 6,

    ('1 2 3 4',): 3,

    ('1 2 3 4',
     '4 1',
     '1 4'): 9,

    ('0',
     '1 1',
     '0 0 0'): 0,

    ('',
     ''): 0,
}


def test_part1():
    yield from validate_by_example(part1, part1_examples)


part2_examples = {
    ('5 9 2 8',
     '9 4 7 3',
     '3 6 8 5'): 9,

    ('10  3  2  20',
     '15  4  7  30',
     ' 7  6 18   5'): 10,

    ('0 1 0',
     '0 0',
     '0',
     ''): 0,

    ('2 3 5',): 0
}


def test_part2():
    yield from validate_by_example(part2, part2_examples)
