#!/usr/bin/env python3

import sys


def tie_knot(L, i, n):
    """Reverse `n` items at position `i` in list `L`.

          +-----------------------+
      L   |  |  |  |  |  |  |  |  |
          +-----------------------+
          0              i        len(L)
          |<---->|       |<------>|
            tail            head

              n = head + tail

    """
    # "Lengths larger than the size of the list are invalid"
    assert n <= len(L)

    # Calculate the size of the head and the (possibly zero-length) tail
    head = min(n, len(L) - i)
    tail = n - head

    # Make the reversed list; then slice it in, modifying L in-place
    rev = list(reversed(L[i:i+head] + L[0:tail]))
    L[i:i+head] = rev[:head]
    L[0:tail] = rev[head:]
    return L


def part1(L, lengths):
    """Compute a hash for list `L` by tying knots of various `lengths`.
    """
    i = 0
    for skip, length in enumerate(lengths):
        tie_knot(L, i, length)
        i = (i + length + skip) % len(L)
    return L[0] * L[1]


def convert(line):
    return [int(x) for x in line.strip().split(',')]


if __name__ == '__main__':
    lengths = convert(sys.stdin.readline())
    L = list(range(256))
    print(part1(L, lengths))
