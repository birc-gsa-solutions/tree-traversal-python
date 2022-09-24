"""A module for depth-first (in-order) traversal of trees."""

from typing import Iterable, Generator
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


def in_order2(t: T | None) -> Iterable[int]:
    """In-order traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(in_order2(tree))
    [1, 2, 3, 4, 5]
    """
    stack: list[T] = []

    while t:
        # go left and save path on the stack
        while t.left:
            stack.append(t)
            t = t.left
        # go up while emitting
        while t:
            yield t.val
            if t.right:
                t = t.right
                break
            t = stack.pop() if stack else None


def go_left(v: T) -> T:
    """Go left and save path on parent pointers."""
    while v.left:
        v.left.parent = v
        v = v.left
    return v


def get_ancestor(v: T) -> T | None:
    """Go to the next ancestor we are not a right-child of."""
    while v.parent and v.parent.right == v:
        v = v.parent
    return v.parent


def go_up(t: T) -> Generator[int, None, T | None]:
    """Search up for the next place we can branch right.

    While we search up, we emit the nodes we meet on our way,
    as long as they are not parents of right-nodes on the path,
    because we have already seen those."""
    v: T | None = t
    while v:
        yield v.val
        if v.right:
            # We can branch right here, so set the parent pointer
            # and return the right child
            v.right.parent = v
            return v.right
        v = get_ancestor(v)
    return v


def in_order3(t: T | None) -> Iterable[int]:
    """In-order traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(in_order3(tree))
    [1, 2, 3, 4, 5]
    """

    while t:
        t = go_left(t)           # Search down a left branch
        t = yield from go_up(t)  # then search up and take a right turn
