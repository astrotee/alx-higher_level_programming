#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_serializer(self):
        jd = Base.to_json_string(None)
        self.assertEqual(jd, "[]")
        jd = Base.to_json_string([])
        self.assertEqual(jd, "[]")
        jd = Base.to_json_string([{'id': 45}])
        self.assertEqual(jd, "[{\"id\": 45}]")

    def test_deserializer(self):
        jd = Base.from_json_string(None)
        self.assertEqual(jd, [])
        jd = Base.from_json_string("[]")
        self.assertEqual(jd, [])
        jd = Base.from_json_string("[{\"id\": 45}]")
        self.assertEqual(jd, [{'id': 45}])
