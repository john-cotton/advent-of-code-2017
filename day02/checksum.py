#!/usr/bin/env python3

import sys
import itertools


def checksum(spreadsheet, row_func):
    values = map(row_numbers, spreadsheet)
    row_calculations = map(row_func, values)
    return sum(row_calculations)


def part1(spreadsheet):
    return checksum(spreadsheet, row_difference)


def part2(spreadsheet):
    return checksum(spreadsheet, row_quotient)


def row_numbers(row):
    return [int(x) for x in row.split()]


def row_difference(row):
    return max(row) - min(row) if row else 0


def row_quotient(row):
    for x, y in itertools.combinations(row, 2):
        if x < y:
            x, y = y, x
        if y == 0:
            return 0
        if x % y == 0:
            return x//y
    return 0


if __name__ == '__main__':
    s = list(sys.stdin)
    print(part1(s))
    print(part2(s))
