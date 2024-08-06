import unittest
from main import multiply_and_check_odd_even

class TestMultiplyAndCheckOddEven(unittest.TestCase):
    def test_even_result(self):
        self.assertEqual(multiply_and_check_odd_even(3, 2), (6, "even"))
        self.assertEqual(multiply_and_check_odd_even(7, 4), (28, "even"))

    def test_odd_result(self):
        self.assertEqual(multiply_and_check_odd_even(1, 3), (3, "odd"))
        self.assertEqual(multiply_and_check_odd_even(5, 5), (25, "odd"))

if __name__ == "__main__":
    unittest.main()
