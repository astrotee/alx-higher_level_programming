#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """unittests for max_integer function"""

    def test_max(self):
        """check if max value returned correctly"""
        self.assertEqual(max_integer([1, 3, 4]), 4)
        self.assertEqual(max_integer([0, -1, 3, 4]), 4)

    def test_empty(self):
        """check if None is returned on empty list"""
        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer(""))

    def test_single(self):
        """check the max value of a single item list"""
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-100]), -100)
