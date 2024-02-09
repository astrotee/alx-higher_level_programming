#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.n = Base().id

    def test_id(self):
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
