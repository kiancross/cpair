#
# Copyright (C) 2021 Kian Cross
#

import unittest

from cpair import Point


class TestPoint(unittest.TestCase):
    def test_repr(self):
        p = Point(3, 4)
        self.assertEqual(repr(p), "(x=3.000000, y=4.000000)")

    def test_sub_valid(self):
        p = Point(3, 4)
        q = Point(1, 1)

        self.assertTrue(p - q == Point(2, 3))

    def test_sub_invalid(self):
        p = Point(3, 4)

        self.assertRaises(ValueError, lambda: p - 1)

    def test_equals_valid(self):
        p = Point(3, 4)
        q = Point(3, 4)

        self.assertTrue(p == q)

    def test_equals_invalid(self):
        p = Point(3, 4)

        self.assertRaises(ValueError, lambda: p == 1)

    def test_abs(self):
        p = Point(3, 4)
        self.assertEqual(abs(p), 5)

    def test_distance(self):
        p = Point(3, 4)
        q = Point(-3, -4)

        self.assertEqual(p.distance(q), 10)
