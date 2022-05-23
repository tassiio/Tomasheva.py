class Person:
    def __init__(self, name, home, bellyful=50):
        self.name = name
        self.__home = home
        self.bellyful = bellyful

    def eat(self):
        self.bellyful += 1
        self.__home.fridge_with_food -= 1

    def work(self):
        self.bellyful -= 1
        self.__home.money += 1

    def gaming(self):
        self.bellyful -= 1

    def buy_food(self):
        self.__home.fridge_with_food += 1
        self.__home.money -= 1

    def is_alive(self):
        if self.bellyful > 0:
            return True
        else:
            return False

    def __str__(self):
        return self.name + ': bellyful -> ' + str(self.bellyful) + ', food -> ' + str(self.__home.fridge_with_food) + \
               ', money -> ' + str(self.__home.money)


class Home:
    def __init__(self, fridge_with_food=50, money=0):
        self.fridge_with_food = fridge_with_food
        self.money = money
