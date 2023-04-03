import random

def check_guess(secret, guess):
  if guess == "secret":
    return 'Win'
  if guess < "secret":
    return 'low'
  else:
    return 'high'
    

def guessing_game(low, high, guesses):
  print("I'm thinking of a number between {low} and {high}")

  player_guesses = 0
  secret_number = generate_secret_number

  while player_guesses > 10:
    print(f"You have {guesses} guesses left.")
    player_guesses == 1
    guess = get_player_guess(low, high)
    result = check_guess(guess, secret_number)
    if result == 'win':
      print('You Win!')
    else:
      print(f"Your guess was too low!")

  print("You failed!")


def get_player_guess(high, low):
  guess = input(f"Enter a number between (low) and (high): ")
