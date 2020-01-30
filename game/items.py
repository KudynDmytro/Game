class Item:
    def __init__(self, name, give_hp, give_dmg, give_arm, passive_abl, active_abl):
        self.name_ = name
        self.give_hp_ = give_hp
        self.give_dmg_ = give_dmg
        self.give_arm_ = give_arm
        self.passive_abl_ = passive_abl
        self.active_abl_ = active_abl

    """тут будет функционал активной и пассывной способностей предметов"""
    # def active(self, aim = None):
    #     if aim != None:
    # def passive()


class RightHand(Item):
    def __init__(self, name, give_hp, give_dmg, give_arm, passive_abl, active_abl):
        super().__init__(name, give_hp, give_dmg, give_arm, passive_abl, active_abl)


class LeftHand(Item):
    def __init__(self, name, give_hp, give_dmg, give_arm, passive_abl, active_abl):
        super().__init__(name, give_hp, give_dmg, give_arm, passive_abl, active_abl)


class TwoHand(Item):
    """клас двуручного снаряжения"""
    def __init__(self, name, give_hp, give_dmg, give_arm, passive_abl, active_abl):
        super().__init__(name, give_hp, give_dmg, give_arm, passive_abl, active_abl)


class Body(Item):
    def __init__(self, name, give_hp, give_dmg, give_arm, passive_abl, active_abl):
        super().__init__(name, give_hp, give_dmg, give_arm, passive_abl, active_abl)


class Arms(Item):
    def __init__(self, name, give_hp, give_dmg, give_arm, passive_abl, active_abl):
        super().__init__(name, give_hp, give_dmg, give_arm, passive_abl, active_abl)


class Legs(Item):
    def __init__(self, name, give_hp, give_dmg, give_arm, passive_abl, active_abl):
        super().__init__(name, give_hp, give_dmg, give_arm, passive_abl, active_abl)


class Head(Item):
    def __init__(self, name, give_hp, give_dmg, give_arm, passive_abl, active_abl):
        super().__init__(name, give_hp, give_dmg, give_arm, passive_abl, active_abl)


class Artifact(Item):
    def __init__(self, name, give_hp, give_dmg, give_arm, passive_abl, active_abl):
        super().__init__(name, give_hp, give_dmg, give_arm, passive_abl, active_abl)
