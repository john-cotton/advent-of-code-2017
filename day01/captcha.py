#!/usr/bin/env python3

"""Inverse Captcha

Part 1:

Find the sum of all digits that match the next digit in the list. The
list is circular, so the digit after the last digit is the first digit
in the list.

Part 2:

Instead of considering the next digit, consider the digit halfway
around the circular list. Fortunately, your list has an even number of
elements.

"""


def captcha(digits, offset):
    # negative list indices ftw
    matches = (int(d) for i, d in enumerate(digits) if d == digits[i-offset])
    return sum(matches)


def part1(s):
    return captcha(s, offset=1)


def part2(s):
    assert(len(s) % 2 == 0)
    return captcha(s, offset=len(s)//2)


if __name__ == '__main__':
    import sys
    s = sys.stdin.readline().strip()
    print(part1(s))
    print(part2(s))
