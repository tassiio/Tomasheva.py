from Artem_cl import *
import random

home = Home()
person_one = Person('Nastya', home)
person_two = Person('Polina', home)

days = 0
while days < 365:
    days += 1
    what_to_do = random.choice([i for i in range(1, 7)])
    if person_one.bellyful < 20:
        person_one.eat()
    elif person_two.bellyful < 20:
        person_two.eat()
    elif home.fridge_with_food < 10:
        if random.choice([1, 2]) == 1:
            person_one.buy_food()
        else:
            person_two.buy_food()
    elif home.money < 50:
        if random.choice([1, 2]) == 1:
            person_one.work()
        else:
            person_two.work()
    elif what_to_do == 1:
        person_one.work()
        person_two.work()
    elif what_to_do == 2:
        person_one.eat()
        person_two.eat()
    else:
        person_one.gaming()
        person_two.gaming()
    if not person_one.is_alive():
        print(f'Sorry, but {person_one.name} is dead...')
        break
    if not person_two.is_alive():
        print(f'Sorry, but {person_two.name} is dead...')
        break
    print(f'Day №{days}:\n', person_one, '\n', person_two)
