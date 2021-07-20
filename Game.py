from typing import List

from Deck import StandardDeck
from Player import Player


class Game:
    def __init__(self):
        self.deck = StandardDeck()
        self.board = []
        self.pot_size: float = 0
        self.players: List[Player] = []
        self.call_amount: float = 0


class Agent:
    def __init__(self, player: Player):
        self.player = player