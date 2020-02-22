import game.unit as un
import game.items as itm
import game.battle as bat

Knight = un.Warrior('Horison', 15, 6, 5, 40, 5)
Orc = un.Warrior('Drex', 20, 10, 2, 40, 5)
Sword = itm.RightHand('Silver edge', 0, 6, 2, None, None)
b = bat.Battle(Knight, Orc)
b.begin()
print(f'{b.winner} wins!')
