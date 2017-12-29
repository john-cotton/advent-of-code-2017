from .knot_hash import csv_convert, tie_knot, part1
from utl.testers import validate_by_example


tie_knot_examples = {
    # (list, pos, len) : new_list
    ('0,1,2,3,4', 0, 3): [2, 1, 0, 3, 4],
    ('2,1,0,3,4', 3, 4): [4, 3, 0, 1, 2],
    ('4,3,0,1,2', 3, 1): [4, 3, 0, 1, 2],
    ('4,3,0,1,2', 1, 5): [3, 4, 2, 1, 0],
}


def tie_knot_wrapper(_input):
    # Convert input here; we have to pass multiple args anyway.
    L, i, n = _input
    return tie_knot(csv_convert(L), i, n)


def test_tie_knot():
    yield from validate_by_example(tie_knot_wrapper, tie_knot_examples)


part1_examples = {
    # (L, lengths) : (
    ('0,1,2,3,4', (3, 4, 1, 5)): 12,
}


def part1_wrapper(_input):
    L, lengths = _input
    return part1(csv_convert(L), lengths)


def test_part1():
    yield from validate_by_example(part1_wrapper, part1_examples)
