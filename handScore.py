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

def is_flush(hand: List[Card]):
    flush_suit = hand[0].suit
    for card in hand[1:]:
        if flush_suit != card.suit:
            return False
    return True

def is_straight(hand: List[Card]):
    # hand is sorted
    for i in range(5):
        if hand[0].number+i == hand[i].number:
            continue
        else:
            if i == 4 and hand[i].number == 14:
                return True
            return False
    return True

def x_of_a_kind(hand: List[Card]):
    """x of a kind returns:
    [power level,
    cards related to power level (in decreasing order) (full house trips first),
    kickers (in decreasing order)]"""
    counts = [0 for i in range(15)]
    for i in range(5):
        counts[hand[i].number] += 1
    if 4 in counts:
        kind = counts.index(4)
        kicker = counts.index(1)
        return [3,kind,kicker] #4 of a kind

    elif 3 in counts:
        trip = counts.index(3)
        if 2 in counts:
            pair = counts.index(2)
            return [4,trip,pair] #full house
        else:
            kicker2 = counts.index(1)
            kicker1 = counts[kicker2+1:].index(1)
            return [7,trip, kicker1, kicker2] #3 of a kind

    elif 2 in counts:
        pair = counts.index(2)
        if 2 in counts[pair+1:]:
            pair2 = counts[pair+1:].index(2)
            kicker = counts.index(1)
            return [8,pair2,pair,kicker] #2 pair
        else:
            kicker3 = counts.index(1)
            kicker2 = counts[kicker3+1:].index(1)
            kicker1 = counts[kicker2+1:].index(1)
            return [9, pair, kicker1,kicker2,kicker3] # pair
    else: #High card
        kickers = [i for i,x in enumerate([counts]) if x==1]
        return [10].extend(kickers[::-1])


def hand_score(hand: List[Card]):
        hand.sort(key=lambda x: x.number)
        result = []
        if is_flush(hand):



def best_hand(board, hand):
    pass
    #hand_score( 5 cards from [board.extend(hand)]) #21 calls to hand_score 7 C 5
    #return max(hand_score, hand)