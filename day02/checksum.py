#!/usr/bin/env python3

"""Corruption Checksum

Part 1:

The spreadsheet consists of rows of apparently-random _numbers_. For
each row, determine the difference between the largest value and the
smallest value; the checksum is the sum of all of these differences.

Part 2:

Find the only two numbers in each row where one evenly divides the
other - that is, where the result of the division operation is a whole
number - divide them, and add up each line's result.

"""

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
