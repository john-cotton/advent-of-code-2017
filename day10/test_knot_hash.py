from .knot_hash import csv_convert, tie_knot, part1, part2
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
    # (lengths, hash_size) : hash[0]*hash[1]
    ('3,4,1,5', 5): 12,
}


def part1_wrapper(_input):
    return part1(*_input)


def test_part1():
    yield from validate_by_example(part1_wrapper, part1_examples)


part2_examples = {
    # input_string : knot_hash
    '': 'a2582a3a0e66e6e86e3812dcb672a272',
    'AoC 2017': '33efeb34ea91902bb2f59c9920caa6cd',
    '1,2,3': '3efbe78a8d82f29979031a4aa0b16a9d',
    '1,2,4': '63960835bcdc130f0b66d7ff4f6a5a8e',
}


def test_part2():
    yield from validate_by_example(part2, part2_examples)
