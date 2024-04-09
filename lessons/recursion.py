"""Writing a Recursive Function."""

__author__ = "730439074"


def f(n: int, k: int) -> int:
    """Write a recursive function that is multiplying."""
    if n == 0:  # base case, returns zero because anything times zero is zero
        return 0
    else:  # recursive rule
        return f(n - 1, k) + k
