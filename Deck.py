from Dealer import Card
from typing import List
from CardTypes import Suit, Rank
import random

class Deck:
    def __init__(self):
        pass

    def draw(self):
        pass

    def shuffle(self):
        pass

    def discard(self):
        pass

class StandardDeck(Deck):
    def __init__(self):
        self.deck_pile = self._create_desklist()
        self.discard_pile: List[Card] = []

    def _create_desklist(self) -> List[Card]:
        decklist = []
        for suit in Suit:
            for rank in Rank:
                decklist.append(Card(suit, rank))
        self.shuffle(decklist)
        return decklist

    def draw(self) -> Card:
        # if deck is (near) empty, shuffle discard into deck
        if len(self.deck_pile) <= 1:
            self.deck_pile.extend(self.discard_pile)
            self.discard_pile = []
            self.shuffle()
        return self.deck_pile.pop()

    def shuffle(self):
        random.shuffle(self.deck_pile)

    def discard(self, card: Card):
        self.discard_pile.append(card)