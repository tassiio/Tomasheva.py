class Warrior:
    def __init__(self, name):
        self.__name = name
        self.__health_points = 100

    # def __str__(self):
        # return self.__name

    # def get_name(self):
        # return self.__name

    def get_health_points(self):
        return self.__health_points

    def damage(self):
        self.__health_points -= 20

    def is_alive(self):
        if self.__health_points > 0:
            return True
        else:
            return False


