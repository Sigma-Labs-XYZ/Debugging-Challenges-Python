import unittest
from challenges.c1 import c1
from challenges.c2 import c2


class Tests(unittest.TestCase):
    def test_c1(self):
        assert c1() == 2

    def test_c2(self):
        assert c2() == 120


if __name__ == "__main__":
    unittest.main()
