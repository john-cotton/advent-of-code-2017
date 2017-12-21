from .towers import part1
from utl.testers import validate_by_example

sample1 = """\
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

input1 = tuple(sample1.split('\n'))

part1_examples = {
    # input : output
    input1: 'tknk'
}


def test_part1():
    yield from validate_by_example(part1, part1_examples)
