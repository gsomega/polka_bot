from typing import List
from CardTypes import Card


class Player:
    def __init__(self, game, name: str, money: float):
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

    #def re_raise(self, bet: float):
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