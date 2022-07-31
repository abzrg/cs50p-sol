"""\
Test um.py
"""

from um import count


def test_um_itself():
    """Test one word that has um in it"""
    assert count("um") == 1
    assert count("umm") == 0


def test_non_alnum_around():
    """Test non-alpha and non-numeric (\\W) characters around um"""
    assert count("um...") == 1
    assert count("um, um.") == 2
    assert count("um?") == 1


def test_case_sensitivity():
    """Test case-sensitivity of um"""
    assert (
        count("Um? Mum? Is this that album, um, umm, the clumsy alums play drums?") == 2
    )
    assert count("UM? thanks, um, regular expression make sense now.") == 2
