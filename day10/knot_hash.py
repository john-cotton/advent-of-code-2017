#!/usr/bin/env python3

import operator
import sys

from functools import reduce


def tie_knot(L, i, n):
    """Reverse `n` items at position `i` in list `L`.

          +-----------------------+
      L   |  |  |  |  |  |  |  |  |
          +-----------------------+
          0              i        len(L)
          |<--->|        |<------>|
           tail             head

              n = head + tail

    """
    # "Lengths larger than the size of the list are invalid"
    assert n <= len(L)

    # Calculate the size of the head and the (possibly zero-length) tail
    head = min(n, len(L) - i)
    tail = n - head

    # Make the reversed list; then slice it in piecemeal, modifying L in-place
    rev = list(reversed(L[i:i+head] + L[0:tail]))
    L[i:i+head] = rev[:head]
    L[0:tail] = rev[head:]
    return L


def do_round(L, lengths, i=0, skip=0):
    """Do a knot hash round for list `L` by tying knots of various `lengths`.
    """
    for length in lengths:
        tie_knot(L, i, length)
        i = (i + length + skip) % len(L)
        skip += 1
    return i, skip


def csv_convert(line):
    return [int(x) for x in line.strip().split(',')]


def ascii_convert(byte_string):
    return [ord(c) for c in byte_string.strip()]


def part1(csv_lengths, hash_size=256):
    lengths = csv_convert(csv_lengths)
    L = list(range(hash_size))
    do_round(L, lengths)
    return L[0] * L[1]


def part2(byte_string, hash_size=256, step=16):
    suffix = [17, 31, 73, 47, 23]
    lengths = ascii_convert(byte_string) + suffix
    L = list(range(hash_size))
    position, skip = 0, 0

    for _ in range(64):
        position, skip = do_round(L, lengths, position, skip)

    sparse_hash = L
    dense_hash = []

    for x in range(0, hash_size, step):
        dense_hash.append(reduce(operator.xor, sparse_hash[x:x+step]))

    return ''.join('{:02x}'.format(x) for x in dense_hash)


if __name__ == '__main__':
    line = sys.stdin.readline()
    print(part1(line))
    print(part2(line))
