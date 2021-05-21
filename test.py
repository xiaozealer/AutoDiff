from numpy.lib.function_base import gradient
from Variable import *
import numpy as np
import pytest
from pathlib import Path
a = Variable(5, 'a')
b = Variable(4, 'b')

eps = Variable(1e-9)


def gradient_check(f, result, a, b=None):
    gradient = result.get_gradient()
    if b:
        da = (f(a + eps, b) - f(a - eps, b)).val / (eps.val*2)
        assert gradient[a] == pytest.approx(da, 1e-5)
        db = (f(a, b + eps) - f(a, b - eps)).val / (eps.val*2)
        assert gradient[b] == pytest.approx(db, 1e-5)
    else:
        da = (f(a + eps) - f(a - eps)).val / (eps.val*2)
        assert gradient[a] == pytest.approx(da, 1e-7)


def test_add():
    result = a + b
    assert result.val == a.val+b.val
    gradient_check(Variable.__add__, result, a, b)


def test_mul():
    result = a * b
    assert result.val == a.val * b.val
    gradient_check(Variable.__mul__, result, a, b)


def test_neg():
    result = -a
    assert result.val == -a.val
    gradient_check(Variable.__neg__, result, a)


def test_sub():
    result = a - b
    assert result.val == a.val - b.val
    gradient_check(Variable.__sub__, result, a, b)


def test_div():
    result = a / b
    assert result.val == a.val / b.val
    gradient_check(Variable.__truediv__, result, a, b)


def test_sin():
    result = sin(a)
    assert result.val == np.sin(a.val)
    gradient_check(sin, result, a)


def test_cos():
    result = cos(a)
    assert result.val == np.cos(a.val)
    gradient_check(cos, result, a)


def test_exp():
    result = exp(a)
    assert result.val == np.exp(a.val)
    gradient_check(exp, result, a)


def test_log():
    result = log(a)
    assert result.val == np.log(a.val)
    gradient_check(log, result, a)


def func(a, b):
    return exp(a)*sin(b)+log(a)/b-a


def test_gradient():
    result = func(a, b)
    assert result.val == np.exp(
        a.val) * np.sin(b.val)+np.log(a.val)/b.val - a.val
    gradient_check(func, result, a, b)
