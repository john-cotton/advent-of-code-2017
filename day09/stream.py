#!/usr/bin/env python3

import sys


def score_stream(s):
    score = 0
    scores = []
    n_garbage = 0

    it = iter(s)
    while True:
        c = next(it, None)
        if c is None:
            break
        if c == '{':
            score += 1
            scores.append(score)
        if c == '}':
            score -= 1
        if c == '<':
            while True:
                c = next(it)
                if c == '!':
                    next(it)
                    continue
                if c == '>':
                    break
                n_garbage += 1

    n_groups = len(scores)
    t_score = sum(scores)

    return n_groups, t_score, n_garbage


if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    _, part1, part2 = score_stream(s)
    print(part1)
    print(part2)
