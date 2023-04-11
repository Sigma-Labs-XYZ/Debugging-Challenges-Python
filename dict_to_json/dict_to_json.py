# This is a program to save a python dictionary as a json
# Do not edit this code, the aim is to debug!

from typing import Dict


def get_return_message(
    status_code: int, status_message: str, content: object
) -> Dict[str, object]:
    """Formats a return message

    Args:
        status_code (int): 200 if successful 400 if not
        status_message (str): Message that caused outcome
        content (object): Function content

    Returns:
        Dict[str,object]: Dictionary of with keys identical to the argument names.
    """
    return {
        "status_code": status_code,
        "status_message": status_message,
        "content": content,
    }


def dict_to_json(
    input_dictionary: Dict[object, object], file_path: str
) -> Dict[str, object]:
    """Saves a dictionary as a JSON to a desired location

    Args:
        input_dictionary (Dict[object, object])
        file_path (str)

    Returns:
        Dict[str, object]: Response dictionary (see the `get return message` function)
    """
    try:
        with open(file_path, "r") as json_file:
            json.dump(input_dictionary, json_file, indent=2)
        return get_return_message(
            status_code=200,
            status_message=f"Dictionary successfully converted to json and saved to {file_path}",
            content=,
        )

    except Exception as e:
        return get_return_message(
            status_code=400,
            status_message=f'The dictionary was not converted into a json, /n stack trace's: {e}',
            content=None,
        )


if __name__ == "__main__":
    test = {
        "status": "test",
        "severity": 500,
        "messages": {"description": "this is a test", "assets": [1, 4, 2, 5]},
    }
    response = dict_to_json(test, "./expected_output.json")
    print(response)
