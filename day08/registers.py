#!/usr/bin/env python3

import sys

from collections import defaultdict


def process(instructions):
    """Process (an iterable of) `instructions`.

    The defaultdict works because int() gives 0 by default. The
    instructions require only slight tweaking for Python's exec().

    """
    regs = defaultdict(int)  # noqa
    ops = {'inc': '+', 'dec': '-'}

    for i in instructions:
        r1, op, n, _, r2, cond = i.strip().split(' ', 5)
        s = "if regs['{r2}'] {cond}: regs['{r1}'] {op}= {n}".format(
            r2=r2, cond=cond, r1=r1, op=ops[op], n=n)
        exec(s)

    part1 = max(regs.values())
    return part1


def part2(s):
    pass


if __name__ == '__main__':
    print(process(sys.stdin))
