from CardTypes import Suit, Rank
from Deck import StandardDeck
from typing import List, Tuple
from collections import deque

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



class TexasHoldem(Game):
    def __init__(self, blinds: Tuple[float, float]):
        super().__init__()
        self.blinds = blinds
        self.big_blind = blinds[0]
        self.small_blind = blinds[1]
        self.bid_order = deque(self.players)
        self.call_amount = self.big_blind

    def start_game(self):
        self.bid_order[-2].bid(self.small_blind)
        self.bid_order[-1].bid(self.big_blind)


        #list of players


    def rotate_action(self):
        # rotate "clockwise" order of play
        self.bid_order.rotate(-1)

        # if everyone is out
        if all(not player.active for player in self.bid_order):
            print("Round over!")
            return

        # get active player
        while not self.bid_order[0].active:
            self.bid_order.rotate(-1)

        print(f"Action is on {self.bid_order[0].name}.")
        #send list of available actions to the player.agent
        #

        #who is the last person to raise

        #how does a side-pot work? (trickiest?)
        #this means we need to keep track of how much each player has put in?


class Player:
    def __init__(self, game: Game, name: str, money: float):
        self.game = game
        self.name = name
        self.money = money
        self.money_in_current_pot = 0
        self.hand: List[Card] = []
        self.active = True

    def call(self):
        money_to_call = self.game.call_amount - self.money_in_current_pot
        if money_to_call > self.money: return False

        self.game.pot_size += money_to_call
        self.money -= money_to_call
        return True

    def all_in(self):
        pass

    def re_raise(self, bet: float):
    def raise_bet(self, bet: float):
        if self.money_in_current_pot != self.game.call_amount: return False
        if bet == self.money: self.all_in()
        elif bet > self.money: return False
        else:
            self.game.pot_size += bet
            self.money -= bet
            self.game.call_amount += bet

        pass

    def fold(self):
        print("Folding")
        self.active = False
        return True

    def check(self):
        return True

class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.number = rank