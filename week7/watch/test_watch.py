"""
Test watch.py
"""

from watch import parse


def test_iframe_single_attribute() -> None:
    """\
    Tests iframes with single (only a 'src') attributes
    """

    assert (
        parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>')
        == "https://youtu.be/xvFZjo5PgG0"
    )

    assert (
        parse('<iframe src="https://www.youtube.com/embed/YSykw8vOJ-Y"></iframe>')
        == "https://youtu.be/YSykw8vOJ-Y"
    )


def test_iframe_multiple_attributes() -> None:
    """\
    Test iframes with multiple attributes
    """

    assert (
        parse(
            '<iframe width="560" height="315"'
            ' src="https://www.youtube.com/embed/xvFZjo5PgG0"'
            ' title="YouTube video player"'
            ' frameborder="0" allow="accelerometer; autoplay;'
            " clipboard-write; encrypted-media; gyroscope;"
            ' picture-in-picture" allowfullscreen></iframe>'
        )
        == "https://youtu.be/xvFZjo5PgG0"
    )

    assert (
        parse(
            '<iframe width="1424" height="631"'
            ' src="https://www.youtube.com/embed/YSykw8vOJ-Y"'
            ' title="Tommy Guerrero - Soul Food Taqueria (Full Album)"'
            ' frameborder="0" allow="accelerometer; autoplay;'
            " clipboard-write; encrypted-media; gyroscope;"
            ' picture-in-picture" allowfullscreen></iframe>'
        )
        == "https://youtu.be/YSykw8vOJ-Y"
    )


def test_iframe_without_src_attribute() -> None:
    """\
    Tests iframe elements that have no 'src' attribute
    """

    assert (
        parse(
            '<iframe width="1424" height="631"'
            ' href="https://www.youtube.com/embed/YSykw8vOJ-Y"'
            ' title="Tommy Guerrero - Soul Food Taqueria (Full Album)"'
            ' frameborder="0" allow="accelerometer; autoplay;'
            " clipboard-write; encrypted-media; gyroscope;"
            ' picture-in-picture" allowfullscreen></iframe>'
        )
        is None
    )

    assert (
        parse('<iframe href="https://www.youtube.com/embed/YSykw8vOJ-Y"></iframe>')
        is None
    )
