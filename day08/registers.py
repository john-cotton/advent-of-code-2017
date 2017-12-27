#!/usr/bin/env python3

import sys

from collections import defaultdict


def process(instructions):
    """Process (an iterable of) `instructions`.

    The defaultdict works because int() gives 0 by default. The
    instructions require only slight tweaking for Python's exec().

    """
    regs = defaultdict(int)
    ops = {'inc': '+', 'dec': '-'}
    p2_highest_ever = 0

    for i in instructions:
        r1, op, n, _, r2, cond = i.strip().split(' ', 5)
        s = "if regs['{r2}'] {cond}: regs['{r1}'] {op}= {n}".format(
            r2=r2, cond=cond, r1=r1, op=ops[op], n=n)
        exec(s)
        p2_highest_ever = max(regs[r2], p2_highest_ever)

    p1_highest_now = max(regs.values())
    return p1_highest_now, p2_highest_ever


if __name__ == '__main__':
    p1, p2 = process(sys.stdin)
    print(p1)
    print(p2)
