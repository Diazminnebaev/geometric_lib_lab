import unittest
from rectangle import area, perimeter

class TestRectangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3, 4), 12)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4), 14)

    def test_zero(self):
        self.assertEqual(area(10, 0), 0)

    def test_negative(self):
        with self.assertRaises(ValueError):
            area(-1, 2)

# if __name__ == "__main__":
#     unittest.main()

