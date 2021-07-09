from CardTypes import Suit, Rank
from Deck import StandardDeck
from typing import List

class Game:
    def __init__(self):
        self.deck = StandardDeck()
        self.board = []
        self.pot_size: float = 0
        self.players: List[Player]

class TexasHoldem(Game):
    def __init__(self):
        super().__init__()

    #list of active players

    #who is the action on? how is action passed?

    #starting player

    #who is the last person to raise

    #how does a side-pot work?
    #this means we need to keep track of how much each player has put in




class Player:
    def __init__(self, game: Game, name: str, money: float):
        self.game = game
        self.name = name
        self.money = money
        self.hand: List[Card] = []

    def bid(self, bid_amount: float, call_amount: float = 0):
        if bid_amount < call_amount:
            print("Need to match call")
            return
        if bid_amount >= self.money:
            print("All in!")
            bid_amount = self.money
        self.game.pot_size += bid_amount
        self.money -= bid_amount

    def fold(self):
        print("Folding")


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.number = rank