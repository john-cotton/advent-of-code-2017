#!/usr/bin/env python3

import sys


def to_exit(jumps):
    steps, i = 0, 0
    while i >= 0 and i < len(jumps):
        jump = jumps[i]
        jumps[i] += 1
        i += jump
        steps += 1
    return steps


def convert_input(lines):
    return [int(x) for x in lines]


def part1(lines):
    return to_exit([int(n.strip()) for n in lines])


if __name__ == '__main__':
    lines = list(sys.stdin)
    print(part1(lines))
