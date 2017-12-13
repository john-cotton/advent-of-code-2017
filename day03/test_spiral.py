import itertools

from .spiral import part1, sum_generator, sum_generator2
from utl.testers import validate_by_example


part1_examples = {
    # i : manhattan_distance
    1: 0,
    12: 3,
    23: 2,
    1024: 31
}


def test_part1():
    yield from validate_by_example(part1, part1_examples)


part2_sample_sums = [
    1,
    1, 2,
    4, 5,
    10, 11,
    23, 25,
    26, 54, 57, 59,
    122, 133, 142, 147,
    304, 330, 351, 362,
    747, 806
]


def test_sum_generator():
    sums = take(len(part2_sample_sums), sum_generator())
    assert sums == part2_sample_sums


def test_sum_generator2():
    sums = take(len(part2_sample_sums), sum_generator2())
    assert sums == part2_sample_sums


def take(n, iterable):
    "Return first n items of the iterable as a list"""
    # https://docs.python.org/2/library/itertools.html#recipes
    return list(itertools.islice(iterable, n))
