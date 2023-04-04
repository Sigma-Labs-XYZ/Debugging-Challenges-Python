import unittest
from book_query import get_proximity_records


class Tests(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(
            get_proximity_records(
                [
                    ["abba", "abba"],
                    ["baab", "abba", "baab"],
                    ["ABBA", "BAAB", "ABBA", "BAAB", "CAAB"],
                    ["a", "b", "c", "d"],
                    ["e"],
                ]
            ),
            [
                ("a", "b", 0.0),
                ("b", "c", 0.0),
                ("c", "d", 0.0),
                ("abba", "baab", 0.3333333333333333),
                ("abba", "abba", 0.5),
                ("a", "c", 1.0),
                ("b", "d", 1.0),
                ("baab", "baab", 1.0),
                ("baab", "caab", 1.0),
                ("a", "d", 2.0),
                ("abba", "caab", 2.0),
            ],
        )


if __name__ == "__main__":
    unittest.main()
