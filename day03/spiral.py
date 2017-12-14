#!/usr/bin/env python3

"""Spiral Memory

Part 1:

How many steps are required to carry the data from the square
identified in your puzzle input all the way [back to at square 1]?

    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23---> ...

Translation:

    What is the Manhattan (i.e. rectilinear, taxicab, city block)
    distance from 1 to any integer, i, on an Ulam spiral?


Part 2:

Store value 1 in square 1. Then, in the same allocation order as shown
above [for an Ulam spiral], store in each square the sum of the values
in all adjacent squares, including diagonals. Once a square is
written, its value does not change.

    147  142  133  122   59
    304    5    4    2   57
    330   10    1    1   54
    351   11   23   25   26
    362  747  806--->   ...

"""

import sys
from collections import deque
from math import ceil, sqrt


def odd(n):
    return bool(n % 2)


def odd_ceil(x):
    n = int(ceil(x))
    return n if odd(n) else n + 1


def manhattan_distance(i):
    """Compute rectilinear distance from 1 to i on an Ulam spiral.

                      n
                    <---->

            +-----------+---+
            | .     +   | . |    _
            |-----------|   |    |
            |   |       |   |    | r
            | + |   1   | + |    |
            |   |       | i |    V
            |   |-----------+
            | . |   +     S |
            +---+-----------+
                                 S=E^2
            <------ E ------>

    E = edge length of the ExE square containing i; always odd
    n = distance to that ring from square 1
    r = distance from i to its nearest, larger corner

    """
    if i == 1:
        return 0

    E = odd_ceil(sqrt(i))
    n = E//2
    q, r = divmod(E**2 - i, E-1)  # could use q to determine (x, y)...
    return n + abs(r - n)


def _expand_table(t):
    # Expand the table width by 2 -- fill the outer ring with zeros
    for row in range(len(t)):
        t[row].appendleft(0)
        t[row].append(0)
    cols = len(t) + 2
    t.appendleft(deque(cols*[0]))
    t.append(deque(cols*[0]))
    assert(cols == len(t))
    assert(len(t) == len(t[0]))
    return cols


def sum_generator():
    """Generate adjacency sums in sequence, following an Ulam spiral.

    How? Grow a deque of deques representing a table of row x column.
    Always keep a ring of padding with zeros outside the ring being filled.

    """
    t = deque()

    def _cell_sum(row, col):
        _sum = sum(t[r][c] for r in range(row-1, row+2) for c in range(col-1, col+2))
        t[row][col] = _sum
        return _sum

    # Base case, square 1
    yield 1
    t.append(deque([1]))
    _expand_table(t)

    while True:
        n = _expand_table(t)
        for row in range(n-3, 0, -1):  # north
            yield _cell_sum(row, n-2)
        for col in range(n-3, 0, -1):  # west
            yield _cell_sum(1, col)
        for row in range(2, n-1):      # south
            yield _cell_sum(row, 1)
        for col in range(2, n-1):      # east
            yield _cell_sum(n-2, col)


def part1(i):
    return manhattan_distance(i)


def part2(i):
    g = sum_generator()
    value = next(g)
    while value <= i:
        value = next(g)
    return value


if __name__ == '__main__':
    i = int(sys.stdin.readline().strip())
    print(part1(i))
    print(part2(i))
