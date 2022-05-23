from warrior_cl import Warrior
import random

f_name = input('Enter the name of the first fighter:\n')
s_name = input('Enter the name of the second fighter:\n')

f_fighter = Warrior(f_name)
s_fighter = Warrior(s_name)

f_is_alive = True
s_is_alive = True

amount = 0
while f_is_alive and s_is_alive:
    amount += 1
    print('############')
    print(f'  ROUND {amount}!')
    if random.choices([1, 2], k=1)[0] == 1:
        print(f'{s_name} strikes {f_name}.')
        f_fighter.damage()
        print('Health after the battle:')
        print(f'{f_name}:', f_fighter.get_health_points())
        print(f'{s_name}:', s_fighter.get_health_points())
    else:
        print(f'{f_name} strikes {s_name}.')
        s_fighter.damage()
        print('Health after the battle:')
        print(f'{f_name}:', f_fighter.get_health_points())
        print(f'{s_name}:', s_fighter.get_health_points())

    f_is_alive = f_fighter.is_alive()
    s_is_alive = s_fighter.is_alive()
    print('############')

if f_is_alive:
    print(f'\n{f_name} WON!')
else:
    print(f'\n{s_name} WON!')
