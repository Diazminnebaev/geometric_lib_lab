import unittest
from triangle import area, perimeter

class TestTriangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(4, 3), 6)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            perimeter(1, 2, 100)

    def test_negative(self):
        with self.assertRaises(ValueError):
            area(-1, 2)

# if __name__ == "__main__":
#     unittest.main()

