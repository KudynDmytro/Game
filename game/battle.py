import game.unit as u
import random as rand
import time


class Battle:
    def __init__(self, unit1, unit2):
        if isinstance(unit1, u.Unit) and isinstance(unit2, u.Unit):
            self.fighter_1 = unit1
            self.fighter_2 = unit2
            self.count = 0
            self.coin = self.beginer(unit1, unit2)

    def begin(self):
        if self.coin == self.fighter_1:
            self.fight(self.fighter_1, self.fighter_2)
        elif self.coin == self.fighter_2:
            self.fight(self.fighter_2, self.fighter_1)

    def turn(self, unit, enemy):
        if unit.status == 'stunned':
            unit.status = None
            pass
        else:
            self.count += 1
            print('Turn #', self.count)
            move = input(f"{unit.name_}'s turn:")
            if move == f'attack {enemy.name_}':
                unit.attack(enemy)
                print(f'{unit.name_}:{unit.stats}\n{enemy.name_}:{enemy.stats}')
            elif move == 'use ability1':
                if isinstance(unit, u.Warrior):
                    unit.rush()
                    print(f'{unit.name_}:{unit.stats}\n{enemy.name_}:{enemy.stats}')
            elif move == 'use ability2':
                if isinstance(unit, u.Warrior):
                    unit.stun(enemy)
                    print(enemy.name_, enemy.status)
            else:
                pass

    def fight(self, u1, u2):
        self.turn(u1, u2)
        while u1.hp_ > 0 and u2.hp_ > 0:
            if u2.hp_ <= 0:
                self.winner = u1.name_
                return self.winner
            self.turn(u2, u1)
            if u1.hp_ <= 0:
                self.winner = u2.name_
                return self.winner
            self.fight(u1, u2)

    def beginer(self, f1, f2):
        self.rnd = rand.randint(1, 2)
        if self.rnd == 1:
            return f1
        else:
            return f2




