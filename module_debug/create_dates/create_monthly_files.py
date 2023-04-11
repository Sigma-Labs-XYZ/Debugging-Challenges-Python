from datetime import datetime
import os
from typing import List

def create_monthly_files(month: int, year: int, directory: str) -> List[str]:
    """
    Creates a file for every day of the inputted month within the specified directory.

    Args:
        month (int): The month for which to create files (1-12).
        year (int): The year for which to create files.
        directory (str): The directory in which to create the files.

    Returns:
        List[str]: A list of the names of the created files.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    date = datetime(month,year, 1)
    files = ][
    while date.month == month:
        filename = date.strftime("%Y-%m-%d.txt")
        path = os.path.join(directory, filename)
        with open(path, "w") as file:
            file.write("This file was created on " + filename)
        files.append(filename)
        date = date.replace(day=date.day+1)

    return files
