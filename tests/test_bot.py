#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from civicu_app.bot import recognize_greeting

__author__ = "Ashley Riehl"
__copyright__ = "Ashley Riehl"
__license__ = "mit"


def test_recognize_greeting():
    assert recognize_greeting('Hi') == True
    assert recognize_greeting('Hello') == True
    assert recognize_greeting('Yo') == False
    assert recognize_greeting('') == False
    # with pytest.raises(AssertionError):
    #     fib(-10)
