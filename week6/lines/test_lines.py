"""
-----------------
Test for lines.py
-----------------

Source: https://cs50.harvard.edu/python/2022/psets/6/lines/
"""

from lines import is_loc


def test_empty_line():
    assert is_loc("") is False


def test_lines_with_only_blanks():
    assert is_loc("    ") is False


def test_comment_at_beginning():
    assert is_loc("# Some Comments") is False
    assert is_loc("##") is False


def test_comment_indented():
    assert is_loc("    # Some Indented Comment") is False
    assert is_loc("    ##") is False
