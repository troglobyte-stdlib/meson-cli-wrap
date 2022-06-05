#!/usr/bin/env python3

#
# Troglobyte stdlib:
# author: Michael Gene Brockus
# Gmail: <mail: michaelbrockus@gmail.com>
#
from code.core import greet


#
# Test cases for this project.
#
def test_basic_assert_works():
    assert True

def test_greet_not_none():
    assert greet() is not None
