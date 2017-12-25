#!/usr/bin/env python3

import re
import sys

from collections import Counter
from pprint import pprint  # noqa


Programs = dict()  # the parsed programs listing; a dict of dicts


def parse(line):
    pattern = re.compile("(\w+) \((\d+)\)[ ->]*(.*)")
    name, weight, subtowers = pattern.match(line).groups()
    weight = int(weight)
    subtowers = [x.strip(',') for x in subtowers.split()]
    return name, weight, subtowers


def parse_programs(listing):
    for line in listing:
        name, weight, subtowers = parse(line)
        Programs[name] = dict(weight=weight, subtowers=subtowers)


def bottom_program():
    """The bottom program is the only one that's not also a subtower.
    """
    programs = set(Programs.keys())
    subtowers = set(s for p in programs for s in Programs[p]['subtowers'])
    bottoms = programs - subtowers
    assert len(bottoms) == 1
    return list(bottoms)[0]


def tower_weight(name):
    """Recursively compute tower weights, starting from program `name`.

    The Programs dict is updated with the tower_weight for each program.

    """
    p = Programs[name]
    subtower_weights = [tower_weight(x) for x in p['subtowers']]
    p['tower_weight'] = p['weight'] + sum(subtower_weights)
    return p['tower_weight']


def update_tower_weights(base):
    tower_weight(base)


def pprint_fun(base):
    pprint(Programs)

    def make_tower(name):
        """Recursively build a tower of nested dicts."""
        node = dict()
        for x in Programs[name]['subtowers']:
            node[x] = make_tower(x)
        return node

    Tower = dict()
    Tower[base] = make_tower(base)
    pprint(Tower)


def compute_correction(name, correction=None):
    """Return a tuple of (program_to_correct, correction)

    Walk recursively up the tower, following any subtower whose weight
    differs from the other subtowers on this program's disc. Stop at the
    first program for which either:

       a) there are no subtowers
          - i.e. it has no disc
       b) the subtowers are all equally weighted
          - i.e. its disc is balanced

    The correction to make is the difference (delta) between the
    outlying subtower's weight and the weight common to all other
    subtowers. And this holds true at each step of the recursive walk,
    so pass the correction forward for confirmation.

    When there's only 1 or 2 subtowers, there's some special-casing that
    could make the puzzle solution ambigious:

       1 subtowers - In a monolithic subtower, *any* program weight can
                     be corrected to affect the entire subtower weight.
                     How would we know which one to correct?

       2 subtowers - At a subtower 'Y', how do we know which subtower is
                     imbalanced? We could peek ahead to see which
                     subtower has an imbalanced disc, and go that way.
                     However, if neither does, then *either* program
                     weight could be corrected. How would we know which
                     one to correct?

    Both cases above lead to a potentially ambiguous puzzle answer, so
    I'm guessing... YAGNI!

    """
    p = Programs[name]
    n_subtowers = len(p['subtowers'])

    # No disc
    if 0 == n_subtowers:
        return name, correction

    # Ambiguity ==> YAGNI
    if 1 <= n_subtowers <= 2:
        raise NotImplementedError

    assert n_subtowers >= 3

    # Analyze subtower weights
    sub_weights = [Programs[x]['tower_weight'] for x in p['subtowers']]
    c = Counter(sub_weights).most_common()
    common_weight, common_count = c[0]
    weight, count = c[-1]
    delta = common_weight - weight

    # Balanced disc; this program's weight should be corrected.
    if len(c) == 1:
        assert delta == 0  # c[0] _is_ c[-1]
        return name, correction

    # Confirm/assign the required weight correction
    if correction:
        assert correction == delta
    else:
        correction = delta

    # One of n_subtowers is an outlier whose weight is counted only once
    assert len(c) == 2
    assert common_count == n_subtowers - 1
    assert count == 1

    # Correlate the weight with its subtower name, via its index
    index = sub_weights.index(weight)
    subtower = p['subtowers'][index]

    # Recurse up the (imbalanced) subtower
    return compute_correction(subtower, correction)


def part2(base):
    """Given exactly one program's weight is wrong, what should it be?
    """
    program, correction = compute_correction(base)
    return Programs[program]['weight'] + correction


def part1():
    """What is the name of the bottom program?
    """
    return bottom_program()


def main(listing):
    parse_programs(listing)
    base = part1()
    update_tower_weights(base)
    # pprint_fun(base)
    corrected_weight = part2(base)
    return base, corrected_weight


if __name__ == '__main__':
    p1, p2 = main(sys.stdin)
    print(p1)
    print(p2)
