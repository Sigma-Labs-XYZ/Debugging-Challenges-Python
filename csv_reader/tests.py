import unittest
from csv_reader import parse_csv


class Tests(unittest.TestCase):
    def test_ints(self):
        result = parse_csv(["one,two,three", "1,2,3"])
        self.assertEqual(result, {"one": [1], "two": [2], "three": [3]})

    def test_floats(self):
        result = parse_csv(["one,two,three", "1.0,2.2,3.3"])
        self.assertEqual(result, {"one": [1.0], "two": [2.2], "three": [3.3]})

    def test_int_float_mix(self):
        result = parse_csv(["one", "1.0", "1.2", "1"])
        self.assertEqual(result, {"one": ["1.0", "1.2", "1"]})

    def test_int_arrays(self):
        result = parse_csv(["one", "1|1|2|3"])
        self.assertEqual(result, {"one": [[1, 1, 2, 3]]})

    def test_arrays_none(self):
        result = parse_csv(["one", "1||||1"])
        self.assertEqual(result, {"one": [[1, None, None, None, 1]]})

    def test_arrays_none_mk2(self):
        result = parse_csv(["one,two", "None,None"])
        self.assertEqual(result, {"one": [None], "two": [None]})

    def test_arrays_float(self):
        result = parse_csv(["one", "5.5|3.4"])
        self.assertEqual(result, {"one": [[5.5, 3.4]]})

    def test_pure_nones(self):
        result = parse_csv(["one", ""])
        self.assertEqual(result, {"one": [None]})

    def test_empty_csv(self):
        result = parse_csv([""])
        self.assertEqual(result, {})

    def test_empty_csv_mk2(self):
        result = parse_csv([])
        self.assertEqual(result, {})

    def test_mixed_csv(self):
        result = parse_csv(
            [
                "column_1,column_2,column_3",
                "89,2.02,1|None|6|None",
                "29,5.1,5|None|4|None",
                "70,4.62,5|None|3|None",
                "87,9.37,",
                "73,1.75,",
                "64,9.27,10|None|4|None",
                "70,2.64,7|None|6|None",
                "95,2.28,10|None|4|None",
                "92,2.58,",
                "79,7.02,",
            ]
        )
        self.assertEqual(
            result,
            {
                "column_1": [89, 29, 70, 87, 73, 64, 70, 95, 92, 79],
                "column_2": [
                    2.02,
                    5.1,
                    4.62,
                    9.37,
                    1.75,
                    9.27,
                    2.64,
                    2.28,
                    2.58,
                    7.02,
                ],
                "column_3": [
                    [1, None, 6, None],
                    [5, None, 4, None],
                    [5, None, 3, None],
                    None,
                    None,
                    [10, None, 4, None],
                    [7, None, 6, None],
                    [10, None, 4, None],
                    None,
                    None,
                ],
            },
        )


if __name__ == "__main__":
    unittest.main()
