from .passphrase import no_duplicates_in, no_anagrams_in
from utl.testers import validate_by_example

valid = True

part1_examples = {
    # phrase : valid
    'aa bb cc dd ee': valid,
    'aa bb cc dd aa': not valid,
    'aa bb cc dd aaa': valid,
}


def test_part1():
    yield from validate_by_example(no_duplicates_in, part1_examples)


part2_examples = {
    # phrase : valid
    'abcde fghij': valid,
    'abcde xyz ecdab': not valid,
    'a ab abc abd abf abj': valid,
    'iiii oiii ooii oooi oooo': valid,
    'oiii ioii iioi iiio': not valid,
}


def test_part2():
    yield from validate_by_example(no_anagrams_in, part2_examples)
