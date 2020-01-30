import game.unit as u
import random as rand
import time


class Battle:
    def __init__(self, unit1, unit2):
        if isinstance(unit1, u.Unit) and isinstance(unit2, u.Unit):

            self.fighter_1 = unit1
            self.fighter_2 = unit2
            self.coin = self.beginer(unit1, unit2)

    def begin(self):
        if self.coin == self.fighter_1:
            self.fight(self.fighter_1, self.fighter_2)
        elif self.coin == self.fighter_2:
            self.fight(self.fighter_2, self.fighter_1)

    def fight(self, u1, u2):
        while u1.hp_ > 0 and u2.hp_ > 0:
            self.hit(u1, u2)
            if u2.hp_ <= 0:
                self.winner = u1.name_
                return self.winner
            elif u1.hp_ <= 0:
                self.winner = u2.name_
                return self.winner
            self.fight(u1, u2)

    def beginer(self, f1, f2):
        self.rnd = rand.randint(1, 2)
        if self.rnd == 1:
            return f1
        else:
            return f2

    def hit(self, first, second):
        first.attack(second)
        print(first.name_, 'attack', second.name_, '\n', second.name_, '\'s HP-->', second.hp_)
        time.sleep(3)
        second.attack(second)
        print(second.name_, 'attack', first.name_, '\n', first.name_, '\'s HP-->', first.hp_)
        time.sleep(3)

