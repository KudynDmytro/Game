import game.unit as un
import game.items as itm
import game.battle as bat

Knight = un.Unit('Horison', 15, 6, 5)
Orc = un.Unit('Drex', 20, 10, 2)
Sword = itm.RightHand('Silver edge', 0, 6, 2, None, None)
print(Knight.right_hand_slot_)
Knight.wear(Sword)
print(Knight.dmg_, Knight.arm_)
Axe = itm.TwoHand('Heavy axe', 5, 9, 0, None, None)
Orc.wear(Axe)
Knight.unwear(Sword)
print(Knight.right_hand_slot_)
print(Knight.dmg_, Knight.arm_)
# print(Knight.right_hand_slot_)
# print(Orc.right_hand_slot_, Orc.left_hand_slot_)
# b = bat.Battle(Knight, Orc)
# b.begin()
# print(b.winner)
