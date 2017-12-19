#!/usr/bin/env python3

import sys

from collections import OrderedDict


def redistribute(banks, i):
    """Redistribute all blocks in bank `i` across the memory `banks`"""
    n = banks[i]
    banks[i] = 0
    while n:
        i = (i+1) % len(banks)
        banks[i] += 1
        n -= 1
    return banks


def reallocate(banks):
    distributions = OrderedDict()
    cycles = 0

    while tuple(banks) not in distributions:
        distributions[tuple(banks)] = cycles
        redistribute(banks, banks.index(max(banks)))
        cycles += 1

    cycles_in_loop = cycles - distributions[tuple(banks)]
    return cycles, cycles_in_loop


def convert(line):
    return [int(x) for x in line.split()]


if __name__ == '__main__':
    line = sys.stdin.readline()
    banks = convert(line)
    part1, part2 = reallocate(banks)
    print(part1)
    print(part2)
