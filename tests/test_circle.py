import unittest
import math
from circle import area, perimeter

class TestCircle(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_two(self):
        self.assertAlmostEqual(area(2), 4 * math.pi, places=10)

    def test_perimeter_two(self):
        self.assertAlmostEqual(perimeter(2), 4 * math.pi, places=10)

    def test_negative(self):
        with self.assertRaises(ValueError):
            area(-1)
