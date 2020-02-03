import random as rand
import game.items as i


class Unit:
    def __init__(self, name, hp, dmg, arm, head_slot=None, body_slot=None, right_hand_slot=None, left_hand_slot=None,
                 arms_slot=None, legs_slot=None, artifact_slot=None):
        self.name_ = name
        self._chance1 = None
        self._chance2 = None
        self.head_slot_ = head_slot
        self.body_slot_ = body_slot
        self.right_hand_slot_ = right_hand_slot
        self.left_hand_slot_ = left_hand_slot
        self.arms_slot_ = arms_slot
        self.legs_slot_ = legs_slot
        self.artifact_slot_ = artifact_slot
        if type(hp) == int and type(dmg) == int and type(arm) == int:
            if hp > 0:
                self.hp_ = hp
            else:
                print('Unit can\'t have negative health!')
            if dmg >= 0 and arm >= 0:
                self.dmg_ = dmg
                self.arm_ = arm
            else:
                print('Unit can\'t have negative damage or armor!')
        else:
            print('NO, you must enter numbers!')

    def set_crit(self, arg):
        try:
            self.chance_ = rand.random()
            if arg >= rand.randint(0, 100):
                self._chance1 = True
            else:
                self._chance1 = False
        except:
            raise Exception

    def get_crit(self):
        return self._chance1

    crit = property(get_crit, set_crit)

    def dodge(self, value):
        try:
            if value >= rand.randint(0, 100):
                self._chance2 = True
            else:
                self._chance2 = False
        except:
            raise Exception

    def attack(self, enemy):
        """Это функция атаки, она выполняет алгоритм нанесения урона другому юниту"""
        if type(enemy) != Unit:
            print('You can attack only units')
        if enemy._chance2 == True:
            print('MISS')
            enemy.hp_ -= 0
        elif self._chance1 == True:
            print('CRIT')
            enemy.hp_ -= (self.dmg_ * 2 - enemy.arm_)
        else:
            enemy.hp_ -= (self.dmg_ - enemy.arm_)

        return enemy.hp_

    def item_buff(self, stuff):
        """даёт бафы от снаряжения"""
        if stuff.give_hp_ is not None and stuff.give_dmg_ is not None and stuff.give_arm_ is not None:
            self.hp_ += stuff.give_hp_
            self.dmg_ += stuff.give_dmg_
            self.arm_ += stuff.give_arm_
            return self.hp_, self.dmg_, self.arm_
        elif stuff.give_hp_ is not None and stuff.give_dmg_:
            self.hp_ += stuff.give_hp_
            self.dmg_ += stuff.give_dmg_
            return self.dmg_, self.hp_
        elif stuff.give_dmg_ is not None and stuff.give_arm_:
            self.dmg_ += stuff.give_dmg_
            self.arm_ += stuff.give_arm_
            return self.dmg_, self.arm_
        elif stuff.give_hp_ is not None and stuff.give_arm_ is not None:
            self.hp_ += stuff.give_hp_
            self.arm_ += stuff.give_arm_
            return self.hp_, self.arm_

    def item_unbuff(self, itm):
        if itm.give_hp_ is not None and itm.give_dmg_ is not None and itm.give_arm_ is not None:
            self.hp_ -= itm.give_hp_
            self.dmg_ -= itm.give_dmg_
            self.arm_ -= itm.give_arm_
            return self.hp_, self.dmg_, self.arm_
        elif itm.give_hp_ is not None and itm.give_dmg_:
            self.hp_ -= itm.give_hp_
            self.dmg_ -= itm.give_dmg_
            return self.dmg_, self.hp_
        elif itm.give_dmg_ is not None and itm.give_arm_:
            self.dmg_ -= itm.give_dmg_
            self.arm_ -= itm.give_arm_
            return self.dmg_, self.arm_
        elif itm.give_hp_ is not None and itm.give_arm_ is not None:
            self.hp_ -= itm.give_hp_
            self.arm_ -= itm.give_arm_
            return self.hp_, self.arm_

    def check_slot(self, atr):
        """проверяет на какой слот даное снаряжение"""
        if isinstance(atr, i.RightHand):
            self.right_hand_slot_ = atr.name_
            self.item_buff(atr)
            return self.right_hand_slot_
        elif isinstance(atr, i.LeftHand):
            self.left_hand_slot_ = atr.name_
            self.item_buff(atr)
            return self.left_hand_slot_
        elif isinstance(atr, i.TwoHand):
            self.right_hand_slot_ = atr.name_
            self.left_hand_slot_ = atr.name_
            self.item_buff(atr)
            return self.right_hand_slot_, self.left_hand_slot_
        elif isinstance(atr, i.Head):
            self.head_slot_ = atr.name_
            self.item_buff(atr)
            return self.head_slot_
        elif isinstance(atr, i.Body):
            self.body_slot_ = atr.name_
            self.item_buff(atr)
            return self.body_slot_
        elif isinstance(atr, i.Arms):
            self.arms_slot_ = atr.name_
            self.item_buff(atr)
            return self.arms_slot_
        elif isinstance(atr, i.Legs):
            self.legs_slot_ = atr.name_
            self.item_buff(atr)
            return self.legs_slot_
        elif isinstance(atr, i.Artifact):
            self.artifact_slot_ = atr.name_
            self.item_buff(atr)
            return self.artifact_slot_

    def wear(self, item):
        if isinstance(item, i.Item):
            self.check_slot(item)
        else:
            print('YOU CAN\'T WEAR IT')

    def unwear(self, slot):
        """функция снятия снаряжения"""
        if isinstance(slot, i.RightHand):
            self.right_hand_slot_ = None
            self.item_unbuff(slot)
            return self.right_hand_slot_
        elif isinstance(slot, i.LeftHand):
            self.left_hand_slot_ = None
            self.item_unbuff(slot)
            return self.left_hand_slot_
        elif isinstance(slot, i.TwoHand):
            self.right_hand_slot_ = None
            self.left_hand_slot_ = None
            self.item_unbuff(slot)
            return self.right_hand_slot_, self.left_hand_slot_
        elif isinstance(slot, i.Head):
            self.head_slot_ = None
            self.item_unbuff(slot)
            return self.head_slot_
        elif isinstance(slot, i.Body):
            self.body_slot_ = None
            self.item_unbuff(slot)
            return self.body_slot_
        elif isinstance(slot, i.Arms):
            self.arms_slot_ = None
            self.item_unbuff(slot)
            return self.arms_slot_
        elif isinstance(slot, i.Legs):
            self.legs_slot_ = None
            self.item_unbuff(slot)
            return self.legs_slot_
        elif isinstance(slot, i.Artifact):
            self.artifact_slot_ = None
            self.item_unbuff(slot)
            return self.artifact_slot_

