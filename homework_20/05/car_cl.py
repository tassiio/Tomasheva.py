import math


class Car:
    def __init__(self, x: float, y: float, angle: float):
        self.x = x
        self.y = y
        self.angle = angle

    def move(self, distance, angle):
        self.x += distance * math.cos(angle)
        self.y += distance * math.sin(angle)

    def get_location(self):
        print(f'Current location: ({self.x:.{3}f} , {self.y:.{3}f})')


class Bus(Car):
    def __init__(self, x: float, y: float, angle: float, passengers: int, ticket_cost: int):
        super().__init__(x, y, angle)
        assert passengers > 0, 'Amount of passengers should be > 0'
        self.passengers = passengers
        self.__ticket_cost = ticket_cost
        self.__money = self.passengers * self.__ticket_cost

    def come_in(self, people):
        self.passengers += people
        self.__money += people * self.__ticket_cost

    def come_out(self, people):
        self.passengers -= people
        assert self.passengers > 0, 'Amount of passengers should be > 0'

    def move(self, distance, angle):
        self.x += distance * math.cos(angle)
        self.y += distance * math.sin(angle)

    def get_info(self):
        print(f'Amount of passengers: {self.passengers}\nMoney: {self.__money}')
