#!/usr/bin/env python3

import sys


def no_duplicates_in(phrase):
    words = _convert(phrase)
    return len(words) == len(set(words))


def no_anagrams_in(phrase):
    return no_duplicates_in([''.join(sorted(x)) for x in _convert(phrase)])


def _convert(phrase):
    return phrase.split() if isinstance(phrase, str) else phrase


def part1(phrases):
    return sum(no_duplicates_in(x) for x in phrases)


def part2(phrases):
    return sum(no_anagrams_in(x) for x in phrases)


if __name__ == '__main__':
    s = list(sys.stdin)
    print(part1(s))
    print(part2(s))
