import unittest
from challenges.c1 import c1
from challenges.c2 import c2
from challenges.c3 import (
    Game,
    Coordinates,
    GameAlreadyFinishedError,
    InvalidCoordinatesError,
    Marker,
    SquareAlreadyOccupiedError,
    Outcome,
)


class Tests(unittest.TestCase):
    def test_c1(self):
        self.assertEqual(c1(), 1)

    def test_c2(self):
        self.assertEqual(c2(), 120)

    def test_c3_1(self):
        game = Game()
        self.assertEqual(
            game.frame,
            [
                [None, None, None],
                [None, None, None],
                [None, None, None],
            ],
        )

    def test_c3_2(self):
        all_lines = [
            # Rows
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            # Columns
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            # Diagonals
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]

        def get_coordinates(line):
            return sorted([Coordinates(x, y) for x, y in line])

        game = Game()
        self.assertEquals(
            sorted(list(map(get_coordinates, all_lines))),
            sorted([sorted(line) for line in game.get_all_lines()]),
        )

    def test_c3_3(self):
        game = Game()
        game.place_marker(Coordinates(1, 0), Marker.O)
        self.assertEquals(
            game.frame,
            [
                [None, Marker.O, None],
                [None, None, None],
                [None, None, None],
            ],
        )

    def test_c3_4(self):
        game = Game()
        with self.assertRaises(InvalidCoordinatesError):
            game.place_marker(Coordinates(0, 3), Marker.O)

    def test_c3_5(self):
        game = Game()
        game.place_marker(Coordinates(0, 0), Marker.O)
        with self.assertRaises(SquareAlreadyOccupiedError):
            game.place_marker(Coordinates(0, 0), Marker.X)

    def test_c3_6(self):
        game = Game()
        game.place_marker(Coordinates(0, 0), Marker.X)
        game.place_marker(Coordinates(0, 1), Marker.O)
        game.place_marker(Coordinates(1, 0), Marker.X)
        game.place_marker(Coordinates(0, 2), Marker.O)
        game.place_marker(Coordinates(2, 0), Marker.X)
        self.assertEquals(game.get_game_outcome(), (Outcome.Win, Marker.X))

    def test_c3_7(self):
        game = Game()
        game.frame = [
            [Marker.O, Marker.O, Marker.X],
            [Marker.X, Marker.X, Marker.O],
            [Marker.X, Marker.O, Marker.X],
        ]
        self.assertEquals(game.get_game_outcome(), (Outcome.Win, Marker.X))

    def test_c3_8(self):
        game = Game()
        game.frame = [
            [None, None, Marker.X],
            [Marker.X, Marker.X, None],
            [Marker.O, Marker.O, Marker.O],
        ]
        self.assertEquals(game.get_game_outcome(), (Outcome.Win, Marker.O))

    def test_c3_9(self):
        game = Game()
        game.frame = [
            [Marker.O, Marker.X, Marker.X],
            [Marker.X, Marker.O, Marker.O],
            [Marker.X, Marker.O, Marker.X],
        ]
        self.assertEquals(game.get_game_outcome(), (Outcome.Draw, None))

    def test_c3_10(self):
        game = Game()
        game.frame = [
            [Marker.O, Marker.O, Marker.X],
            [Marker.X, None, Marker.O],
            [Marker.X, Marker.X, Marker.O],
        ]
        self.assertEquals(game.get_game_outcome(), None)

    def test_c3_11(self):
        game = Game()
        game.frame = [
            [Marker.X, Marker.O, None],
            [Marker.X, Marker.O, None],
            [Marker.X, None, None],
        ]
        with self.assertRaises(GameAlreadyFinishedError):
            game.place_marker(Coordinates(2, 0), Marker.O)


if __name__ == "__main__":
    unittest.main()
