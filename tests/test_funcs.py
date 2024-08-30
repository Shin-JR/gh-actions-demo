import pytest

from main.funcs import division, sum_multiple


def test_sum_multiple():
    assert sum_multiple(1, 2, 3, 4, 5) == 15
    assert sum_multiple(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 55


def test_division():
    assert division(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        division(10, 0)
    assert division(0, 1) == 0
