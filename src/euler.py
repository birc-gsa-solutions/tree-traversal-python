"""
Euler tour traversal.

This isn't one of the traversals from the exercise, but a way to
traverse the tree as an Euler tour without using additional space.
"""

from __future__ import annotations
from typing import Optional, Iterator


class T:
    """
    Tree node class.

    A Tree is a T or None. A T has a value and a left/right sub-tree
    where these are also used as 'next' and 'then' in the traversal.
    """

    val: int
    _left_next: Tree
    _right_then: Tree

    def __init__(self, val: int, left: Tree, right: Tree) -> None:
        """Create a new tree node."""
        self.val = val
        self._left_next = left
        self._right_then = right

    @property
    def left(self) -> Tree:
        """Access left subtree."""
        return self._left_next

    @left.setter
    def left(self, left: Tree) -> None:
        self._left_next = left

    @property
    def next(self) -> Tree:
        """Access next subtree."""
        return self._left_next

    @next.setter
    def next(self, next: Tree) -> None:
        self._left_next = next

    @property
    def right(self) -> Tree:
        """Access right subtree."""
        return self._right_then

    @right.setter
    def right(self, right: Tree) -> None:
        self._right_then = right

    @property
    def then(self) -> Tree:
        """Access subtree after next."""
        return self._right_then

    @then.setter
    def then(self, then: Tree) -> None:
        self._right_then = then

    def __str__(self) -> str:
        """Get us a string representation."""
        return f"({self.left} [{self.val}] {self.right})"


Tree = Optional[T]
Root = T(-1337, None, None)  # A unique node used only as a pseudo-root


def rotate_out(v: T, f: T) -> T:
    """Rotate the edges of v until we find an out edge."""
    w, v.next, v.then = v.next, v.then, f
    while w is None:
        w, v.next, v.then = v.next, v.then, w
    return w


def traverse(t: Tree) -> Iterator[int]:
    """Perform an Euler tour of the tree t."""
    if t:
        v, f = t, Root
        while v is not Root:
            yield v.val
            v, f = rotate_out(v, f), v


tree = T(2,
         T(1, None, None),
         T(4,
           T(3, None, None),
           T(5,
             None,
             T(6, None, None))))
print(list(traverse(tree)))
