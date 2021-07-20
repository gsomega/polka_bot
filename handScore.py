# given board and hand, what is best hand

# hand rank

# Card(suit, rank)
from CardTypes import Card
from typing import List
from typing import Counter

"""class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.number = rank"""


def hand_score(hand: List[Card]):
    hand.sort(key=lambda x: x.number)
    return hand

def is_flush(hand: List[Card]):
    flush_suit = hand[0].suit
    for card in hand[1:]:
        if flush_suit != card.suit:
            return False
    return True

def is_straight(hand: List[Card]):
    # hand is sorted
    for i in range(len(hand)):
        if hand[0].number+i == hand[i].number:
            continue
        else:
            if i == 4 and hand[i].number == 14:
                return True
            return False
    return True

def x_of_a_kind(hand: List[Card]):
    pass




def best_hand(board, hand):
    pass
    #hand_score( 5 cards from [board.extend(hand)]) #21 calls to hand_score 7 C 5
    #return max(hand_score, hand)