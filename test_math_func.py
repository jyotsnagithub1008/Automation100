import unittest
import math_func


def test_add():
    assert math_func.add(7, 3) ==10
    assert math_func.add(5) == 7


def test_sub():
    assert math_func.sub(7, 3) == 4
    assert math_func.sub(5) == 2


def test_multi():
    assert math_func.multi(7, 3) == 21
    assert math_func.multi(5) == 10
    
def test_div():
    assert math_func.div(8, 2) == 4
    assert math_func.div(4) == 2
