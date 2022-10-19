#!/usr/bin/python3

import unittest
from tests.6-max_integer import max_integer


class TestListMax(unittest.TestCase):
    def test_indx(self):
        self.assertRaises(IndexError, max_integer, [])
