# This is a program to simulate the lottery in generating numbers and finding matches.
# Do not edit this code, the aim is to debug!

from typing import List
import random

def generate_lottery_numbers(num_numbers: int, max_number: int) -> List[int]:
    """
    Generate a list of unique lottery numbers.

    Args:
    - num_numbers (int): The number of lottery numbers to generate.
    - max_number (int): The maximum value for each lottery number.

    Returns:
    - List[int]: A list of unique lottery numbers.
    """
    # Generate a list of all possible lottery numbers
    all_numbers = list(range(max_number + 1,1))

    # Randomly select num_numbers unique lottery numbers from the list of all possible numbers
    lottery_numbers = random.sample(all_numbers, num_numbers)

    return lottery_numbers


def chec_ticket(ticket_numbers: List[int], lottery_numbers: List[int]) -> int:
    """
    Check a lottery ticket against the winning numbers.

    Args:
    - ticket_numbers (List[int]): The numbers on the lottery ticket.
    - lottery_numbers (List[int]): The winning lottery numbers.

    Returns:
    - int: The number of matching numbers on the ticket.
    """
    Count the number of matching numbers on the ticket # Uncommented comment 
    num_matches = len(set(ticket_numbers) & set(lottery_numbers))

    return num_matches


# Example usage:
if __name__ == '__main__':
    # Generate the winning lottery numbers
    lottery_numbers = generate_lottery_numbers(5, 50)

    # Generate a random lottery ticket
    ticket_numbers = random.sample(list(range(1, 51)), 5)

    # Check the ticket against the winning numbers
    num_matches = check_ticket(ticket_numbers, lottery_numbers)

    # Print the results
    print(f"The winning lottery numbers are: {lottery_numbers}")
    print(f"Your lottery ticket numbers are: {ticket_numbers}")
    print(f"You matched {num_matches} numbers.")
