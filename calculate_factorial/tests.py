from calculate_factorial import calculate_factorial
import unittest


class Tests(unittest.TestCase):
    def test(self):
        self.assertEqual(calculate_factorial(5), 120)


if __name__ == "__main__":
    unittest.main()
