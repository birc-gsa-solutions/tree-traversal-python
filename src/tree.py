"""Module for representing trees."""

from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class T:
    """A node in a tree. Leaves are None"""
    val: int
    left: T | None
    right: T | None

    # For versions where we add parents
    parent: T | None = field(default_factory=lambda: None, repr=False)
