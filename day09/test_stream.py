from .stream import score_stream
from utl.testers import validate_by_example


garbage_examples = {
    # stream: (n_groups, t_score, n_garbage)
    '<>': (0, 0, 0),
    '<random characters>': (0, 0, 17),
    '<<<<>': (0, 0, 3),
    '<!!>': (0, 0, 0),
    '<!!!>>': (0, 0, 0),
    '<{o"i!a,<{i<a>': (0, 0, 10),
    '<{!>}>': (0, 0, 2)
}


def test_garbage():
    yield from validate_by_example(score_stream, garbage_examples)


stream_examples = {
    # stream: (n_groups, t_score, n_garbage)
    '{}': (1, 1, 0),
    '{{{}}}': (3, 6, 0),
    '{{},{}}': (3, 5, 0),
    '{{{},{},{{}}}}': (6, 16, 0),
    '{<{},{},{{}}>}': (1, 1, 10),
    '{<a>,<a>,<a>,<a>}': (1, 1, 4),
    '{{<a>},{<a>},{<a>},{<a>}}': (5, 9, 4),
    '{{<!>},{<!>},{<!>},{<a>}}': (2, 3, 13),
    '{{<ab>},{<ab>},{<ab>},{<ab>}}': (5, 9, 8),
    '{{<!!>},{<!!>},{<!!>},{<!!>}}': (5, 9, 0),
    '{{<a!>},{<a!>},{<a!>},{<ab>}}': (2, 3, 17),
}


def test_stream():
    yield from validate_by_example(score_stream, stream_examples)
