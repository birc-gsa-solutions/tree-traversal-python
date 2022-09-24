# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from tree import T
from dft import in_order, in_order2, in_order3


def test_in_order() -> None:
    """Test in_order. Add tests as needed."""
    tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    res = list(in_order(tree))
    assert res == [1, 2, 3, 4, 5]
    assert list(in_order(None)) == []


def test_in_order2() -> None:
    """Test in_order. Add tests as needed."""
    tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    res = list(in_order2(tree))
    assert res == [1, 2, 3, 4, 5]
    assert list(in_order2(None)) == []


def test_in_order3() -> None:
    """Test in_order. Add tests as needed."""
    tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    res = list(in_order3(tree))
    assert res == [1, 2, 3, 4, 5]
    assert list(in_order3(None)) == []
