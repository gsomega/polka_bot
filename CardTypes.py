from enum import IntEnum
from enum import Enum

class Suit(Enum):
    CLUB = "CLUB"
    SPADE = "SPADE"
    DIAMOND = "DIAMOND"
    HEART = "HEART"

class Rank(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14
    # TWO = "TWO"
    # THREE = "THREE"
    # FOUR = "FOUR"
    # FIVE = "FIVE"
    # SIX = "SIX"
    # SEVEN = "SEVEN"
    # EIGHT = "EIGHT"
    # NINE = "NINE"
    # TEN = "TEN"
    # JACK = "JACK"
    # QUEEN = "QUEEN"
    # KING = "KING"
    # ACE = "ACE"


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.number = rank