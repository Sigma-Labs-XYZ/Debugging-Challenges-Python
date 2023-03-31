from remove_parentheses import remove_parentheses
import unittest


class Tests(unittest.TestCase):
    def test(self):
        self.assertEqual(
            remove_parentheses("example(unwanted thing)example"),
            "exampleexample",
        )


if __name__ == "__main__":
    unittest.main()
