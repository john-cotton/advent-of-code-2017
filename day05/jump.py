#!/usr/bin/env python3

import sys


def to_exit(jumps, offset_adjustment):
    steps, i = 0, 0
    while i >= 0 and i < len(jumps):
        offset = jumps[i]
        jumps[i] += offset_adjustment(offset)
        i += offset
        steps += 1
    return steps


def part1(jumps):
    return to_exit(jumps, offset_adjustment=lambda x: 1)


def part2(jumps):
    return to_exit(jumps, offset_adjustment=lambda x: -1 if x >= 3 else 1)


if __name__ == '__main__':
    jumps1 = [int(x) for x in list(sys.stdin)]
    jumps2 = list(jumps1)
    print(part1(jumps1))
    print(part2(jumps2))
