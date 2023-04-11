# This is a simple game of snap that is played by the computer
# The game is not working if the same person wins every time the game is played.
# Do not edit this code, the aim is to debug! 

import random

class Snap:
    """
    A class representing a Snap card game.
    
    Attributes:
        deck (List[Tuple[str, str]]): A list of tuples representing the deck of cards,
            where the first element is the card's rank and the second element is the card's suit.
        players (List[str]): A list of player names.
        hands (dict): A dictionary representing the hands of each player,
            where the keys are player names and the values are lists of card tuples.
    """
    
    def __init__(self, deck: List[Tuple[str, str]], players: List[str]) -> None:
        """
        Initializes a new Snap game instance.
        
        Args:
            deck (List[Tuple[str, str]]): A list of tuples representing the deck of cards,
                where the first element is the card's rank and the second element is the card's suit.
            players (List[str]): A list of player names.
        """
        self.deck = deck
        # random.shuffle(self.deck) 
        self.players = players
        self.hands = {player: [] for player in players}
    
    def deal() -> None: 
        """
        Deals the cards to the players.
        """
        num_players = len(self.players)
        num_cards = len(self.deck) // num_players
        for i, player in enumerate(self.players):
            start = i * num_cards
            end = start + num_cards
            self.hands[player] = self.deck[start:end]
    
    def play_round(self) -> str: 
    """
    Plays a single round of Snap.
    
    Returns:
        str: The name of the player who won the round, or None if there was no winner.
    """
    cards_played = [self.hands[player].pop(0) for player in self.players]
    ranks_played = [card[0] for card in cards_played]
    if len(set(ranks_played)) == 1:
        return None
    else:
        return self.players[ranks_played.index(max(ranks_played))]

if __name__ == "__main__":
    # Create the deck using loops
    deck = []
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    for rank in ranks:
        for suit in suits:
            card = (rank, suit)
            deck.append(card)

    # Create a Snap instance with the deck and players
    players = ['Alice', 'Bob', 'Charlie']
    game = Snap(deck, players)

    # Deal the cards to the players
    game.deal()

    # Play a round of Snap
    winner = game.play_round()

    # Print the winner
    if winner is None:
        print("No one won this round.")
    else:
        print(f"{winner} won this round!")
