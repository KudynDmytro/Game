import game.unit as un
import game.items as itm
import game.battle as bat

Knight = un.Unit('Horison', 15, 6, 5)
Orc = un.Unit('Drex', 20, 10, 2)
Sword = itm.RightHand('Silver edge', 0, 6, 2, None, None)
Knight.wear(Sword)
Axe = itm.TwoHand('Heavy axe', 5, 9, 0, None, None)
Orc.wear(Axe)
print(Knight.right_hand_slot_)
print(Orc.right_hand_slot_, Orc.left_hand_slot_)
b = bat.Battle(Knight, Orc)
b.begin()
print(b.winner)


