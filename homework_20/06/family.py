import random
from family_cl import *
house = House()
husband = Husband('He', house)
wife = Wife('She', house)
cat = Cat('cat', house)

total_money = 0
total_coats = 0
total_food = 0
day = 1
while day < 366:
    print(f'DAY {day}: ')
    house.get_dirty()

    if house.dirt > 90:
        husband.happiness -= 10
        wife.happiness -= 10
        wife.clean(random.randint(30, 99))

    if day % 7 != [5, 6]:
        husband.go_for_work()
        total_money += 150
        hus_food = random.randint(10, 30)
        husband.eat(hus_food)
        husband.pet_the_cat()
        w_food = random.randint(5, 30)
        wife.eat(w_food)
        total_food += hus_food + w_food
        wife.pet_the_cat()

    else:
        husband.gaming()
        hus_food = random.randint(15, 30)
        husband.eat(hus_food)
        husband.pet_the_cat()
        w_food = random.randint(5, 30)
        wife.eat(w_food)
        total_food += hus_food + w_food

    if random.choices([0, 1], [7/10, 1/100])[0] == 1:
        wife.buy_coat()
        total_coats += 1
        wife.pet_the_cat()

    if random.choices([0, 1], [6/7, 1/7])[0] == 1 and house.dirt > 50:
        wife.clean(random.randint(5, 99))

    if house.fridge_with_food < 5:
        wife.buy_food(random.randint(30, 80), 0)
    elif house.feed < 5:
        wife.buy_food(0, random.randint(5, 30))

    cat.eat(random.randint(1, 9))
    if random.choices([0, 1], [4/7, 3/7])[0] == 1:
        cat.damage_wallpaper()
        cat.sleep()

    if not husband.is_alive() or not wife.is_alive() or not cat.is_alive():
        break

    day += 1

    print(husband)
    print(wife)
    print(cat)
    print(house)

    print('--------------------------')

print('Total money: ', total_money)
print('Total coats: ', total_coats)
print('Total food: ', total_food)
