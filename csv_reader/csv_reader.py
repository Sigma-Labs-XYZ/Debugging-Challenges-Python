# You need to create a function that parses a .txt file that is csv-formatted
# into a dataframe-like python object

# Your function should return columns with correct types. If the type of the column
# can not be inferred as the same throughout, e.g. int, the column should default to str.

# Lists should only be typed if the types they contain are homogenous.
# e.g. 30|fifty should default to List[str], 30|20 can be List[int]

# Check every piece of data in a column/array to make sure the types are homogenous

# Don't worry about edge cases: just get tests passing

# Copy parse_csv into ChatGPT to get an overview of the helper functions.

from types import NoneType
from typing import (
    NewType,
    Any,
    List,
    Optional,
    Dict,
    TypeVar,
    Union,
    Literal,
    Type,
)

Column = Union[
    List[Optional[str]],
    List[Optional[int]],
    List[Optional[float]],
    List[Optional[List[Optional[str]]]],
    List[Optional[List[Optional[int]]]],
    List[Optional[List[Optional[float]]]],
    List[Optional[List[None]]],
]

DataFrame = Dict[str, Column]


class InvalidNumberOfColumnsError(Exception):
    pass


def parse_csv(text: List[str]) -> DataFrame:
    if text in ([], [""]):
        return {}

    def represent_type(t: Type[float | int], s: str) -> bool:
        try:
            t(s)
        except ValueError:
            return False
        return True

    class TypeRepresentation:
        def __init__(
            self, type: Type[NoneType | str | int | float], is_list: bool
        ):
            self.type = type
            self.is_list = is_list

        def __eq__(self, other):
            return self.type is other.type and self.is_list is other.is_list

        def __repr__(self):
            return f"({self.type}, {self.is_list})"

    def get_value_type(
        value: str,
    ) -> Type[NoneType | str | int | float]:
        if value in ("None", ""):
            return NoneType
        for type in [int, float]:
            if represent_type(type, value):
                return type

        return str

    def get_type_representation(value: str) -> TypeRepresentation:
        first_type_pass = get_value_type(value)
        if first_type_pass is not str:
            return TypeRepresentation(first_type_pass, False)

        if "|" not in value:
            return TypeRepresentation(str, False)

        value_types = [get_value_type(value) for value in value.split("|")]

        for meta_type in [NoneType, str, float, int]:
            if all(
                value_type is meta_type or value_type is NoneType
                for value_type in value_types
            ):
                return TypeRepresentation(meta_type, True)

        return TypeRepresentation(str, True)

    def reduce_type_representations(
        types: List[TypeRepresentation],
    ) -> TypeRepresentation:
        first_non_none_type: TypeRepresentation | None = None
        is_array_column: bool = False
        for value_type in types:
            if first_non_none_type is None and value_type.type is not NoneType:
                first_non_none_type = value_type

            if (
                first_non_none_type is not None
                and value_type.type is not NoneType
                and first_non_none_type != value_type
            ):
                return TypeRepresentation(str, False)
            is_array_column = is_array_column and value_type.is_list

        return first_non_none_type or TypeRepresentation(
            NoneType, is_array_column
        )

    def cast_value_to_type(
        value: str, type_representation: TypeRepresentation
    ) -> (
        None
        | str
        | int
        | float
        | List[str]
        | List[int]
        | List[float]
        | List[None]
    ):
        if value in ("", "None"):
            return None
        if type_representation.is_list:
            split_value = value.split("|")

            if type_representation.type is NoneType:
                return [None for _ in split_value]
            if type_representation.type is str:
                return split_value
            return [
                type_representation.type(item)  # type: ignore
                if item not in ("", "None")
                else None
                for item in split_value  # type: ignore
            ]  # type: ignore

        if type_representation.type is NoneType:
            return None
        if type_representation.type is str:
            return value

        return type_representation.type(value)  # type: ignore

    def coerce_column_type(column: list[str]):
        type_representations = [
            get_type_representation(value) for value in column
        ]
        reduced_type = reduce_type_representations(type_representations)
        return [cast_value_to_type(value, reduced_type) for value in column]

    def get_untyped_dataframe() -> Dict[str, List[str]]:
        column_names = text[0].split(",")
        number_of_columns = len(column_names)

        columns: List[List] = [[] for column in column_names]
        for i, row in enumerate(text[1:]):
            split_row = row.split(",")
            if len(split_row) != number_of_columns:
                raise InvalidNumberOfColumnsError(f"Row number: {i + 1}")
            for column_number in range(len(columns)):
                columns[column_number].append(split_row[column_number])
        return {
            column_name: columns[i]
            for i, column_name in enumerate(column_names)
        }

    return {
        column_name: coerce_column_type(column)
        for column_name, column in get_untyped_dataframe().items()
    }
