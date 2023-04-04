import random


class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value}{self.suit}"


class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in ["♠", "♣", "♦", "♥"]
                      for v in "23456789TJQKA"]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_of_cards):
        [self.cards.pop() for _ in range(num_of_cards)]


class PokerHand:
    def __init__(self):
        self.cards = []

    def __repr__(self):
        return ", ".join(map(str, self.cards))

    def add_cards(self, new_cards):
        self.cards = self.cards + new_cards


player_hand = PokerHand()
computer_hand = PokerHand()


def poker_game():
    print("Welcome to the 5-Card Draw Poker Game!\n")

    while True:
        deck = Deck()
        deck.shuffle()

        player_hand.add_cards(deck.deal(5))
        computer_hand.add_cards(deck.deal(5))

        print(f"Your hand: {player_hand}")
        cards_to_replace = input(
            "Enter the card positions (1-5) to replace, separated by spaces, or press enter to keep all: ")

        if cards_to_replace:
            replacement_positions = list(map(int, cards_to_replace.split()))
            for pos in replacement_positions:
                player_hand.cards[pos] = deck.deal(1)[0]

        print(f"Your new hand: {player_hand}")

        # This simple game does not have hand evaluation logic, so the winner is decided randomly.
        winner = random.choice(["player", "computer"])

        if winner == "player":
            print("Congratulations! You won!")
        else:
            print("Sorry, you lost. Better luck next time!")

        print(f"Computer hand: {computer_hand}\n")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    poker_game()
