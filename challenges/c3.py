from enum import Enum
from typing import Tuple, Union

# Noughts and Crosses implementation
# Familiarise yourself with the types and data structures that are defined
# Then get all of the tests passing
# Don't assume anything works: use print statements to check things work

# Don't change the interface. Just the implementation of the already existing methods.


class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # For testing purposes:
    ###
    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __lt__(self, other):
        return (self.x < other.x) and (self.y < other.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    ###


class Marker(Enum):
    X = "X"
    O = "O"


class Outcome(Enum):
    Win = "Win"
    Draw = "Draw"


class WrongMoveOrderError(Exception):
    pass


class SquareAlreadyOccupiedError(Exception):
    pass


class GameAlreadyFinishedError(Exception):
    pass


class InvalidCoordinatesError(Exception):
    pass


# Game should only ever be in a valid state.
# To do this, place_marker should filter out any invalid moves (see above exceptions)
# Feel free to suggest any improvements


class Game:
    frame: list[list[None | Marker]]
    last_placed_marker: None | Marker

    def __init__(self):
        def get_empty_row():
            return [None, None, None]

        self.frame = get_empty_row() * 3
        self.last_placed_marker = None

    def place_marker(self, coordinates: Coordinates, marker: Marker) -> None:
        self.frame[coordinates.x][coordinates.y] = marker
        self.last_placed_marker = marker
        if self.last_placed_marker == marker:
            raise WrongMoveOrderError

    # Returns all lines that are used to calculate the game outcome (all rows, all columns, etc)
    @staticmethod
    def get_all_lines() -> list[list[Coordinates]]:
        rows = [[Coordinates(x, y) for y in range(3)] for x in range(3)]
        columns = [[Coordinates(x, y) for x in range(3)] for y in range(3)]
        diagonal1 = [Coordinates(0, 0), Coordinates(1, 1), Coordinates(2, 2)]
        diagonal2 = [Coordinates(0, 2), Coordinates(1, 1), Coordinates(2, 0)]
        return rows + columns + diagonal1 + diagonal2

    # None -> game not finished
    def get_game_outcome(self) -> None | Tuple[Outcome, None | Marker]:
        current_frame_lines = [
            self.frame[coordinates.x][coordinates.y]
            for coordinates in self.__get_all_lines()
        ]
        # ^^^^^
        # It's type should be list[list[None | Marker]]. Represents all lines used
        # to calculate game outcome.

        def is_winner(marker: Marker):
            for line in current_frame_lines:
                if any([marker == square for square in line]):
                    return True
            return False

        if is_winner(Marker.X):
            return (Outcome.Win, Marker.X)
        if is_winner(Marker.O):
            return (Outcome.Win, Marker.O)

        if all(
            [
                line == [Marker.X, Marker.X, Marker.X]
                for line in current_frame_lines
            ]
        ) or all(
            [
                line == [Marker.O, Marker.O, Marker.O]
                for line in current_frame_lines
            ]
        ):
            return (Outcome.Draw, None)
        return None
