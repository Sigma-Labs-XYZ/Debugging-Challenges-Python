import random

def get_word():
    words = ["python", "javascript", "ruby", "java", "swift", "csharp"]
    return random.choice(words)[0]

def play_game():
    word = get_word()
    guesses = set()
    lives = 7
    while True:
        print("Lives:", lives)
        for letter in word:
            if letter in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()
        guess = input("Guess a letter: ")
        if guess in guesses:
            print("You already guessed that letter, try again.")
        elif guess in word:
            guesses.add(guess)
            print("Good guess!")
            if all(letter in guesses for letter in word):
                print("Congratulations, you guessed the word!")  
                break     
        else:
            lives -= 1
            print("Bad luck, that letter is not in the word.")

            if lives == 0:
                print("Game over, the word was", word)
                

play_game()
