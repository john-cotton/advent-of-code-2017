#!/usr/bin/env python3

import sys


def redistribute(banks, i):
    """Redistribute blocks in bank `i` across all the memory `banks`"""
    n = banks[i]
    banks[i] = 0
    while n:
        i = (i+1) % len(banks)
        banks[i] += 1
        n -= 1
    return banks


def part1(_input):
    banks = convert(_input)
    distributions = set()
    cycles = 0

    while tuple(banks) not in distributions:
        distributions.add(tuple(banks))

        # start cycle
        i = banks.index(max(banks))
        redistribute(banks, i)
        cycles += 1

    return cycles


def part2(s):
    pass


def convert(line):
    return [int(x) for x in line.split()]


if __name__ == '__main__':
    line = sys.stdin.readline()
    print(part1(line))
