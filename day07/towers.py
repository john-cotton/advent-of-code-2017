#!/usr/bin/env python3

import re
import sys


def part1(_input):
    child_programs = set()
    parent_programs = set()

    for line in _input:
        program, _, children = parse(line)
        child_programs.update(children)
        parent_programs.add(program)

    # What program is at the root? The one parent that is not a child of any other program.
    root_programs = parent_programs - child_programs
    assert(len(root_programs) == 1)
    return list(root_programs)[0]


def parse(line):
    pattern = re.compile("(\w+) \((\d+)\)[ ->]*(.*)")
    program, weight, children = pattern.match(line).groups()
    children = [x.strip(',') for x in children.split()]
    return program, weight, children


if __name__ == '__main__':
    _input = list(sys.stdin)
    print(part1(_input))
