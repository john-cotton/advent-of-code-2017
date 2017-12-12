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
    n = distance to that outer square from square 1
    r = distance from i to its nearest, larger corner

    """
    if i == 1:
        return 0

    E = odd_ceil(sqrt(i))
    n = E//2
    q, r = divmod(E**2 - i, E-1)  # could use q to determine (x, y)...
    return n + abs(r - n)


def sum_generator():
    """Generate adjacency sums in sequence, following an Ulam spiral.

    How? Grow a deque of deques representing a table of row x column.
    Always keep a ring of padding with zeros outside the ring being filled.

    (Why a deque? Mostly because I wanted to play with them. The
    mid-deque indexed access times are probably awful)

    """
    t = deque()

    def _cell_sum(row, col):
        # Yup, this sums 3x3 = 9 values, 5 of which are zeros :)
        _sum = sum(t[r][c] for r in range(row-1, row+2) for c in range(col-1, col+2))
        t[row][col] = _sum
        return _sum

    def _expand_table():
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

    # Base case, square 1
    yield 1
    t.append(deque([1]))
    _expand_table()

    while True:
        n = _expand_table()
        for row in range(n-3, 0, -1):  # north
            yield _cell_sum(row, n-2)
        for col in range(n-3, 0, -1):  # west
            yield _cell_sum(1, col)
        for row in range(2, n-1):      # south
            yield _cell_sum(row, 1)
        for col in range(2, n-1):      # east
            yield _cell_sum(n-2, col)


def sum_generator2():
    """2nd attempt...

    - Don't store the whole table; just the last 4 edges, in a FIFO

    - Use (out-of-range) slicing for the 3 cells in the adjacent edge
      that contribute to the current cell's sum (since it's forgiving)

    - Generate the first 10 values manually, since it skips some early edge cases

    - For each iteration:
       - the current edge starts with last item from 1 edge ago
       - the adjacent edge was 4 edges ago; it's now left-most in the deque
         - prefix it with the 2nd-last item from 1 edge ago
       - fill out the current edge -- with as many values as are in the adjacent edge

    """

    yield from (1, 1, 2, 4, 5, 10, 11, 23, 25, 26)

    first_four_edges = (
        [1, 2],
        [2, 4, 5],
        [5, 10, 11],
        [11, 23, 25, 26]
    )
    edges = deque(first_four_edges)

    while True:
        current = edges[-1][-1:]
        adjacent = edges.popleft()
        adjacent.insert(0, edges[-1][-2])

        for i in range(len(adjacent)):
            _sum = current[-1] + sum(adjacent[i:i+3])  # slice is forgiving! :)
            current.append(_sum)
            yield _sum

        edges.append(current)


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
