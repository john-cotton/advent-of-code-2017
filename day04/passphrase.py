#!/usr/bin/env python3

import fileinput


def no_duplicates_in(words):
    return len(words) == len(set(words))


def no_anagrams_in(words):
    return no_duplicates_in(
        [''.join(sorted(x)) for x in words]
    )


if __name__ == '__main__':
    part1, part2 = 0, 0
    for line in fileinput.input():
        words = line.split()
        part1 += no_duplicates_in(words)
        part2 += no_anagrams_in(words)
    print(part1)
    print(part2)
