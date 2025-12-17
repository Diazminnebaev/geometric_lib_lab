import unittest
from square import area, perimeter

class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3), 9)

    def test_perimeter(self):
        self.assertEqual(perimeter(3), 12)

    def test_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-3)

# if __name__ == "__main__":
#     unittest.main()

