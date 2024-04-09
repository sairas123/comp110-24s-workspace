"""Test sum functionality."""

from lessons.sum import f_sum

def test_sum_empty() -> None:
    """Sum of empty list should return 0."""
    assert sum([]) == 0 

    def test_sum_one_element() -> None:
        """Sum of one element should reutrn that elements."""
        test: list[int] = [7]
        assert su,(test) == 7

def test_sum_positive() -> None:
    """Sum of positice numbers should return sum of those numbers"""
    test: list[int] = [2, 4, 6]
    assert sum(test) == 12

def test_sum_with_negatives() -> None:
    """Sum should worj with positice and negaitve numbers."""
    test: list[int] = [2, -2, 4]
    assert sum(test) == 4