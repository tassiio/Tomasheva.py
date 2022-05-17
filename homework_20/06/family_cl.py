class Husband:
    def __init__(self, name: str, home, bellyful=30, happiness=100):
        self.name = name
        self.__home = home
        self.bellyful = bellyful
        self.happiness = happiness

    def eat(self, how_much: int):
        assert how_much < 31, "It's binge eating"
        self.bellyful += how_much
        self.__home.fridge_with_food -= how_much
        print(f'{self.name} eats {how_much} food.')

    def gaming(self):
        self.bellyful -= 10
        self.happiness += 20
        print(f'{self.name} plays games today.')

    def go_for_work(self):
        self.bellyful -= 10
        self.__home.money += 150
        print(f'{self.name} goes to work today.')

    def pet_the_cat(self):
        self.happiness += 5
        print(f'{self.name} pets the cat.')

    def is_alive(self):
        if self.bellyful > 0 and self.happiness > 10:
            return True
        elif self.bellyful <= 0 and self.happiness > 10:
            return False, 'Dead from hunger.'
        elif self.bellyful > 0 and self.happiness <= 10:
            return False, 'Dead from depression.'
        else:
            return False, 'Dead...'

    def __str__(self):
        return self.name + ': bellyful -> ' + str(self.bellyful) + ', happiness -> ' + str(self.happiness)


class Wife:
    def __init__(self, name: str, home, bellyful=30, happiness=100):
        self.name = name
        self.__home = home
        self.bellyful = bellyful
        self.happiness = happiness

    def eat(self, how_much: int):
        assert how_much < 31, "It's binge eating"
        self.bellyful += how_much
        self.__home.fridge_with_food -= how_much
        print(f'{self.name} eats {how_much} food.')

    def buy_food(self, for_people: int, for_cat: int):
        self.bellyful -= 10
        self.__home.fridge_with_food += for_people
        self.__home.feed += for_cat
        self.__home.money -= for_people + for_cat
        print(f'{self.name} bought {for_people} food for people and {for_cat} for cat.')

    def buy_coat(self):
        self.bellyful -= 10
        self.__home.money -= 350
        self.happiness += 60
        print(f'{self.name} bought the coat.')

    def clean(self, how_much):
        assert how_much < 100, 'Wife is not a cleaning woman.'
        self.__home.dirt -= how_much
        self.bellyful -= 10
        print(f'{self.name} cleans the house {how_much} today.')

    def pet_the_cat(self):
        self.happiness += 5
        print(f'{self.name} pets the cat.')

    def is_alive(self):
        if self.bellyful > 0 and self.happiness > 10:
            return True
        elif self.bellyful <= 0 and self.happiness > 10:
            return False, 'Dead from hunger.'
        elif self.bellyful > 0 and self.happiness <= 10:
            return False, 'Dead from depression.'
        else:
            return False, 'Dead...'

    def __str__(self):
        return self.name + ': bellyful -> ' + str(self.bellyful) + ', happiness -> ' + str(self.happiness)


class Cat:
    def __init__(self, name, home, bellyful=30):
        self.name = name
        self.__home = home
        self.bellyful = bellyful

    def eat(self, how_much):
        assert how_much < 10, "It's too much for the cat"
        self.bellyful += how_much * 2
        self.__home.feed -= how_much
        print(f'{self.name} eats {how_much} food.')

    def sleep(self):
        self.bellyful -= 10
        print(f'{self.name} sleeps.')

    def damage_wallpaper(self):
        self.bellyful -= 10
        self.__home.dirt += 5
        print(f'{self.name} damages the wallpaper.')

    def is_alive(self):
        if self.bellyful > 0:
            return True
        else:
            return False, 'Dead from hunger.'

    def __str__(self):
        return self.name + ': bellyful -> ' + str(self.bellyful)


class House:
    def __init__(self, money=100, fridge_with_food=50, feed=30, dirt=0):
        self.money = money
        self.fridge_with_food = fridge_with_food
        self.feed = feed
        self.dirt = dirt

    def get_dirty(self):
        self.dirt += 5

    def __str__(self):
        return f'House: dirt -> {self.dirt}, food in the fridge -> {self.fridge_with_food}, money -> {self.money}, ' \
               f'feed for cat -> {self.feed}'
