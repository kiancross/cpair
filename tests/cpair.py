#
# Copyright (C) 2021 Kian Cross
#

import unittest

from cpair import Point, closest_pair


class TestClosestPair(unittest.TestCase):
    def test_two(self):
        points = [Point(0, 0), Point(0, 1)]

        self.assertEqual(closest_pair(points), 1)

    def test_on_line(self):
        points = [Point(0, 9), Point(0, 1), Point(0, 4), Point(0, 10)]

        self.assertEqual(closest_pair(points), 1)

    def test_duplicates(self):
        points = [Point(1, 1), Point(1, 1), Point(1, 1), Point(1, 1)]

        self.assertEqual(closest_pair(points), 0)

    def test_strip_hit(self):
        points = [Point(0, -1), Point(0, 0.1), Point(0, -0.1), Point(0, 1)]

        self.assertEqual(closest_pair(points), 0.2)

    def test_strip_miss(self):
        points = [Point(0, -1), Point(0, 0.1), Point(0, 10), Point(0, 1)]

        self.assertEqual(closest_pair(points), 0.9)

    def test_large(self):
        points = (
            [Point(-1, -1)] + [Point(i, i) for i in range(0, 100, 2)] + [Point(-1, -2)]
        )

        self.assertEqual(closest_pair(points), 1)
