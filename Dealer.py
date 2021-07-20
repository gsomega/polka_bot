from typing import Tuple
from collections import deque
from Game import Game


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


