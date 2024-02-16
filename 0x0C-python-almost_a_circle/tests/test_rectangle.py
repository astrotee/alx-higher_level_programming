#!/usr/bin/python3

import unittest
import os
import sys
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.b1 = Rectangle(2, 3, 4, 5, 1)
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

        self.assertEqual(self.b1.width, 2)
        self.assertEqual(self.b1.height, 3)
        self.assertEqual(self.b1.x, 4)
        self.assertEqual(self.b1.y, 5)
        self.assertEqual(self.b1.id, 1)

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
        self.assertRaises(ValueError, Rectangle.create, width=-2)
        self.assertRaises(ValueError, Rectangle.create, height=-2)

    def test_area(self):
        b1 = Rectangle(3, 4)
        self.assertEqual(b1.area(), 12)

    def test_str(self):
        self.assertEqual(self.b1.__str__(), "[Rectangle] (1) 4/5 - 2/3")

    def test_to_dictionary(self):
        self.assertEqual(self.b1.to_dictionary(),
                         {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5})

    def test_update(self):
        b1 = Rectangle(2, 3, 4, 5, 1)
        d = b1.to_dictionary()
        b1.update()
        self.assertEqual(b1.to_dictionary(), d)

        b1.update(23)
        d['id'] = 23
        self.assertEqual(b1.to_dictionary(), d)

        b1.update(43, 49)
        d['id'] = 43
        d['width'] = 49
        self.assertEqual(b1.to_dictionary(), d)

        b1.update(94, 90, 20)
        d['id'] = 94
        d['width'] = 90
        d['height'] = 20
        self.assertEqual(b1.to_dictionary(), d)

        b1.update(39, 23, 83, 84)
        d['id'] = 39
        d['width'] = 23
        d['height'] = 83
        d['x'] = 84
        self.assertEqual(b1.to_dictionary(), d)

        b1.update(58, 84, 94, 39, 48)
        d['id'] = 58
        d['width'] = 84
        d['height'] = 94
        d['x'] = 39
        d['y'] = 48
        self.assertEqual(b1.to_dictionary(), d)

        b1.update(id=3)
        self.assertEqual(b1.id, 3)

        b1.update(id=3, width=4)
        self.assertEqual(b1.width, 4)

        b1.update(id=3, width=4)
        self.assertEqual(b1.width, 4)

        b1.update(id=3, width=4, height=5)
        self.assertEqual(b1.height, 5)

        b1.update(id=3, width=4, height=5, x=1)
        self.assertEqual(b1.x, 1)

        b1.update(id=3, width=4, height=5, x=1, y=2)
        self.assertEqual(b1.y, 2)

    def test_create(self):
        b1 = Rectangle.create(id=3, width=4, height=5)
        self.assertEqual(b1.height, 5)

        b1 = Rectangle.create(id=3, width=4, height=5, x=1)
        self.assertEqual(b1.x, 1)

        b1 = Rectangle.create(id=3, width=4, height=5, x=1, y=2)
        self.assertEqual(b1.y, 2)

    def test_save_to_file(self):
        if os.path.exists('Rectangle.json'):
            os.remove('Rectangle.json')
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")
        if os.path.exists('Rectangle.json'):
            os.remove('Rectangle.json')
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")
        Rectangle.save_to_file([self.b1])
        self.assertEqual(Rectangle.load_from_file()[0].to_dictionary(),
                         self.b1.to_dictionary())

    def test_load_from_file(self):
        if os.path.exists('Rectangle.json'):
            os.remove('Rectangle.json')
        list_objs = Rectangle.load_from_file()
        self.assertEqual(list_objs, [])
        Rectangle.save_to_file([self.b1])
        list_objs = Rectangle.load_from_file()
        self.assertEqual(list_objs[0].to_dictionary(), self.b1.to_dictionary())

    def test_display(self):
        co = io.StringIO()
        sys.stdout = co
        Rectangle(2, 3).display()
        self.assertEqual(co.getvalue(), """##
##
##
""")
        co = io.StringIO()
        sys.stdout = co
        Rectangle(2, 3, 2).display()
        self.assertEqual(co.getvalue(), """  ##
  ##
  ##
""")
        co = io.StringIO()
        sys.stdout = co
        Rectangle(2, 3, y=2).display()
        self.assertEqual(co.getvalue(), """

##
##
##
""")
        co = io.StringIO()
        sys.stdout = co
        Rectangle(2, 3, 2, 2).display()
        self.assertEqual(co.getvalue(), """

  ##
  ##
  ##
""")
