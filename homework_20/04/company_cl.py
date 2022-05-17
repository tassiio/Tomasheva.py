class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age


class Employee(Person):
    def salary(self):
        pass


class Manager(Employee):
    def salary(self):
        return 13000


class Agent(Employee):
    def __init__(self, name, surname, age, volume_of_sales):
        super().__init__(name, surname, age)
        self.volume_of_sales = volume_of_sales

    def salary(self):
        return 5000 + 0.05 * self.volume_of_sales


class Worker(Employee):
    def __init__(self, name, surname, age,  working_hours):
        super().__init__(name, surname, age)
        self.working_hours = working_hours

    def salary(self):
        return 100 * self.working_hours
