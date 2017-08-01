#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from civicu_app.skeleton import fib

__author__ = "Ashley Riehl"
__copyright__ = "Ashley Riehl"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
