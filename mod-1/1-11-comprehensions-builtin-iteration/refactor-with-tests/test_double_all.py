# pytest runs every function whose name starts with test_, in every file whose name starts with test_.
# With the virtual environment activated, run it from this folder: python3 -m pytest
from double_all import double_all_purely


def test_double_all_purely():
    """double_all_purely - doubles each value in the list"""
    # == compares the contents of lists and dictionaries
    assert double_all_purely([1, 2, 3, 4]) == [2, 4, 6, 8]


def test_double_all_purely_does_not_mutate():
    """double_all_purely - returns a new list and leaves the original alone"""
    original = [1, 2, 3, 4]
    copy = double_all_purely(original)

    # A new list should be returned, not the original
    assert copy is not original

    # The copy should be doubled
    assert copy == [2, 4, 6, 8]

    # The original should not be mutated
    assert original == [1, 2, 3, 4]


def test_double_all_purely_strings():
    """double_all_purely - doubles numbers and repeats strings"""
    assert double_all_purely([1, 2, 'a', None]) == [2, 4, 'aa', None]
