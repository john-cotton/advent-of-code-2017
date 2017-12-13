#!/usr/bin/env python3

import sys


def no_duplicates_in(words):
    return len(words) == len(set(words))


def no_anagrams_in(words):
    return no_duplicates_in(
        [''.join(sorted(x)) for x in words]
    )


def stats(line):
    words = line.split()
    return (no_duplicates_in(words), no_anagrams_in(words))


if __name__ == '__main__':
    part1, part2 = map(sum, zip(*(stats(line) for line in sys.stdin)))
    print(part1)
    print(part2)
