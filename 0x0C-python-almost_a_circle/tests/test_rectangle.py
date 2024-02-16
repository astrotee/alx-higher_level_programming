#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.n = Base().id

    def test_init(self):
        b1 = Rectangle(2, 3)
        self.assertEqual(b1.width, 2)
        self.assertEqual(b1.height, 3)

        b1 = Rectangle(2, 3, 4)
        self.assertEqual(b1.width, 2)
        self.assertEqual(b1.height, 3)
        self.assertEqual(b1.x, 4)

        b1 = Rectangle(2, 3, 4, 5)
        self.assertEqual(b1.width, 2)
        self.assertEqual(b1.height, 3)
        self.assertEqual(b1.x, 4)
        self.assertEqual(b1.y, 5)

        b1 = Rectangle(2, 3, 4, 5, 1)
        self.assertEqual(b1.width, 2)
        self.assertEqual(b1.height, 3)
        self.assertEqual(b1.x, 4)
        self.assertEqual(b1.y, 5)
        self.assertEqual(b1.id, 1)

    def test_auto_id(self):
        b1 = Rectangle(2, 3)
        self.assertEqual(b1.id, self.n + 1)

        b2 = Rectangle(2, 3)
        self.assertEqual(b2.id, self.n + 2)

        b3 = Rectangle(2, 3)
        self.assertEqual(b3.id, self.n + 3)

        b4 = Rectangle(2, 3, id=12)
        self.assertEqual(b4.id, 12)

        b5 = Rectangle(2, 3)
        self.assertEqual(b5.id, self.n + 4)

    def test_type_errors(self):
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, '1', 1)
        self.assertRaises(TypeError, Rectangle, 1, '1')
        self.assertRaises(TypeError, Rectangle, 1, 1, '1')
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, '1')

    def test_value_errors(self):
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, -1, 1)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, -1)
        self.assertRaises(ValueError, Rectangle, 1, 1, -1)
        self.assertRaises(ValueError, Rectangle, 1, 1, 1, -1)
