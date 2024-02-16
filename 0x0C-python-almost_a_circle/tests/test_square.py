#!/usr/bin/python3

import unittest
import os
from models.base import Base
from models.square import Square


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.b1 = Square(2, 3, 4, 1)
        self.n = Base().id

    def test_init(self):
        b1 = Square(2)
        self.assertEqual(b1.size, 2)

        b1 = Square(2, 3)
        self.assertEqual(b1.size, 2)
        self.assertEqual(b1.x, 3)

        b1 = Square(2, 3, 4)
        self.assertEqual(b1.size, 2)
        self.assertEqual(b1.x, 3)
        self.assertEqual(b1.y, 4)

        self.assertEqual(self.b1.size, 2)
        self.assertEqual(self.b1.x, 3)
        self.assertEqual(self.b1.y, 4)
        self.assertEqual(self.b1.id, 1)

    def test_auto_id(self):
        b1 = Square(2, 3)
        self.assertEqual(b1.id, self.n + 1)

        b2 = Square(2, 3)
        self.assertEqual(b2.id, self.n + 2)

        b3 = Square(2, 3)
        self.assertEqual(b3.id, self.n + 3)

        b4 = Square(2, 3, id=12)
        self.assertEqual(b4.id, 12)

        b5 = Square(2, 3)
        self.assertEqual(b5.id, self.n + 4)

    def test_type_errors(self):
        self.assertRaises(TypeError, Square)
        self.assertRaises(TypeError, Square, '1', 1)
        self.assertRaises(TypeError, Square, 1, '1')
        self.assertRaises(TypeError, Square, 1, 1, '1')

    def test_value_errors(self):
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 1, -1)
        self.assertRaises(ValueError, Square, 1, 1, -1)
        self.assertRaises(ValueError, Square.create, size=-2)

    def test_area(self):
        b1 = Square(3)
        self.assertEqual(b1.area(), 9)

    def test_str(self):
        self.assertEqual(self.b1.__str__(), "[Square] (1) 3/4 - 2")

    def test_to_dictionary(self):
        self.assertEqual(self.b1.to_dictionary(),
                         {'id': 1, 'size': 2, 'x': 3, 'y': 4})

    def test_update(self):
        b1 = Square(2, 3, 4, 1)
        d = b1.to_dictionary()
        b1.update()
        self.assertEqual(b1.to_dictionary(), d)

        b1.update(23)
        d['id'] = 23
        self.assertEqual(b1.to_dictionary(), d)

        b1.update(43, 49)
        d['id'] = 43
        d['size'] = 49
        self.assertEqual(b1.to_dictionary(), d)

        b1.update(94, 90)
        d['id'] = 94
        d['size'] = 90
        self.assertEqual(b1.to_dictionary(), d)

        b1.update(39, 23, 84)
        d['id'] = 39
        d['size'] = 23
        d['x'] = 84
        self.assertEqual(b1.to_dictionary(), d)

        b1.update(58, 94, 39, 48)
        d['id'] = 58
        d['size'] = 94
        d['x'] = 39
        d['y'] = 48
        self.assertEqual(b1.to_dictionary(), d)

        b1.update(id=3)
        self.assertEqual(b1.id, 3)

        b1.update(id=3, size=4)
        self.assertEqual(b1.size, 4)

        b1.update(id=3, size=4, x=1)
        self.assertEqual(b1.x, 1)

        b1.update(id=3, size=4, x=1, y=2)
        self.assertEqual(b1.y, 2)

    def test_create(self):
        b1 = Square.create(id=3, size=4)
        self.assertEqual(b1.size, 4)

        b1 = Square.create(id=3, size=5, x=1)
        self.assertEqual(b1.x, 1)

        b1 = Square.create(id=3, size=5, x=1, y=2)
        self.assertEqual(b1.y, 2)

    def test_save_to_file(self):
        if os.path.exists('Square.json'):
            os.remove('Square.json')
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")
        if os.path.exists('Square.json'):
            os.remove('Square.json')
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file([self.b1])
        self.assertEqual(Square.load_from_file()[0].to_dictionary(),
                         self.b1.to_dictionary())

    def test_load_from_file(self):
        if os.path.exists('Square.json'):
            os.remove('Square.json')
        list_objs = Square.load_from_file()
        self.assertEqual(list_objs, [])
        Square.save_to_file([self.b1])
        list_objs = Square.load_from_file()
        self.assertEqual(list_objs[0].to_dictionary(), self.b1.to_dictionary())
