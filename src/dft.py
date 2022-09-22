"""A module for depth-first (in-order) traversal of trees."""

from typing import Iterable
from tree import T


def in_order(t: T | None) -> Iterable[int]:
    """In-order traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(in_order(tree))
    [1, 2, 3, 4, 5]
    """
    # When we have a tree on the stack we need to traverse it,
    # when we have an int it is a value we should emit
    stack: list[T | int] = []

    def push(x: int | T | None) -> None:
        if x is not None:
            stack.append(x)

    push(t)
    while stack:
        match stack.pop():
            case int(v):
                yield v
            case T(val=val, left=left, right=right):
                push(right)
                push(val)
                push(left)
