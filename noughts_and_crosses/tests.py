from noughts_and_crosses import (
    Game,
    Coordinates,
    GameAlreadyFinishedError,
    InvalidCoordinatesError,
    Marker,
    SquareAlreadyOccupiedError,
    Outcome,
)
import unittest


class Tests(unittest.TestCase):
    def test_game_frame_init(self):
        game = Game()
        self.assertEqual(
            game.frame,
            [
                [None, None, None],
                [None, None, None],
                [None, None, None],
            ],
        )

    def test_get_all_lines(self):
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
        self.assertEqual(
            sorted(list(map(get_coordinates, all_lines))),
            sorted([sorted(line) for line in game.get_all_lines()]),
        )

    def test_place_single_marker(self):
        game = Game()
        game.place_marker(Coordinates(1, 0), Marker.O)
        self.assertEqual(
            game.frame,
            [
                [None, Marker.O, None],
                [None, None, None],
                [None, None, None],
            ],
        )

    def test_incorrect_coordinate_error(self):
        game = Game()
        with self.assertRaises(InvalidCoordinatesError):
            game.place_marker(Coordinates(0, 3), Marker.O)

    def test_square_already_occupied_error(self):
        game = Game()
        game.place_marker(Coordinates(0, 0), Marker.O)
        with self.assertRaises(SquareAlreadyOccupiedError):
            game.place_marker(Coordinates(0, 0), Marker.X)

    def test_game_win_top_row(self):
        game = Game()
        game.place_marker(Coordinates(0, 0), Marker.X)
        game.place_marker(Coordinates(0, 1), Marker.O)
        game.place_marker(Coordinates(1, 0), Marker.X)
        game.place_marker(Coordinates(0, 2), Marker.O)
        game.place_marker(Coordinates(2, 0), Marker.X)
        self.assertEqual(game.get_game_outcome(), (Outcome.Win, Marker.X))

    def test_diagonal_win(self):
        game = Game()
        game.frame = [
            [Marker.O, Marker.O, Marker.X],
            [Marker.X, Marker.X, Marker.O],
            [Marker.X, Marker.O, Marker.X],
        ]
        self.assertEqual(game.get_game_outcome(), (Outcome.Win, Marker.X))

    def test_bottom_row_win(self):
        game = Game()
        game.frame = [
            [None, None, Marker.X],
            [Marker.X, Marker.X, None],
            [Marker.O, Marker.O, Marker.O],
        ]
        self.assertEqual(game.get_game_outcome(), (Outcome.Win, Marker.O))

    def test_draw(self):
        game = Game()
        game.frame = [
            [Marker.O, Marker.X, Marker.X],
            [Marker.X, Marker.O, Marker.O],
            [Marker.X, Marker.O, Marker.X],
        ]
        self.assertEqual(game.get_game_outcome(), (Outcome.Draw, None))

    def test_ongoing_game(self):
        game = Game()
        game.frame = [
            [Marker.O, Marker.O, Marker.X],
            [Marker.X, None, Marker.O],
            [Marker.X, Marker.X, Marker.O],
        ]
        self.assertEqual(game.get_game_outcome(), None)

    def test_game_already_finished_error(self):
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
