import unittest
from tower_builder import tower_builder


class Tests(unittest.TestCase):
    def test(self):
        self.assertEqual(tower_builder(3), ["  *  ", " *** ", "*****"])


if __name__ == "__main__":
    unittest.main()
